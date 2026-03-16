from gbm_simulation import GBM

def test_gbm_parameters():
    model = GBM(0.1, 0.2)

    assert model.mu == 0.1
    assert model.sigma == 0.2

def test_gbm_equality():
    model1 = GBM(0.1, 0.2)
    model2 = GBM(0.1, 0.2)
    model3 = GBM(0.1, 0.3)

    assert model1 == model2
    assert model1 != model3

def test_gbm_hash():
    model1 = GBM(0.1, 0.2)
    model2 = GBM(0.1, 0.2)
    model3 = GBM(0.1, 0.3)

    assert hash(model1) == hash(model2)
    assert hash(model1) != hash(model3)

def test_path_generation():
    model = GBM(0.1, 0.2)
    path = model.sample_path(1.0, 100)

    assert len(path) == 101

