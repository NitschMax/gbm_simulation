from .gbm import GBM

class SimulationConfig:
    def __init__(self, mu, sigma, T, steps):
        self.__params = (float(mu), float(sigma), float(T), int(steps))

    @property
    def params(self):
        return self.__params

    def __eq__(self, other):
        if isinstance(other, SimulationConfig):
            return self.params == other.params
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.params)

    def simulation(self):
        gbm = GBM(*self.params[:2])
        return gbm.sample_path(*self.params[2:])
