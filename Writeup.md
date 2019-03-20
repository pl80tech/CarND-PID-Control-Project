# **PID Control Project** 
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

## Writeup

This is my writeup for the project "PID Control" of Self Driving Car Nanadegree on Udacity.

---

### Contents

* [About PID Control Project](#About-PID-Control-Project)
* [Project code](#Project-code)
* [Rubric Points](#Rubric-Points)
* [Code compilation](#Code-compilation)
* [Implementation](#Implementation)
* [Reflection](#Reflection)
	* [Effect of each components](#Effect-of-each-components)
	* [How to choose the hyperparameters](#How-to-choose-the-hyperparameters)
* [Simulation](#Simulation)

[//]: # (Image References)

[tuneKp]: ./log/Kp_tuning.jpg "Result with different Kp"
[tuneKi]: ./log/Ki_tuning.jpg "Result with different Ki"
[tuneKd]: ./log/Kd_tuning.jpg "Result with different Kd"

[animation]: ./output/SimulationWithTunedCoefficient.gif "Simulation with tuned coefficients"

---
## About PID Control Project

The goals / steps of this project are the following:

* The goal of this project is to implement a PID controller in C++ to maneuver the vehicle around the track.
* More detail explanation can be found in [README](https://github.com/pl80tech/CarND-PID-Control-Project/blob/master/README.md)

---
## Project code

Here is my working repository for this project:

https://github.com/pl80tech/CarND-PID-Control-Project.git

It is imported and frequently updated (cherry-pick or merge) from below original repository:

https://github.com/udacity/CarND-PID-Control-Project.git

---
## Rubric Points

Here are the [Rubric Points](https://review.udacity.com/#!/rubrics/1972/view) which need to be addressed to meet the requirements of this project. Each point/criteria is explained in next sections.

---
## Code compilation

The final solution is implemented in [/src/main.cpp](https://github.com/pl80tech/CarND-PID-Control-Project/blob/master/src/main.cpp) and [PID.cpp](https://github.com/pl80tech/CarND-PID-Control-Project/blob/master/src/PID.cpp). It can be compiled successfully with **cmake** and **make** (as explained in [README](https://github.com/pl80tech/CarND-PID-Control-Project/blob/master/README.md)).

```shell
$ cmake ..
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done

$ make
Scanning dependencies of target pid
[ 33%] Building CXX object CMakeFiles/pid.dir/src/PID.cpp.o
[ 66%] Building CXX object CMakeFiles/pid.dir/src/main.cpp.o
[100%] Linking CXX executable pid
[100%] Built target pid
```

---
## Implementation

The process for PID control is implemented in main() function on [/src/main.cpp](https://github.com/pl80tech/CarND-PID-Control-Project/blob/master/src/main.cpp) and each function of PID class on [/src/PID.cpp](https://github.com/pl80tech/CarND-PID-Control-Project/blob/master/src/PID.cpp), following the base algorithm as presented in the lesson.

---
## Reflection

### Effect of each components

### How to choose the hyperparameters

The code is implemented so that the coefficients Kp/Ki/Kd can be passed directly from command line (like below example) and the simulated data (CTE) is saved in log file with format 20YYMMDD_HHMMSS_cte_Kpxx_Kixx_Kdxx.txt for easy visualization & tuning.

```shell
$ ./pid 0.1 0.0001 1
Initial values: kp = 0.1, ki = 0.0001, kd = 1
Listening to port 4567
```

The save logs are then processed (as below) by a python script [/log/data_visualize.py](https://github.com/pl80tech/CarND-PID-Control-Project/blob/master/log/data_visualize.py) to visualize the simulated data of multiple combinations (keeping 2 coefficients while changing the remaining one in small range) for easy comparison.

```shell
$ python data_visualize.py <log1> <log2> <log3> <title> <xlabel> <ylabel> <legend1> <legend2> <legend3> <savefile>
```

Here are the observation results, from which I chose Kp=0.1, Ki=0.001, Ki=1 as final/tuned coefficients.

| Tuning parameters       | Visualization           |
|:-----------------------:|:-----------------------:|
| Kp                      | ![alt text][tuneKp]     |
| Ki                      | ![alt text][tuneKi]     |
| Kd                      | ![alt text][tuneKd]     |

---
## Simulation

Here is the simulation video with tuned coefficients (Kp=0.1, Ki=0.001, Ki=1). Click on the thumbnail animated gif to view the video directly on Youtube or click on the hyperlink to download the video on Github.

| Link on Github | Link on Youtube |
|:--------------:|:---------------:|
| [Simulation video](https://github.com/pl80tech/CarND-PID-Control-Project/blob/master/output/SimulationWithTunedCoefficient.mp4) | [![alt text][animation]](https://www.youtube.com/watch?v=zLosrupTjGo) |