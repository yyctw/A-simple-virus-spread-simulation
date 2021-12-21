from my_simulation.visualize import build_figure
from my_simulation.visualize import draw_current_simu_status
from my_simulation.visualize import run_and_build_animation
from my_simulation.visualize import population
from my_simulation.visualize import print_in_terminal
from my_simulation.population import population
import matplotlib.pyplot as plt
import _simulator
import numpy as np
import sys
import os


def run(simu_status):
    if simu_status.mode == 2:
        run_and_build_animation(simu_status)
    else:
        frames = 0
        max_frames = simu_status.simu_step

        # init figure
        figure, spec, fig1, fig2 = build_figure(simu_status.lx_bound, simu_status.rx_bound, simu_status.dy_bound, simu_status.uy_bound, max_frames, simu_status.total_num_people)

        # for statistics graph
        count_pop = population()

        print_in_terminal(frames, simu_status)
        while frames < max_frames:
            if simu_status.num_infected == 0:
                break
            frames += 1
            _simulator.RunStep(simu_status)

            count_pop.update(simu_status.total_num_people, simu_status.num_infected, simu_status.num_recovered, simu_status.num_dead, frames)

            # visualize
            if simu_status.mode == 1:
                draw_current_simu_status(simu_status, figure, fig1, fig2, count_pop, frames)
                plt.draw()
                plt.pause(0.0001)
            if simu_status.dirty == True:
                print_in_terminal(frames, simu_status)
        draw_current_simu_status(simu_status, figure, fig1, fig2, count_pop, frames)
        if not os.path.exists('./image'):
            os.makedirs('./image')
        plt.savefig('./image/Sim_policy%i.png' %simu_status.policy)


def simulate(simu_status):
    print("In")

    # init
    _simulator.InitSimulation(simu_status)

    run(simu_status)

    simu_status.print_status
