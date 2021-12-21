import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation
import numpy as np

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


def draw_current_simu_status(simu_status, figure, fig1, fig2, count_population, frames):

    # clean figure
    fig1.clear()
    fig2.clear()

    health = np.array(simu_status.draw_health)
    infected = np.array(simu_status.draw_infected)
    recovered = np.array(simu_status.draw_recovered)
    dead = np.array(simu_status.draw_dead)

    # set figure 1
    fig1.set_xlim(simu_status.lx_bound - 0.1, simu_status.rx_bound + 0.1)
    fig1.set_ylim(simu_status.dy_bound - 0.1, simu_status.uy_bound + 0.1)
    fig1.set_xlabel("X")
    fig1.set_ylabel("Y")

    try:
        # health: green
        fig1.scatter(health[:, 0], health[:, 1], s = 10.0, color = "green", label = 'health')
    except:
        pass
    if simu_status.policy == 0 or simu_status.policy == 3 or simu_status.policy == 4:
        try:
            # infected: red
            fig1.scatter(infected[:, 0], infected[:, 1], s = 10.0, color = "red", label = 'infected')
        except:
            pass
    elif simu_status.policy == 1:
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
    elif simu_status.policy == 2:
        fig1.axvline(x = 0.5, ymin = 0, ymax = simu_status.total_num_people, linewidth = 3.0, color = 'pink', label = 'quarantine bound')
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
    fig1.text(simu_status.lx_bound, simu_status.uy_bound + 0.13, 'simu_time: %i, total: %i, healthy: %i, infected: %i, recovered: %i, dead: %i' %(frames+1, simu_status.total_num_people, simu_status.num_health, simu_status.num_infected, simu_status.num_recovered, simu_status.num_dead), fontsize = 8)


    # set figure 2
    fig2.set_title('infection statistics')
    #fig2.set_xlim(0, simu_status.simu_step)
    fig2.set_xlim(0, frames + 1)
    fig2.set_ylim(0, simu_status.total_num_people + 100)
    fig2.set_xlabel("Time step")
    fig2.set_ylabel("Total people")

    # draw line
    fig2.fill_between(count_population.frames, count_population.infected, simu_status.dy_bound, color = 'lightcoral', label = 'infected people')
    if simu_status.policy == 1:
        fig2.axhline(y = simu_status.healthcare_capacity, xmin = 0, xmax = frames, color = 'pink')
        fig2.fill_between(count_population.frames, count_population.infected, simu_status.healthcare_capacity, color = 'lightcoral', label = 'infected people')
        fig2.fill_between(count_population.frames, simu_status.healthcare_capacity, simu_status.dy_bound, color = 'lightpink', label = 'healthcare people')

    fig2.plot(count_population.frames, count_population.dead, color = 'black')
    fig2.plot(count_population.frames, count_population.recovered, color = 'blue')
    fig2.plot(count_population.frames, count_population.infected, color = 'red')
    fig2.fill_between(count_population.frames, count_population.dead, simu_status.total_num_people, color = 'dimgray', label = 'dead people')
    fig2.fill_between(count_population.frames, count_population.recovered, count_population.dead, color = 'aquamarine', label = 'recovered people')
    fig2.fill_between(count_population.frames, count_population.recovered, count_population.infected, color = 'lightgreen', label = 'health people')


    # Place a legend in this subplot
    fig2.legend(loc = 'best')

    # modify format
    #figure.tight_layout()
    #plt.savefig('foo.png')


def print_in_terminal(frames, simu_status):
    print(f'\riter: {frames+1}, health: {simu_status.num_health}, infected: {simu_status.num_infected}')
    print(f'\r       recovered: {simu_status.num_recovered}, dead: {simu_status.num_dead}')


def update_ani(frames, simu_status, figure, fig1, fig2, count_population):
    _simulator.RunStep(simu_status)

    count_population.update(simu_status.total_num_people, simu_status.num_infected, simu_status.num_recovered, simu_status.num_dead, frames)

    draw_current_simu_status(simu_status, figure, fig1, fig2, count_population, frames)
    if simu_status.dirty:
        print_in_terminal(frames, simu_status)


def run_and_build_animation(simu_status):
    count_population = population()
    figure, spec, fig1, fig2 = build_figure(simu_status.lx_bound, simu_status.rx_bound, simu_status.dy_bound, simu_status.uy_bound, simu_status.simu_step, simu_status.total_num_people)
    print_in_terminal(0, simu_status)
    ani = FuncAnimation(figure, update_ani, fargs = (simu_status, figure, fig1, fig2, count_population), frames = simu_status.simu_step, interval = 10)

    ani.save('Sim_m%i_p%i.gif' %(simu_status.mode, simu_status.policy), writer='pillow', fps=1/0.04)
    plt.savefig('mode%ipolicy%i.png' %(simu_status.mode, simu_status.policy))
