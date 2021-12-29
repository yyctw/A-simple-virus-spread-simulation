"""
This file is used to adjust the parameters of simulation.
You can only change the value of each variables, other changes is not allow.
"""
# all input parameter
# total number of people for simulation(optional, default = 1000(<= 10000))
TOTAL_POPULATION = 1000
# init number of infected people(percentage)(optional, default =
# 1 %)
INFECTED_PEOPLE = 0.01
# moving speed of people(optional, default = 3)
MOVE_SPEED = 19
# virus infection rate(optional, default = 0.7)
INFECTED_RATE = 0.7
# virus mortality rate(optional, default = 0.001)
MORTALITY_RATE = 0.001
# recovery rate(optional, default = 0.001)
RECOVERY_RATE = 0.001
# healthcare capacity(optional, default = 100, The mortality rate is
# halved.)
HEALTHCARE_CAPACITY = 100

"""
All the mode below will save the final simulation results in ./output_images/Simulation_policy{x}.png. (x = policy number)
mode = 0 : fast, only save the final result graph of simulation.
mode = 1 : slow, show and update animation on the screen immediately.
mode = 2 : slow, save animation in ./output_images/Simulation_policy{x}.gif.
"""
MODE = 2
# Max simulation step, default = 1000
SIMULATION_STEP = 1000
# the distance of move one step(every iter move one step), default = 0.001
MOVE_STEP = 0.001
# Virus transmission range, default = 0.02
SPREAD_RANGE = 0.02
"""
policy = 0 : free without healthcare.
policy = 1 : free with healthcare.
            The first N(N = HEALTHCARE_CAPACITY) infected people will receive healthcare, and the mortality rate will be halved.
policy = 2 : Attempted quarantine.
            According to ACCEPT_ISOLATION_RATE, the infected were isolated to an area.
policy = 3 : Moderate distancing
            60% people cannot move.
policy = 4 : Extensive distancing
            90% people cannot move.
"""
POLICY = 4

# If policy = 2, the probability of an infected person being quarantined.
ACCEPT_ISOLATION_RATE = 0.95

# Simulation boundary
LEFT_X = 0.0
RIGHT_X = 2.0
UP_Y = 2.0
DOWN_Y = 0.0
