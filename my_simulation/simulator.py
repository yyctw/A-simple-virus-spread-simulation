from my_simulation.population import population
import my_simulation
import _simulator
from typing import Callable
import matplotlib.pyplot as plt


def run(simulation_state: _simulator.SimulationState, figure: plt.figure, fig1: plt.figure,
        fig2: plt.figure, on_each_iter_updated: Callable, save_result: Callable) -> None:
    """
    run the simulator and save the result.

    _simulator.RunStep:
        1. Check policy
        2. Everyone move one step
        3. Spread the virus: If someone is infected, update his/her state.
        4. Recovered or dead: Check whether the infected person has recovered or died.
        5. Classify people: For visualize.
    """
    if simulation_state.mode == 2:
        # Use FuncAnimation to store the result .gif
        my_simulation.run_and_build_animation(
            simulation_state, figure, fig1, fig2)
    else:
        frames = 0
        max_frames = simulation_state.simulation_step

        # for statistics graph
        count_pop = population()

        while frames < max_frames:
            if simulation_state.num_infected == 0:
                break
            frames += 1

            # run one time step in c++ environment.
            _simulator.RunStep(simulation_state)

            count_pop.update(
                simulation_state.total_num_people,
                simulation_state.num_infected,
                simulation_state.num_recovered,
                simulation_state.num_dead,
                frames)

            on_each_iter_updated(
                simulation_state,
                figure,
                fig1,
                fig2,
                count_pop,
                frames)

        save_result(simulation_state, figure, fig1, fig2, count_pop, frames)
