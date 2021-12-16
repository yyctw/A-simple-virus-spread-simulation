from _simulator import SimulationParameter
import _simulator
import pytest
import timeit
import numpy as np
import os

float_bias = 1e-5

class Test_Simulator:

    def default_parameter(self):
        default_parameter = SimulationParameter(1000, 5, 1, 0.7, 0.3, 0.3, 100, 0.0, 2.0, 2.0, 0.0)
        return default_parameter

    def test_dafault_parameters(self):
        default_parameter = self.default_parameter()
        assert 1000 == default_parameter.total_num_people
        assert 5 == default_parameter.infected_people
        assert 1 == default_parameter.move_speed
        assert abs(0.7 - default_parameter.infect_rate) < float_bias
        assert abs(0.3 - default_parameter.mortality_rate) < float_bias
        assert abs(0.3 - default_parameter.recovery_rate) < float_bias
        assert 100 == default_parameter.healthcare_capacity

    def test_print_status(self):
        default_parameter = self.default_parameter()
        default_parameter.print_status

    def test_Init_Simulation(self):
        default_parameter = self.default_parameter()
        _simulator.InitSimulation(default_parameter)
        for i in range(default_parameter.num_infected):
            assert 1 == default_parameter.g_person_status[i].status

    def test_move(self):
        default_parameter = self.default_parameter()
        _simulator.InitSimulation(default_parameter)
        old_x = []
        old_y = []
        for i in range(default_parameter.total_num_people):
            old_x.append(default_parameter.g_person_status[i].coord_x)
            old_y.append(default_parameter.g_person_status[i].coord_y)
        _simulator.Move(default_parameter)
        new_x = []
        new_y = []
        for i in range(default_parameter.total_num_people):
            new_x.append(default_parameter.g_person_status[i].coord_x)
            new_y.append(default_parameter.g_person_status[i].coord_y)
        assert old_x != new_x
        assert old_y != new_y


