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

The visualization results of the simulation will saved as a Sim.gif file in the root directory of this repo.

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

### Next goal
Add policy.

### Schedule

:white_check_mark: Week 1: Parser, Simulator

:white_check_mark: Week 2: Simulator(policy: Free)

:red_circle: current doing ---> Week 3: Simulator(policy: Attempted quarantine)

:white_large_square: Week 4: Simulator(policy: Moderate distancing)

:white_large_square: Week 5: Simulator(policy: Extensive distancing)

:white_check_mark: Week 6: Printer

:white_large_square: Week 7: Flexible time(Add death rate of each age)

:white_large_square: Week 8: Flexible time(Add death rate of each age)

### TODO
:white_check_mark: Combine my cpp with python by pybind and visualize.

:white_check_mark: Github Action.

:white_large_square: Increase policy.

#### for performance
:white_large_square: Change the type of infected_person from vector to unorder_map at line 165 in MySimulator.cpp.
