import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation
import numpy as np

import my_simulation
import _simulator


def build_figure(lx_bound, rx_bound, dy_bound, uy_bound, simulation_steps, total_num_people):
    # set figure
    figure = plt.figure(figsize = (7, 9))
    spec = figure.add_gridspec(ncols=1, nrows=2, height_ratios=[5,2])

    fig1 = figure.add_subplot(spec[0,0])
    #fig1.set_title('infection simulation')
    fig1.set_xlim(lx_bound - 0.1, rx_bound + 0.1)
    fig1.set_ylim(dy_bound - 0.1, uy_bound + 0.1)

    fig2 = figure.add_subplot(spec[1,0])
    fig2.set_title('infection statistics')
    fig2.set_xlim(0, simulation_steps)
    fig2.set_ylim(0, total_num_people + 100)

    return figure, spec, fig1, fig2

def classify_people(simu_status):
    # init class
    health = []
    infected = []
    recovered = []
    dead = []
    for i in range(simu_status.total_num_people):
        # health
        if simu_status.g_person_status[i].status == 0:
            health.append([simu_status.g_person_status[i].coord_x, simu_status.g_person_status[i].coord_y])
        # infected
        elif simu_status.g_person_status[i].status == 1:
            infected.append([simu_status.g_person_status[i].coord_x, simu_status.g_person_status[i].coord_y])
        # recovered
        elif simu_status.g_person_status[i].status == 2:
            recovered.append([simu_status.g_person_status[i].coord_x, simu_status.g_person_status[i].coord_y])
        # dead
        else:
            dead.append([simu_status.g_person_status[i].coord_x, simu_status.g_person_status[i].coord_y])

    return health, infected, recovered, dead

def draw_simu(simu_status, figure, fig1, fig2, count_population, frames, simulation_steps):

    # clean figure
    fig1.clear()
    fig2.clear()

    health = np.array(simu_status.draw_health)
    infected = np.array(simu_status.draw_infected)
    recovered = np.array(simu_status.draw_recovered)
    dead = np.array(simu_status.draw_dead)

    # set figure 1
    #fig1.set_title('infection simulation')
    fig1.set_xlim(simu_status.lx_bound - 0.1, simu_status.rx_bound + 0.1)
    fig1.set_ylim(simu_status.dy_bound - 0.1, simu_status.uy_bound + 0.1)
    fig1.set_xlabel("X")
    fig1.set_ylabel("Y")

    try:
        # health: green
        fig1.scatter(health[:, 0], health[:, 1], s = 10.0, color = "green", label = 'health')
    except:
        pass
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
    fig1.text(simu_status.lx_bound, simu_status.uy_bound + 0.13, 'simu_time: %i, total: %i, healthy: %i, infected: %i, recovered: %i, dead: %i' %(frames, simu_status.total_num_people, simu_status.num_health, simu_status.num_infected, simu_status.num_recovered, simu_status.num_dead), fontsize = 10)


    # set figure 2
    fig2.set_title('infection statistics')
    fig2.set_xlim(0, simulation_steps)
    fig2.set_ylim(0, simu_status.total_num_people + 100)
    fig2.set_xlabel("Time step")
    fig2.set_ylabel("Total people")

    # draw line
    fig2.plot(count_population.frames, count_population.health, color = 'green')
    fig2.plot(count_population.frames, count_population.infected, color = 'red')
    fig2.fill_between(count_population.frames, count_population.health, count_population.infected, color = 'lightgreen', label = 'health people')
    fig2.fill_between(count_population.frames, count_population.infected, 0, color = 'lightcoral', label = 'infected people')

    # Place a legend in this subplot
    fig2.legend(loc = 'upper right')

    # modify format
    figure.tight_layout()
    plt.draw()
    plt.pause(0.0001)
    if simu_status.dirty:
        print_in_terminal(frames, simu_status)

    if (frames + 1) == simulation_steps:
        plt.savefig('foo.png')


def draw_current_simu_status(simu_status, figure, fig1, fig2, count_population, frames):

    count_population.health.append(simu_status.num_health)
    count_population.infected.append(simu_status.num_infected)
    count_population.recovered.append(simu_status.num_recovered)
    count_population.dead.append(simu_status.num_dead)
    count_population.frames.append(frames)


    # clean figure
    fig1.clear()
    fig2.clear()

    health = np.array(simu_status.draw_health)
    infected = np.array(simu_status.draw_infected)
    recovered = np.array(simu_status.draw_recovered)
    dead = np.array(simu_status.draw_dead)

    # set figure 1
    #fig1.set_title('infection simulation')
    fig1.set_xlim(simu_status.lx_bound - 0.1, simu_status.rx_bound + 0.1)
    fig1.set_ylim(simu_status.dy_bound - 0.1, simu_status.uy_bound + 0.1)
    fig1.set_xlabel("X")
    fig1.set_ylabel("Y")

    try:
        # health: green
        fig1.scatter(health[:, 0], health[:, 1], s = 10.0, color = "green", label = 'health')
    except:
        pass
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
    fig1.text(simu_status.lx_bound, simu_status.uy_bound + 0.13, 'simu_time: %i, total: %i, healthy: %i, infected: %i, recovered: %i, dead: %i' %(frames, simu_status.total_num_people, simu_status.num_health, simu_status.num_infected, simu_status.num_recovered, simu_status.num_dead), fontsize = 10)


    # set figure 2
    fig2.set_title('infection statistics')
    fig2.set_xlim(0, simu_status.simu_step)
    fig2.set_ylim(0, simu_status.total_num_people + 100)
    fig2.set_xlabel("Time step")
    fig2.set_ylabel("Total people")

    # draw line
    fig2.plot(count_population.frames, count_population.health, color = 'green')
    fig2.plot(count_population.frames, count_population.infected, color = 'red')
    fig2.fill_between(count_population.frames, count_population.health, count_population.infected, color = 'lightgreen', label = 'health people')
    fig2.fill_between(count_population.frames, count_population.infected, 0, color = 'lightcoral', label = 'infected people')

    # Place a legend in this subplot
    fig2.legend(loc = 'upper right')

    # modify format
    figure.tight_layout()
    #plt.savefig('foo.png')


def print_in_terminal(frames, simu_status):
    print(f'\riter: {frames}, health: {simu_status.num_health}, infected: {simu_status.num_infected}')
    print(f'\r       recovered: {simu_status.num_recovered}, dead: {simu_status.num_dead}')


def update_ani(frames, simu_status, figure, fig1, fig2, count_population):
    _simulator.Move(simu_status)
    _simulator.SpreadVirus(simu_status)
    if frames % 24 == 23:
        _simulator.RecoveredOrDead(simu_status)

    _simulator.ClassifyPeople(simu_status)
    draw_current_simu_status(simu_status, figure, fig1, fig2, count_population, frames)
    print_in_terminal(frames, simu_status)
    #if simu_status.dirty:
    #    print_in_terminal(frames, simu_status)


def run_and_build_animation(simu_status):
    count_population = population()
    figure, spec, fig1, fig2 = build_figure(simu_status.lx_bound, simu_status.rx_bound, simu_status.dy_bound, simu_status.uy_bound, simu_status.simu_step, simu_status.total_num_people)
    print_in_terminal(0, simu_status)
    ani = FuncAnimation(figure, update_ani, fargs = (simu_status, figure, fig1, fig2, count_population), frames = simu_status.simu_step, interval = 10)
    plt.show()

    ani.save('Sim.gif', writer='pillow', fps=1/0.04)


class population():
    def __init__(self):
        self.health = []
        self.infected = []
        self.recovered = []
        self.dead = []
        self.frames = []

