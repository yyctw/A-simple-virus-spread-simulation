from _simulator import SimulationState
import _simulator
import pytest
import timeit
import numpy as np
import os
import config
from main import set_simulation_state

float_bias = 1e-5

class Test_Simulator:

    def test_set_simulation_state(self):
        simulation = set_simulation_state(config)
        assert config.TOTAL_POPULATION == simulation.total_num_people
        assert config.INFECTED_PEOPLE*config.TOTAL_POPULATION == simulation.infected_people
        assert config.MOVE_SPEED== simulation.move_speed
        assert abs(config.INFECTED_RATE - simulation.infect_rate) < float_bias
        assert abs(config.MORTALITY_RATE - simulation.mortality_rate) < float_bias
        assert abs(config.RECOVERY_RATE - simulation.recovery_rate) < float_bias
        assert config.HEALTHCARE_CAPACITY == simulation.healthcare_capacity

        for i in range(simulation.num_infected):
            assert 1 == simulation.g_person_status[i].status

    def test_print_status(self):
        simulation = set_simulation_state(config)
        simulation.print_status


    def test_move(self):
        simulation = set_simulation_state(config)
        old_x = []
        old_y = []
        for i in range(simulation.total_num_people):
            old_x.append(simulation.g_person_status[i].coord_x)
            old_y.append(simulation.g_person_status[i].coord_y)
        _simulator.Move(simulation)
        new_x = []
        new_y = []
        for i in range(simulation.total_num_people):
            new_x.append(simulation.g_person_status[i].coord_x)
            new_y.append(simulation.g_person_status[i].coord_y)
        assert old_x != new_x
        assert old_y != new_y
