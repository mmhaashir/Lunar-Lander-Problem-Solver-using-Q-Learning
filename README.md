# Lunar Lander Problem Solver using Q Learning

This Python project solves the Lunar Lander problem from the OpenAI Gym environment using Q-learning. It leverages TensorFlow for reinforcement learning and can be configured to run on a GPU for faster performance, though it can also be run in CPU mode.

![dav_image](https://miro.medium.com/v2/resize:fit:1346/1*i7lxpgt2K3Q8lgEPJu3_xA.png)

## Table of Contents

- [**Introduction**](#intro)
- [**Dependencies**](#dep)
- [**Installation**](#install)
- [**Usage**](#usage)
- [**Results**](#results)
- [**Contribution**](#contr)
- [**Conclusion**](#conc)

## Introduction <a name="intro"></a>

This repository contains Python code that solves the Lunar Lander problem using the Q-Learning algorithm in the OpenAI Gym environment. The Lunar Lander problem is a classic reinforcement learning task where an agent must learn to safely land a spacecraft on the moon's surface.

## Dependencies <a name="dep"></a>

To run this code, you will need the following Python libraries:

- **Gym:** OpenAI Gym provides the environment for the CartPole problem.
- **TensorFlow:** TensorFlow is used for deep reinforcement learning.
- **NumPy:** NumPy is used for numerical operations.
- **Math:** Basic math operations are utilized in the code.
- **Matplotlib:** Matplotlib is used for plotting the rewards over episodes.
- **Time:** Time is used for tracking the execution time.
- **Random:** For generating random numbers required in the project.

## Installation <a name="install"></a>

1. Clone the repository:
   `git clone https://github.com/mmhaashir/Lunar-Lander-Problem-Solver-using-Q-Learning.git`
   
3. Install the required dependencies:
   `pip install gym tensorflow numpy matplotlib`

## Usage <a name="usage"></a>

1. Run the CartPole solver script:
   `python lunar_lander_q_learning.py`
   
3. The script will simulate a specified number of episodes (default is 20,000) using Q-learning and print the sum of rewards obtained in each episode to the command line interface.
   
5. Once the simulation is complete, the script will generate a graph showing the rewards obtained over episodes.

## Results <a name="results"></a>

Upon running the Lunar Lander solver, you can expect to see the sum of rewards for each episode printed to the CLI. Additionally, a graph displaying the rewards obtained over episodes will be generated and saved in the project directory.

## Contributing <a  name="contr"></a>

Contributions to this project are welcome. If you have suggestions or improvements, please open an issue or submit a pull request.

## Conclusion <a name="conc"></a>

In this project, we tackled the classic Lunar Lander problem using Q-learning, a fundamental reinforcement learning technique. 

In conclusion, this Lunar Lander problem solver showcases the potential of reinforcement learning techniques in solving challenging control problems. Whether you're a beginner exploring reinforcement learning or an experienced practitioner looking for a practical example, we hope this project proves to be insightful and useful. Happy coding and happy learning!

