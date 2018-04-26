import numpy as np
from DE import DE
if __name__ == "__main__":
    bound = np.tile([[-600], [600]], 25)
    dea = DE.DifferentialEvolutionAlgorithm(60, 25, bound, 1000, [0.8,  0.6])
    dea.solve()