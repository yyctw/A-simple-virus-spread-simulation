"""
This file is used to adjust the parameters of simulation.
You can only change the value of each variables, other changes is not allow.
"""
class config():
    def __init__(self):
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
