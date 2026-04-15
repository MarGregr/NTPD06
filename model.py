from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score


def train_model():
    # dane
    data = load_wine()
    X = data.data
    y = data.target

    # podział
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # model
    model = RandomForestClassifier(
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test


def train_and_predict():
    model, X_test, y_test = train_model()

    preds = model.predict(X_test)

    return preds, y_test


def get_metrics():
    preds, y_test = train_and_predict()

    acc = accuracy_score(y_test, preds)
    precision = precision_score(y_test, preds, average="macro")
    recall = recall_score(y_test, preds, average="macro")

    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall
    }