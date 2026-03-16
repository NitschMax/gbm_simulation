from gbm_simulation import Path
import pytest

def test_path_length():
    path = Path([0, 1, 2], [1, 2, 3])
    assert len(path) == 3

def test_path_indexing():
    path = Path([0, 1, 2], [1, 2, 3])
    assert path[1] == (1, 2)

def test_path_slice_returns_path():
    path = Path([0, 1, 2, 3], [1, 2, 3, 4])
    sliced_path = path[1:3]
    assert isinstance(sliced_path, Path)
    assert len(sliced_path) == 2
    assert sliced_path[0] == (1, 2)
    assert sliced_path[1] == (2, 3)

def test_path_length_mismatch():
    with pytest.raises(ValueError):
        Path([0, 1], [1, 2, 3])
