from config import config
import my_simulation
import _simulator


def set_config(config):
    simulation = _simulator.SimulationParameter(
        config.total_num_people,
        int(config.infected_people * config.total_num_people),
        config.move_speed,
        config.infect_rate,
        config.mortality_rate,
        config.recovery_rate,
        config.healthcare_capacity,
        config.left_x,
        config.right_x,
        config.up_y,
        config.down_y,
        config.simu_step,
        config.mode,
        config.move_step,
        config.spread_range,
        config.policy)
    return simulation


if __name__ == '__main__':
    # read all config from config.py file
    config = config()
    simulation = set_config(config)
    # doing simulation
    my_simulation.simulate(simulation)
