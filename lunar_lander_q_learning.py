import tensorflow as tf, gymnasium as gym, random, math, time, matplotlib.pyplot as plt

print("--> Checking for physical Tensorflow devices")
for device in tf.config.list_physical_devices():
    print(": {}".format(device.name))

!pip install gymnasium

pip install gymnasium[box2d]

with tf.device('/GPU:0'):

    env = gym.make('LunarLander-v2',render_mode='rgb_array')

    number_of_buckets = (10, 10, 10, 10, 10, 10, 2, 2)
    number_of_actions = env.action_space.n

    state_value_bounds = list(zip(env.observation_space.low,env.observation_space.high))

    state_value_bounds[0] = [-1,1]
    state_value_bounds[1] = [-1,1]
    state_value_bounds[2] = [-1,1]
    state_value_bounds[3] = [-1,1]
    state_value_bounds[4] = [-1,1]
    state_value_bounds[5] = [-1,1]
    state_value_bounds[6] = [0,1]
    state_value_bounds[7] = [0,1]

    upperBounds=env.observation_space.high
    lowerBounds=env.observation_space.low


    alpha = 0.1
    gamma = 0.95
    epsilon = 0.2
    num_episodes = 20000
    num_actions = env.action_space.n
    state_size = env.observation_space.shape[0]
    max_steps_per_episode = 1000

    class QLearning:
        def __init__(self,env,alpha,gamma,epsilon,numberEpisodes,numberOfBins,lowerBounds,upperBounds):
            import numpy as np

            self.env=env
            self.alpha=alpha
            self.gamma=gamma
            self.epsilon=epsilon
            self.actionNumber=env.action_space.n
            self.numberEpisodes=numberEpisodes
            self.numberOfBins=numberOfBins
            self.lowerBounds=lowerBounds
            self.upperBounds=upperBounds

            self.sumRewardsEpisode=[]

            self.Qmatrix=np.random.uniform(low=0, high=1, size=(numberOfBins[0],numberOfBins[1],numberOfBins[2],numberOfBins[3],self.actionNumber))

        def returnIndexState(self,state):
            position =      state[0]
            velocity =      state[1]
            angle    =      state[2]
            angularVelocity=state[3]

            cartPositionBin=np.linspace(self.lowerBounds[0],self.upperBounds[0],self.numberOfBins[0])
            cartVelocityBin=np.linspace(self.lowerBounds[1],self.upperBounds[1],self.numberOfBins[1])
            poleAngleBin=np.linspace(self.lowerBounds[2],self.upperBounds[2],self.numberOfBins[2])
            poleAngleVelocityBin=np.linspace(self.lowerBounds[3],self.upperBounds[3],self.numberOfBins[3])

            indexPosition=np.maximum(np.digitize(state[0],cartPositionBin)-1,0)
            indexVelocity=np.maximum(np.digitize(state[1],cartVelocityBin)-1,0)
            indexAngle=np.maximum(np.digitize(state[2],poleAngleBin)-1,0)
            indexAngularVelocity=np.maximum(np.digitize(state[3],poleAngleVelocityBin)-1,0)

            return tuple([indexPosition,indexVelocity,indexAngle,indexAngularVelocity])

        def selectAction(self,state,index):

            if index<500:
                return np.random.choice(self.actionNumber)

            randomNumber=np.random.random()

            if index>7000:
                self.epsilon=0.999*self.epsilon

            if randomNumber < self.epsilon:

                return np.random.choice(self.actionNumber)
            else:
                return np.random.choice(np.where(self.Qmatrix[self.returnIndexState(state)]==np.max(self.Qmatrix[self.returnIndexState(state)]))[0])

        def simulateEpisodes(self):

            for indexEpisode in range(self.numberEpisodes):

                rewardsEpisode=[]

                (stateS,_)=self.env.reset()
                stateS=list(stateS)

                print("Simulating episode {}".format(indexEpisode))

                terminalState=False
                total_reward = 0
                while not terminalState and total_reward < max_steps_per_episode:

                    stateSIndex=self.returnIndexState(stateS)

                    actionA = self.selectAction(stateS,indexEpisode)

                    (stateSprime, reward, terminalState,_,_) = self.env.step(actionA)

                    rewardsEpisode.append(reward)

                    stateSprime=list(stateSprime)

                    stateSprimeIndex=self.returnIndexState(stateSprime)

                    QmaxPrime=np.max(self.Qmatrix[stateSprimeIndex])

                    if not terminalState:
                        error=reward+self.gamma*QmaxPrime-self.Qmatrix[stateSIndex+(actionA,)]
                        self.Qmatrix[stateSIndex+(actionA,)]=self.Qmatrix[stateSIndex+(actionA,)]+self.alpha*error

                    else:
                        error=reward-self.Qmatrix[stateSIndex+(actionA,)]
                        self.Qmatrix[stateSIndex+(actionA,)]=self.Qmatrix[stateSIndex+(actionA,)]+self.alpha*error

                    total_reward+=1

                    stateS=stateSprime

                print("Sum of rewards {}".format(np.sum(rewardsEpisode)))
                self.sumRewardsEpisode.append(np.sum(rewardsEpisode))

        def simulateLearnedStrategy(self):

                (currentState,_)= self.env.reset()
                timeSteps=1000
                obtainedRewards=[]

                for timeIndex in range(timeSteps):
                    print(timeIndex)
                    actionInStateS=np.random.choice(np.where(self.Qmatrix[self.returnIndexState(currentState)]==np.max(self.Qmatrix[self.returnIndexState(currentState)]))[0])
                    currentState, reward, terminated, truncated, info =self.env.step(actionInStateS)
                    obtainedRewards.append(reward)
                    time.sleep(0.05)
                    if (terminated):
                        time.sleep(1)
                        break
                return obtainedRewards,self.env

    ql = QLearning(env,alpha,gamma,epsilon,num_episodes,number_of_buckets,lowerBounds,upperBounds)
    ql.simulateEpisodes()
    (obtainedRewardsOptimal,env) = ql.simulateLearnedStrategy()

    plt.figure(figsize=(12, 5))
    plt.plot(ql.sumRewardsEpisode,color='blue',linewidth=1)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.show()

    env.close()
    np.sum(obtainedRewardsOptimal)
