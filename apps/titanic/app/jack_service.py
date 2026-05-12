from sklearn.model_selection import train_test_split

from titanic.app.rose_model import RoseModel
from titanic.app.walter_reader import WalterReader


class JackService:
    _FEATURES = ["Pclass", "Sex", "Age", "Fare"]
    _TARGET = "Survived"
    _RANDOM_STATE = 42

    _accuracy: float | None = None
    _model_name: str | None = None

    def __init__(self) -> None:
        self.walter = WalterReader()
        self.rose = RoseModel()

    def get_model_name_and_accuracy(self) -> dict:
        if JackService._accuracy is None:
            df = self.walter.get_full_data()
            df = df[self._FEATURES + [self._TARGET]].copy()
            df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
            df["Age"] = df["Age"].fillna(df["Age"].median())
            df["Fare"] = df["Fare"].fillna(df["Fare"].median())

            X = df[self._FEATURES]
            y = df[self._TARGET]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=self._RANDOM_STATE
            )
            self.rose.model.fit(X_train, y_train)

            JackService._accuracy = float(self.rose.model.score(X_test, y_test))
            JackService._model_name = self.rose.get_model_name()

        return {"model_name": JackService._model_name, "accuracy": JackService._accuracy}