from _simulator import SimulationParameter
import _simulator
import pytest
import timeit
import numpy as np
import os
from config import config
from main import set_config

float_bias = 1e-5

class Test_Simulator:

    def set_simu(self):
        m_config = config()
        simulation = set_config(m_config)
        return simulation, m_config

    def test_config(self):
        simulation, mcon = self.set_simu()
        assert mcon.total_num_people == simulation.total_num_people
        assert mcon.infected_people*mcon.total_num_people == simulation.infected_people
        assert mcon.move_speed == simulation.move_speed
        assert abs(mcon.infect_rate - simulation.infect_rate) < float_bias
        assert abs(mcon.mortality_rate - simulation.mortality_rate) < float_bias
        assert abs(mcon.recovery_rate - simulation.recovery_rate) < float_bias
        assert mcon.healthcare_capacity == simulation.healthcare_capacity

    def test_print_status(self):
        simulation, mcon= self.set_simu()
        simulation.print_status

    def test_Init_Simulation(self):
        simulation, mcon = self.set_simu()
        _simulator.InitSimulation(simulation)
        for i in range(simulation.num_infected):
            assert 1 == simulation.g_person_status[i].status

    def test_move(self):
        simulation, mcon = self.set_simu()
        _simulator.InitSimulation(simulation)
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


