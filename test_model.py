import numpy as np
from model import train_and_predict, get_metrics


def test_predictions_not_none():
    preds, _ = train_and_predict()
    assert preds is not None


def test_predictions_length():
    preds, y_test = train_and_predict()

    assert len(preds) > 0
    assert len(preds) == len(y_test)


def test_predictions_value_range():
    preds, _ = train_and_predict()

    for p in preds:
        assert p in [0, 1, 2], "PRedykcja poza spodziewanymi klasami"


def test_model_accuracy():
    metrics = get_metrics()

    assert metrics["accuracy"] >= 0.7, f"Dokładność jest za niska: {metrics['accuracy']}"