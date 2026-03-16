import numpy as np
import numpy.random as npr
from .path import Path


class GBM:
    def __init__(self, mu=0, sigma=1):
        self.__mu = float(mu)
        self.__sigma = float(sigma)

    @property
    def mu(self):
        return self.__mu

    @property
    def sigma(self):
        return self.__sigma

    def __eq__(self, other):
        if isinstance(other, GBM):
            return (self.mu, self.sigma) == (other.mu, other.sigma)
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.mu, self.sigma))

    def sample_path(self, T, steps, S0=1, seed=None):
        if seed is not None:
            npr.seed(seed)
        dt = T / steps
        times = np.linspace(0, T, steps + 1)
        dW = npr.normal(0, np.sqrt(dt), size=steps)
        W = np.cumsum(dW)
        W = np.insert(W, 0, 0)  # Insert W(0) = 0 at the beginning
        S = S0 * np.exp((self.mu - 0.5 * self.sigma ** 2) * times + self.sigma * W)
        return Path(times, S)
