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

---
## Reflection

### Effect of each components

### How to choose the hyperparameters

| Tuning parameters       | Visualization           |
|:-----------------------:|:-----------------------:|
| Kp                      | ![alt text][tuneKp]     |
| Ki                      | ![alt text][tuneKi]     |

---
## Simulation

| Filename | Link on Youtube |
|:--------:|:---------------:|
| Simulation video | [![alt text][animation]](https://www.youtube.com/watch?v=zLosrupTjGo) |