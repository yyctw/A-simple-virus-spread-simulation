import os
import matplotlib.pyplot as plt
import time

import config
import my_simulation
import _simulator


def set_simulation_state(config) -> _simulator.SimulationState:
    """
    Put the parameters in config.py to init the simulation state.
    """
    simulation = _simulator.SimulationState(
        config.TOTAL_POPULATION,
        int(config.INFECTED_PEOPLE * config.TOTAL_POPULATION),
        config.MOVE_SPEED,
        config.INFECTED_RATE,
        config.MORTALITY_RATE,
        config.RECOVERY_RATE,
        config.HEALTHCARE_CAPACITY,
        config.LEFT_X,
        config.RIGHT_X,
        config.UP_Y,
        config.DOWN_Y,
        config.SIMULATION_STEP,
        config.MODE,
        config.MOVE_STEP,
        config.SPREAD_RANGE,
        config.POLICY)

    return simulation


def save_result(simulation_state: _simulator.SimulationState, figure: plt.figure, fig1: plt.figure, fig2: plt.figure, count_pop: my_simulation.population, frames: int) -> None:
    """
    After the simulator is finished, save the result image in certain directory.
    """

    # Finished simulator, draw the result figure
    my_simulation.draw_current_simulation_state(simulation_state, figure, fig1, fig2, count_pop, frames)

    # Finished simulator, saved the result figure
    dirname = './output_images'
    os.makedirs(dirname, exist_ok = True)
    plt.savefig(f'{dirname}/Simulation_policy{simulation_state.policy}.png')


def on_each_iter_updated(simulation_state: _simulator.SimulationState, figure: plt.figure, fig1: plt.figure, fig2: plt.figure, count_pop: my_simulation.population, frames: int) -> None:
    """
    In each iteration, the current simulation state is drawn.
    If the simulation state been changed, print current state of population in terminal
    """
    # visualize
    if simulation_state.mode == 1:
        my_simulation.draw_current_simulation_state(simulation_state, figure, fig1, fig2, count_pop, frames)
        plt.draw()
        plt.pause(0.0001)

    if simulation_state.dirty == True:
        my_simulation.print_in_terminal(frames, simulation_state)



def main() -> None:
    """
    The main function running simulator.
    1. init simulation state
    2. init figure for visualization
    3. run simulator
    """
    s = time.time()
    # read all config from config.py file and ste init simulation state
    simulation_state = set_simulation_state(config)

    # init figure for visualization
    figure, _, fig1, fig2 = my_simulation.build_figure(simulation_state.lx_bound, simulation_state.rx_bound, simulation_state.dy_bound, simulation_state.uy_bound, simulation_state.simulation_step, simulation_state.total_num_people)
    e = time.time()
    print(f'=== Initialize time: {e-s} ===')

    # run simulator
    if simulation_state.mode == 2:
        # Store the results in a gif file.
        s = time.time()
        my_simulation.run_and_build_animation(simulation_state, figure, fig1, fig2)
        e = time.time()
        print(f'=== TOTAL TIME: {e-s}')
    else:
        my_simulation.run(simulation_state, figure, fig1, fig2, on_each_iter_updated, save_result)



if __name__ == '__main__':
    main()
