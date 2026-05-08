from pathlib import Path
import pickle

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier


_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _DATA_DIR / "titanic_decision_tree.pkl"


class Rose:
    def __init__(self):
        pass

    def save_decision_tree_model(self, model_path: Path | None = None):
        df = pd.read_csv(_CSV_PATH)

        y = df["Survived"]
        X = df.drop(columns=["Survived"])

        numeric_features = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
        categorical_features = ["Sex", "Embarked"]

        numeric_transformer = Pipeline(
            steps=[("imputer", SimpleImputer(strategy="median"))]
        )
        categorical_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]
        )

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
            ]
        )

        model = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("classifier", DecisionTreeClassifier(random_state=42)),
            ]
        )

        model.fit(X, y)

        target_path = Path(model_path) if model_path else _MODEL_PATH
        with open(target_path, "wb") as f:
            pickle.dump(model, f)

        return str(target_path)