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

    def init_simulation(self):
        simulation = _simulator.SimulationState(
            1000,
            50,
            19,
            1.0,
            0.001,
            0.001,
            100,
            0.0,
            2.0,
            2.0,
            0.0,
            1000,
            0,
            0.001,
            0.02,
            0,
            0.95)
        return simulation


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
        for j in range(simulation.num_infected, simulation.total_num_people):
            assert 0 == simulation.g_person_status[j].status


    def test_move(self):
        simulation = self.init_simulation()
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
