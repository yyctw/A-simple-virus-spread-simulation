from _simulator import SimulationParameter
import _simulator
import pytest
import timeit
import numpy as np
import os

float_bias = 1e-5

class Test_Simulator:

    def default_parameter(self):
        default_parameter = SimulationParameter(1000, 1, 1, 0.7, 0.3, 5, 100)
        return default_parameter

    def test_dafault_parameters(self):
        default_parameter = self.default_parameter()
        assert 1000 == default_parameter.total_num_people
        assert 1 == default_parameter.infected_people
        assert 1 == default_parameter.move_speed
        assert abs(0.7 - default_parameter.infect_rate) < float_bias
        assert abs(0.3 - default_parameter.mortality_rate) < float_bias
        assert 5 == default_parameter.recovery_time
        assert 100 == default_parameter.healthcare_capacity

    def test_print_status(self):
        default_parameter = self.default_parameter()
        print(f"{default_parameter.print_status}")
