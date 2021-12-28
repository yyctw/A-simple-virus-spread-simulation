import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation
import numpy as np
import os
import time

import my_simulation
import _simulator
from my_simulation.population import population

# python rich for debug
from rich.traceback import install
install(show_locals=True)


def build_figure(lx_bound, rx_bound, dy_bound, uy_bound, simulation_steps, total_num_people):
    # set figure
    figure = plt.figure(figsize = (7, 9))
    spec = figure.add_gridspec(ncols=1, nrows=2, height_ratios=[5,2])

    fig1 = figure.add_subplot(spec[0,0])
    fig1.set_xlim(lx_bound - 0.1, rx_bound + 0.1)
    fig1.set_ylim(dy_bound - 0.1, uy_bound + 0.1)

    fig2 = figure.add_subplot(spec[1,0])
    fig2.set_title('infection statistics')
    fig2.set_xlim(0, simulation_steps)
    fig2.set_ylim(0, total_num_people + 100)

    return figure, spec, fig1, fig2


def draw_current_simulation_state(simulation_state, figure, fig1, fig2, count_population, frames):

    # clean figure
    fig1.clear()
    fig2.clear()

    health = np.array(simulation_state.draw_health)
    infected = np.array(simulation_state.draw_infected)
    recovered = np.array(simulation_state.draw_recovered)
    dead = np.array(simulation_state.draw_dead)

    # set figure 1
    fig1.set_xlim(simulation_state.lx_bound - 0.1, simulation_state.rx_bound + 0.1)
    fig1.set_ylim(simulation_state.dy_bound - 0.1, simulation_state.uy_bound + 0.1)
    fig1.set_xlabel("X")
    fig1.set_ylabel("Y")

    try:
        # health: green
        fig1.scatter(health[:, 0], health[:, 1], s = 10.0, color = "green", label = 'health')
    except:
        pass
    if simulation_state.policy == 0 or simulation_state.policy == 3 or simulation_state.policy == 4:
        try:
            # infected: red
            fig1.scatter(infected[:, 0], infected[:, 1], s = 10.0, color = "red", label = 'infected')
        except:
            pass
    elif simulation_state.policy == 1:
        try:
            # healthcare: pink
            fig1.scatter(infected[0:101, 0], infected[0:101, 1], s = 10.0, color = "pink", label = 'healthcare')
        except:
            try:
                fig1.scatter(infected[:, 0], infected[:, 1], s = 10.0, color = "pink", label = 'healthcare')
            except:
                pass
        try:
            # infected: red
            fig1.scatter(infected[101:, 0], infected[101:, 1], s = 10.0, color = "red", label = 'infected')
        except:
            pass
    elif simulation_state.policy == 2:
        fig1.axvline(x = 0.5, ymin = 0, ymax = simulation_state.total_num_people, linewidth = 3.0, color = 'pink', label = 'quarantine bound')
        try:
            # infected: red
            fig1.scatter(infected[:, 0], infected[:, 1], s = 10.0, color = "red", label = 'infected')
        except:
            pass
    try:
        # recovered: blue
        fig1.scatter(recovered[:, 0], recovered[:, 1], s = 10.0, color = "blue", label = 'recovered')
    except:
        pass
    try:
        # dead: black
        fig1.scatter(dead[:, 0], dead[:, 1], s = 10.0, color = "black", label = 'dead')
    except:
        pass


    fig1.legend(loc = 'upper right')
    # add text descriptors
    fig1.text(simulation_state.lx_bound, simulation_state.uy_bound + 0.13, 'simu_time: %i, total: %i, healthy: %i, infected: %i, recovered: %i, dead: %i' %(frames+1, simulation_state.total_num_people, simulation_state.num_health, simulation_state.num_infected, simulation_state.num_recovered, simulation_state.num_dead), fontsize = 8)


    # set figure 2
    fig2.set_title('infection statistics')
    #fig2.set_xlim(0, simulation_state.simulation_step)
    fig2.set_xlim(0, frames + 1)
    fig2.set_ylim(0, simulation_state.total_num_people + 100)
    fig2.set_xlabel("Time step")
    fig2.set_ylabel("Total people")

    # draw line
    fig2.fill_between(count_population.frames, count_population.infected, simulation_state.dy_bound, color = 'lightcoral', label = 'infected people')
    if simulation_state.policy == 1:
        fig2.axhline(y = simulation_state.healthcare_capacity, xmin = 0, xmax = frames, color = 'pink')
        fig2.fill_between(count_population.frames, count_population.infected, simulation_state.healthcare_capacity, color = 'lightcoral', label = 'infected people')
        fig2.fill_between(count_population.frames, simulation_state.healthcare_capacity, simulation_state.dy_bound, color = 'lightpink', label = 'healthcare people')

    fig2.plot(count_population.frames, count_population.dead, color = 'black')
    fig2.plot(count_population.frames, count_population.recovered, color = 'blue')
    fig2.plot(count_population.frames, count_population.infected, color = 'red')
    fig2.fill_between(count_population.frames, count_population.dead, simulation_state.total_num_people, color = 'dimgray', label = 'dead people')
    fig2.fill_between(count_population.frames, count_population.recovered, count_population.dead, color = 'aquamarine', label = 'recovered people')
    fig2.fill_between(count_population.frames, count_population.recovered, count_population.infected, color = 'lightgreen', label = 'health people')


    # Place a legend in this subplot
    fig2.legend(loc = 'best')


def print_in_terminal(frames, simulation_state):
    print(f'\riter: {frames+1}, health: {simulation_state.num_health}, infected: {simulation_state.num_infected}')
    print(f'\r       recovered: {simulation_state.num_recovered}, dead: {simulation_state.num_dead}')


def update_ani(frames, simulation_state, figure, fig1, fig2, count_population):
    _simulator.RunStep(simulation_state)

    count_population.update(simulation_state.total_num_people, simulation_state.num_infected, simulation_state.num_recovered, simulation_state.num_dead, frames)

    draw_current_simulation_state(simulation_state, figure, fig1, fig2, count_population, frames)
    if simulation_state.dirty:
        print_in_terminal(frames, simulation_state)


def run_and_build_animation(simulation_state: _simulator.SimulationState, figure, fig1, fig2) -> None:
    """
    Use the function FuncAnimation() provided by matplotlib for save the result into .gif graph.
    """

    count_population = population()
    print_in_terminal(0, simulation_state)
    ani = FuncAnimation(figure, update_ani, fargs = (simulation_state, figure, fig1, fig2, count_population), frames = simulation_state.simulation_step, interval = 10)

    dirname = './output_images'
    os.makedirs(dirname, exist_ok = True)
    ani.save(f'{dirname}/Simulation_policy{simulation_state.policy}.gif', writer='pillow', fps=1/0.04)
    plt.savefig(f'{dirname}/Simulation_policy%i.png')
