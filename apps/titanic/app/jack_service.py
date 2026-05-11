from titanic.app.walter_reader import WalterReader
from titanic.app.rose_model import RoseModel

class JackService :
    def __init__(self):
        self.w = WalterReader()
        self.rose = RoseModel()

    def get_training_model_name(self) -> str:
        """연관된 추정기의 클래스명을 반환합니다"""
        return type(self.rose.model).__name__