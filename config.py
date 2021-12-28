"""
This file is used to adjust the parameters of simulation.
You can only change the value of each variables, other changes is not allow.
"""
# all input parameter
# total number of people for simulation(optional, default = 1000(<= 2000))
TOTAL_POPULATION = 10000
# init number of infected people(percentage)(optional, default =
# 1 %)
INFECTED_PEOPLE = 0.01
# moving speed of people(optional, default = 3)
MOVE_SPEED = 19
# virus infection rate(optional, default = 70 %)
INFECTED_RATE = 1.0
# virus mortality rate(optional, default = 30 %)
MORTALITY_RATE = 0.001
# recovery rate(optional, default = 30 %)
RECOVERY_RATE = 0.001
# healthcare capacity(optional, default = 100, The mortality rate is
# halved.)
HEALTHCARE_CAPACITY = 100

# mode = 0 : fast, only get the graph of simulation result, not animation.
# mode = 1 : slow, show animation on the screen and update immediately.
# mode = 2 : slow, save animation in Sim.gif.
MODE = 0
# Max simulation step, default = 10000
SIMULATION_STEP = 1000
# the distance of move one step(every iter move one step), default = 0.001
MOVE_STEP = 0.001
# Virus transmission range, default = 0.02
SPREAD_RANGE = 0.02
# policy = 0 : free without healthcare
# policy = 1 : free with healthcare
# policy = 2 : Attempted quarantine
# policy = 3 : Moderate distancing
# policy = 4 : Extensive distancing
POLICY = 0

# Simulation boundary
LEFT_X = 0.0
RIGHT_X = 2.0
UP_Y = 2.0
DOWN_Y = 0.0
