from my_simulation.visualize import build_figure
from my_simulation.visualize import draw_current_simu_status
from my_simulation.visualize import run_and_build_animation
from my_simulation.visualize import draw_simu
from my_simulation.visualize import population
from my_simulation.visualize import print_in_terminal
import _simulator
import numpy as np
import sys


def run(simu_status):
    frames = 0
    max_frames = simu_status.simu_step
    m_hours = 0

    # init figure
    figure, spec, fig1, fig2 = build_figure(simu_status.lx_bound, simu_status.rx_bound, simu_status.dy_bound, simu_status.uy_bound, max_frames, simu_status.total_num_people)

    count_pop = population()

    print_in_terminal(frames, simu_status)
    while frames < max_frames:
        if simu_status.num_infected == 0:
            break
        frames += 1
        _simulator.Move(simu_status)
        _simulator.SpreadVirus(simu_status)
        if m_hours == 24:
            _simulator.RecoveredOrDead(simu_status)
            m_hours = 0
        m_hours += 1

        count_pop.health.append(simu_status.num_health)
        count_pop.infected.append(simu_status.num_infected)
        count_pop.recovered.append(simu_status.num_recovered)
        count_pop.dead.append(simu_status.num_dead)
        count_pop.frames.append(frames)

        _simulator.ClassifyPeople(simu_status)
        _simulator.SpreadVirus(simu_status)
        # visualize
        draw_simu(simu_status, figure, fig1, fig2, count_pop, frames, max_frames)


def simulate(simu_status):
    print("In")

    # init
    _simulator.InitSimulation(simu_status)

    # print result on screen
    if simu_status.mode == 1:
        run(simu_status)

    # save result in Sim.gif
    elif simu_status.mode == 2:
        run_and_build_animation(simu_status)

    simu_status.print_status
