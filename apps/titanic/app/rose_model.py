from sklearn.tree import DecisionTreeClassifier
class RoseModel:

    def __init__(self) -> None:
        self.model = DecisionTreeClassifier(random_state=42)
       

    def get_model_name(self) -> None:
        return type(self.model).__name__