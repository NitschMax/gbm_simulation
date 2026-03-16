from gbm_simulation import ParameterSet

def test_parameter_equality():
    p = ParameterSet(0.1, 0.2, 1, 100)
    p2 = ParameterSet(0.1, 0.2, 1, 100)
    p3 = ParameterSet(0.1, 0.2, 1, 101)
    assert p == p2
    assert p != p3

def test_parameter_hash():
    p = ParameterSet(0.1, 0.2, 1, 100)
    p2 = ParameterSet(0.1, 0.2, 1, 100)
    p3 = ParameterSet(0.1, 0.2, 1, 101)
    assert hash(p) == hash(p2)
    assert hash(p) != hash(p3)

def test_simulation_returns_path():
    p = ParameterSet(0.1, 0.2, 1, 100)
    result = p.simulation()

    from gbm_simulation import Path
    assert isinstance(result, Path)
    assert len(result) == 101  # 100 steps + initial point
    assert result[0] == (0, 1)  # Initial time and price
