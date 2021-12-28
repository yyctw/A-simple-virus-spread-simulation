# NSD Term Project (f-21)
## A-simple-virus-spread-simulation
``` Author: Eric Zhong```

## Overview

A simple virus spread simulation, which can modify config.py to set the simulation configuration and run it.

This simulation use C++ computing power to speed up the calculation process in the simulation process and use python to visualize the simulation results.

This simulation combine C++ and python3 by pybind11.

## Build environment

Install the dependencies with Poetry.

``` bash
poetry install --no-dev
```

Compile the \*.so file for run simulation.

``` bash
make
```

## Set config

Modify simulation config in config.py before run simulation.

``` bash
vim config.py
```

## Run

Run simulation using the Poetry environment.

``` bash
poetry run python3 main.py
```

The visualization results of the simulation will saved in ./output_images/Simulation_policy{policy number}.png.

## Simulation result

config

``` bash
        # all input parameter
        # total number of people for simulation(optional, default = 1000(<= 2000))
        self.total_num_people = 2000
        # init number of infected people(percentage or int)(optional, default =
        # 1 %)
        self.infected_people = 0.01
        # moving speed of people(optional, default = 3)
        self.move_speed = 19
        # virus infection rate(optional, default = 70 %)
        self.infect_rate = 0.1
        # virus mortality rate(optional, default = 30 %)
        self.mortality_rate = 0.001
        # recovery rate(optional, default = 30 %)
        self.recovery_rate = 0.001
        # healthcare capacity(optional, default = 100, The mortality rate is
        # halved.)
        self.healthcare_capacity = 100

        # mode = 0 : fast, only get the graph of simulation result, not animation.
        # mode = 1 : slow, show animation on the screen and update immediately.
        # mode = 2 : slow, save animation in Sim.gif.
        self.mode = 2
        # Max simulation step, default = 10000
        self.simu_step = 1000
        # the distance of move one step(every iter move one step), default = 0.001
        self.move_step = 0.001
        # Virus transmission range, default = 0.02
        self.spread_range = 0.02
        # policy = 0 : free without healthcare
        # policy = 1 : free with healthcare
        # policy = 2 : Attempted quarantine
        # policy = 3 : Moderate distancing
        # policy = 4 : Extensive distancing
        self.policy = 0

        # Simulation boundary
        self.left_x = 0.0
        self.right_x = 2.0
        self.up_y = 2.0
        self.down_y = 0.0
```

policy = 0 : free without healthcare

![Simulation_policy0](output_images/Simulation_policy0.gif)

Final result

![Simulation_policy0_result](output_images/Simulation_policy0.png)

---

policy = 1 : free with healthcare (healthcare can reduce the mortality rate by half.)

![Simulation_policy1](output_images/Simulation_policy1.gif)

Final result

![Simulation_policy1_result](output_images/Simulation_policy1.png)

---

policy = 2 : Attempted quarantine (infected people will go to quarantine area.)

![Simulation_policy2](output_images/Simulation_policy2.gif)

Final result

![Simulation_policy2_result](output_images/Simulation_policy2.png)

---

policy = 3 : Moderate distancing (60% people can not move)

![Simulation_policy3](output_images/Simulation_policy3.gif)

Final result

![Simulation_policy3_result](output_images/Simulation_policy3.png)

---

policy = 4 : Extensive distancing (90% people can not move)

![Simulation_policy4](output_images/Simulation_policy4.gif)

Final result

![Simulation_policy4_result](output_images/Simulation_policy4.png)

---

## References

1. [Why outbreaks like coronavirus spread exponentially, and how to “flatten the curve”](https://www.washingtonpost.com/graphics/2020/world/corona-simulator/)

2. [python_corona_simulation](https://github.com/paulvangentcom/python_corona_simulation)

---

### proposal
https://github.com/Eric860730/nsdhw_21au/tree/Eric860730-proposal-submission/proposal/Eric860730

### Completion
11/24 [Feat] Success run on pybind and add test for read class data.

12/14 [Feat] Can run easy simulation on pure cpp environment without policy.

12/16 [Feat] Can run on python with pybind and plot result graph.

12/18 [Feat] Github Action done.

12/18 [Feat] Can plot simulation result as animation.

12/20 [Feat] Finish plot and accelerate simulation time.

12/21 [Feat] Finish all basic policy.

12/28 [Feat] Modify the code structure and accelerate the simulation time successfully.

### Next goal
Prepare final presentation.

### Schedule

:white_check_mark: Week 1: Parser, Simulator

:white_check_mark: Week 2: Simulator(policy: Free)

:white_check_mark: Week 3: Simulator(policy: Attempted quarantine)

:white_check_mark: Week 4: Simulator(policy: Moderate distancing)

:white_check_mark: Week 5: Simulator(policy: Extensive distancing)

:white_check_mark: Week 6: Printer

:white_check_mark: Week 7: Code Optimized.

:red_circle: current doing ---> Week 8: Prepare final presentation.

### TODO

:white_check_mark: Combine my cpp with python by pybind and visualize.

:white_check_mark: Github Action.

:white_check_mark: Increase policy.

:white_large_square: Increase customized policy.

#### for performance

:white_check_mark: Change the type of infected_person from vector to map at line 165 in MySimulator.cpp.

:white_check_mark: Optimized the Simulation time on 10000 population. (total simulation time < 2s)

:white_large_square: Use QT QUICK to accelerate visualization.
