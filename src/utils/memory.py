import random
from src.utils.misc import Transition


class ReplayMemory(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0

    def push(self, *args):
        """Saves a transition."""
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = Transition(*args)
        self.position = int((self.position + 1) % self.capacity)

    def sample(self, batch_size):
        transitions = random.sample(self.memory, batch_size)
        return transitions

    def sample_zipped(self, batch_size):
        transitions = self.sample(batch_size)
        return Transition(*zip(*transitions))

    def __len__(self):
        return len(self.memory)

