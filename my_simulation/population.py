"""
Count the number of people in each state at every time step for draw the statistics graph.
"""
class population():
    def __init__(self):
        self.infected = []
        self.recovered = []
        self.dead = []
        self.frames = []

    def update(self, total, infected, recovered, dead, frames):
        self.infected.append(infected)
        self.recovered.append(total - dead - recovered)
        self.dead.append(total - dead)
        self.frames.append(frames)
