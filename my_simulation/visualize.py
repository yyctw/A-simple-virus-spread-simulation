import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

import my_simulation
import _simulator


def build_figuer(lx_bound, rx_bound, dy_bound, uy_bound, simulation_steps, total_num_people):
    # set figure
    figure = plt.figure(figsize = (5,7))
    spec = figure.add_gridspec(ncols=1, nrows=2, height_ratios=[5,2])

    fig1 = figure.add_subplot(spec[0,0])
    fig1.set_title('infection simulation')
    fig1.set_xlim(lx_bound - 0.1, rx_bound + 0.1)
    fig1.set_ylim(dy_bound - 0.1, uy_bound + 0.1)

    fig2 = figure.add_subplot(spec[1,0])
    fig2.set_title('infection statistics')
    fig2.set_xlim(0, simulation_steps)
    fig2.set_ylim(0, total_num_people + 100)

    return figure, spec, fig1, fig2

def classify_people(simu_status):
    # init class
    health = np.zeros((1,2))
    infected = np.zeros((1,2))
    recovered = np.zeros((1,2))
    dead = np.zeros((1,2))
    for i in range(simu_status.total_num_people):
        # health
        if simu_status.g_person_status[i].status == 0:
            health = np.append(health, [[simu_status.g_person_status[i].coord_x, simu_status.g_person_status[i].coord_y]], axis = 0)
        # infected
        elif simu_status.g_person_status[i].status == 1:
            infected = np.append(infected, [[simu_status.g_person_status[i].coord_x, simu_status.g_person_status[i].coord_y]], axis = 0)
        # recovered
        elif simu_status.g_person_status[i].status == 2:
            recovered = np.append(recovered, [[simu_status.g_person_status[i].coord_x, simu_status.g_person_status[i].coord_y]], axis = 0)
        # dead
        elif simu_status.g_person_status[i].status == -1:
            dead = np.append(dead, [[simu_status.g_person_status[i].coord_x, simu_status.g_person_status[i].coord_y]], axis = 0)

    return health, infected, recovered, dead

def draw_current_simu_status(simu_status, figure, fig1, fig2):

    # classify health, infected, recovered and dead people
    health, infected, recovered, dead = classify_people(simu_status)

    # clean figure
    fig1.clear()
    fig2.clear()

    # set figure 1
    fig1.set_title('infection simulation')
    fig1.set_xlim(simu_status.lx_bound - 0.1, simu_status.rx_bound + 0.1)
    fig1.set_ylim(simu_status.dy_bound - 0.1, simu_status.uy_bound + 0.1)
    fig1.set_xlabel("X")
    fig1.set_ylabel("Y")

    # health: green
    fig1.scatter(health[:, 0], health[:, 1], s = 10.0, color = "green")
    # infected: red
    fig1.scatter(infected[:, 0], infected[:, 1], s = 10.0, color = "red")
    # recovered: blue
    fig1.scatter(recovered[:, 0], recovered[:, 1], s = 10.0, color = "blue")
    # dead: black
    fig1.scatter(dead[:, 0], dead[:, 1], s = 10.0, color = "black")

    # set figure 2
    fig2.set_title('infection statistics')
    fig2.set_xlim(0, 1000)
    fig2.set_ylim(0, simu_status.total_num_people + 100)
    fig2.set_xlabel("Time step")
    fig2.set_ylabel("Total people")

    # modify format
    figure.tight_layout()
    plt.savefig('foo.png')



def update(simu_status):

    pass

def visualize(simu_status):
    simulation_steps = 10000
    # set figure
    fig = plt.figure(figsize = (5,7))
    spec = fig.add_gridspec(ncols=1, nrows=2, height_ratios=[5,2])

    ax1 = fig.add_subplot(spec[0,0])
    plt.title('infection simulation')
    plt.xlim(simu_status.lx_bound - 0.1, simu_status.rx_bound + 0.1)
    plt.ylim(simu_status.dy_bound - 0.1, simu_status.uy_bound + 0.1)

    ax2 = fig.add_subplot(spec[1,0])
    ax2.set_title('number of infected')
    ax2.set_xlim(0, simulation_steps)
    ax2.set_ylim(0, simu_status.total_num_people + 100)

    infected_plot = []
    fatalities_plot = []
    animation = FuncAnimation(fig, update, fargs = (simu_status,), frames = simulation_steps, interval = 33)

    plt.show()

