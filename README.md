# GBM Simulation

A lightweight Python library for simulating **geometric Brownian motion (GBM)** paths and managing parameterized simulation experiments.

This project was created as a learning exercise in **object-oriented Python design, API development, packaging, and automated testing**. The library demonstrates how to structure a small simulation framework that separates model definitions, simulation configuration, and simulation results.

---

## Features

- Geometric Brownian Motion model implementation
- Immutable time-series container (`Path`)
- Parameter configuration objects (`ParameterSet`)
- Hashable parameter sets suitable for caching simulations
- Simple Monte Carlo path generation
- Basic automated test suite using `pytest`

---

## Installation

Clone the repository and install the package in editable mode:

```bash
git clone https://github.com/<your-username>/gbm_simulation.git
cd gbm_simulation
pip install -e .
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Quick Example

```python
from gbm_simulation import ParameterSet

# Define simulation parameters
params = ParameterSet(mu=0.1, sigma=0.2, T=1.0, steps=100)

# Run simulation
path = params.simulation()

print(len(path))
print(path[0])
```

Example output:

```
101
(0.0, 1.0)
```

# For a complete runnable example see:
examples/basic_simulation.py

# Run it with:
python examples/basic_simulation.py

---

## Project Structure

```
gbm_simulation/
│
├─ gbm_simulation/
│   ├─ __init__.py
│   ├─ gbm.py
│   ├─ path.py
│   └─ parameters.py
│
├─ tests/
│   ├─ test_gbm.py
│   ├─ test_path.py
│   └─ test_parameters.py
│
├─ requirements.txt
├─ pyproject.toml
└─ README.md
```

---

## Core Components

### GBM

Implements a geometric Brownian motion model with:

- drift parameter `mu`
- volatility parameter `sigma`
- Monte Carlo path generation

---

### Path

Immutable container representing a simulated time series.

Features:

- indexing
- slicing
- length queries
- representation suitable for debugging

---

### ParameterSet

Configuration object representing a full simulation setup:

```
(mu, sigma, T, steps)
```

Parameter sets are:

- immutable
- comparable
- hashable

This allows them to be used as keys in dictionaries for **simulation caching or experiment tracking**.

---

## Running Tests

Execute the test suite with:

```bash
pytest
```

The tests verify the behavior of:

- `GBM`
- `Path`
- `ParameterSet`

---

## Dependencies

- numpy

---

## Purpose of the Project

This repository demonstrates:

- Python package structure
- API design for internal libraries
- object-oriented modeling
- dependency management
- automated testing with `pytest`

The project is intentionally small and focuses on **clear structure and reproducibility** rather than
