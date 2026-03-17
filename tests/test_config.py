from gbm_simulation import SimulationConfig

def test_config_equality():
    p = SimulationConfig(0.1, 0.2, 1, 100)
    p2 = SimulationConfig(0.1, 0.2, 1, 100)
    p3 = SimulationConfig(0.1, 0.2, 1, 101)
    assert p == p2
    assert p != p3

def test_config_hash():
    p = SimulationConfig(0.1, 0.2, 1, 100)
    p2 = SimulationConfig(0.1, 0.2, 1, 100)
    p3 = SimulationConfig(0.1, 0.2, 1, 101)
    assert hash(p) == hash(p2)
    assert hash(p) != hash(p3)

def test_simulation_returns_path():
    p = SimulationConfig(0.1, 0.2, 1, 100)
    result = p.simulation()

    from gbm_simulation import Path
    assert isinstance(result, Path)
    assert len(result) == 101  # 100 steps + initial point
    assert result[0] == (0, 1)  # Initial time and price
