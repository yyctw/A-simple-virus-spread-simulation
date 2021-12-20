import _simulator

def init_config():
    # all input parameter
    # total number of people for simulation(optional, default = 1000(<= 2000))
    total_num_people = 1000
    # init number of infected people (percentage or int) (optional, default = 1%)
    infected_people = 0.01
    # moving speed of people (optional, default = 3)
    move_speed = 3
    # virus infection rate (optional, default = 70%)
    infect_rate = 0.1
    # virus mortality rate (optional, default = 30%)
    mortality_rate = 0.01
    # recovery rate (optional, default = 30%)
    recovery_rate = 0.01
    # healthcare capacity (optional, default = 100, The mortality rate is halved.)
    healthcare_capacity = 100

    # mode = 0: fast, only get the graph of simulation result, not animation.
    # mode = 1: slow, show animation on the screen and update immediately.
    # mode = 2: slow, save animation in Sim.gif.
    mode = 2
    # Max simulation step, default = 10000
    simu_step = 100
    # the distance of move one step(every iter move one step), default = 0.001
    move_step = 0.001
    # Virus transmission range, default = 0.02
    spread_range = 0.02

    # Simulation boundary
    left_x = 0.0
    right_x = 2.0
    up_y = 2.0
    down_y = 0.0

    config = _simulator.SimulationParameter(total_num_people, int(infected_people * total_num_people), move_speed, infect_rate, mortality_rate, recovery_rate, healthcare_capacity, left_x, right_x, up_y, down_y, simu_step, mode, move_step, spread_range)

    return config
