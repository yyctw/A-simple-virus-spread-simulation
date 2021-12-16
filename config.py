import _simulator

def init_config():
    # all input parameter
    # total number of people for simulation(optional, default = 1000(<= 2000))
    total_num_people = 1000
    # init number of infected people (percentage or int) (optional, default = 1%)
    infected_people = 0.01
    # moving speed of people (optional, default = 1)
    move_speed = 1
    # virus infection rate (optional, default = 70%)
    infect_rate = 0.7
    # virus mortality rate (optional, default = 30%)
    mortality_rate = 0.3
    # recovery rate (optional, default = 30%)
    recovery_rate = 0.3
    # healthcare capacity (optional, default = 100, The mortality rate is halved.)
    healthcare_capacity = 100

    config = _simulator.SimulationParameter(total_num_people, int(infected_people * total_num_people), move_speed, infect_rate, mortality_rate, recovery_rate, healthcare_capacity, 0.0, 2.0, 2.0, 0.0)

    return config
