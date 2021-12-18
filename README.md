# NSD Term Project (f-21)
## A-simple-virus-spread-simulation

## Build environment

Install the dependencies with Poetry.

``` bash
poetry install --no-dev
```

Compile the \*.so file for run simulation.

``` bash
make
```

## Usage

Run simulation using the Poetry environment.

``` bash
poetry run python3 main.py
```

The visualization results of the simulation will saved as a Sim.gif file in the root directory of this repo.

---

### proposal
https://github.com/Eric860730/nsdhw_21au/tree/Eric860730-proposal-submission/proposal/Eric860730

### Completion
11/24 [Feat] Success run on pybind and add test for read class data.

12/14 [Feat] Can run easy simulation on pure cpp environment without policy.

12/16 [Feat] Can run on python with pybind and plot result graph.

12/18 [Feat] Github Action done.

12/18 [Feat] Can plot simulation result as animation.

### Next goal
Plot statistic result as animation.

### Schedule

:white_check_mark: Week 1: Parser, Simulator

:white_check_mark: Week 2: Simulator(policy: Free)

:white_large_square: Week 3: Simulator(policy: Attempted quarantine)

:white_large_square: Week 4: Simulator(policy: Moderate distancing)

:white_large_square: Week 5: Simulator(policy: Extensive distancing)

:red_circle: current doing ---> Week 6: Printer  

:white_large_square: Week 7: Flexible time(Add death rate of each age)

:white_large_square: Week 8: Flexible time(Add death rate of each age)

### TODO
:white_check_mark: Combine my cpp with python by pybind and visualize.

:white_check_mark: Github Action.

:white_large_square: Increase policy.

#### for performance
:white_large_square: Change the type of infected_person from vector to unorder_map at line 165 in MySimulator.cpp.

test github action
