"""
Basic example demonstrating how to run a GBM simulation
using the gbm_simulation library.
"""

from gbm_simulation import ParameterSet


def main():
    # Define model parameters
    mu = 0.05
    sigma = 0.2
    T = 1.0
    steps = 100

    # Create parameter configuration
    params = ParameterSet(mu, sigma, T, steps)

    # Run simulation
    path = params.simulation()

    print("Number of time points:", len(path))
    print("First observation:", path[0])
    print("Last observation:", path[-1])

    print("\nFirst five points of the simulated path:")

    for i in range(5):
        t, s = path[i]
        print(f"t={t:.3f}, S={s:.4f}")


if __name__ == "__main__":
    main()
