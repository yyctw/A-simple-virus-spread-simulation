from my_simulation.visualize import build_figure
from my_simulation.visualize import draw_current_simu_status
from my_simulation.visualize import run_and_build_animation
import _simulator
import numpy as np


def run(simu_status):
    count = 1000000
    m_hours = 0
    # init figure
    figure, spec, fig1, fig2 = build_figure(simu_status.lx_bound, simu_status.rx_bound, simu_status.dy_bound, simu_status.uy_bound, count, simu_status.total_num_people)
    while count:
        count -= 1
        _simulator.Move(simu_status)
        _simulator.SpreadVirus(simu_status)
        if m_hours == 24:
            _simulator.RecoveredOrDead(simu_status)
            m_hours = 0
        m_hours += 1

        # visualize
        draw_current_simu_status(simu_status, figure, fig1, fig2)


def simulate(simu_status):
    print("In")

    # init
    _simulator.InitSimulation(simu_status)

    # run
    #run(simu_status)

    simulation_steps = 1000
    run_and_build_animation(simu_status, simulation_steps)

    simu_status.print_status
