from my_simulation.population import population
import _simulator
from typing import Callable
import matplotlib.pyplot as plt
import time


def run(simulation_state: _simulator.SimulationState, figure: plt.figure, fig1: plt.figure, fig2: plt.figure, on_each_iter_updated: Callable, save_result: Callable) -> None:
    """
    run the simulator and save the result.

    _simulator.RunStep:
        1. Check policy
        2. Everyone move one step
        3. Spread the virus: If someone is infected, update his/her state.
        4. Recovered or dead: Check whether the infected person has recovered or died.
        5. Classify people: For visualize.
    """
    frames = 0
    max_frames = simulation_state.simulation_step

    # for statistics graph
    count_pop = population()

    run_step_time = 0
    pop_update_time = 0
    visualize_time = 0

    while frames < max_frames:
        if simulation_state.num_infected == 0:
            break
        frames += 1

        s = time.time()
        # run one time step in c++ environment.
        _simulator.RunStep(simulation_state)
        e = time.time()
        run_step_time += e - s

        s = time.time()
        count_pop.update(simulation_state.total_num_people, simulation_state.num_infected, simulation_state.num_recovered, simulation_state.num_dead, frames)
        e = time.time()
        pop_update_time += e - s

        s = time.time()
        on_each_iter_updated(simulation_state, figure, fig1, fig2, count_pop, frames)
        e = time.time()
        visualize_time += e - s

    s = time.time()
    save_result(simulation_state, figure, fig1, fig2, count_pop, frames)
    e = time.time()
    visualize_time += e - s

    print(f'=== Run step time: {run_step_time} ===')
    print(f'=== Pop update time: {pop_update_time} ===')
    print(f'=== visualize time: {visualize_time} ===')
