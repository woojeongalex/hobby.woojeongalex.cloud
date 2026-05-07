from fastapi import FastAPI
import pandas as pd
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "한국도로공사_교통사고통계_20241231.csv"

app = FastAPI(title="doro(director)")

from .doro_reader import DoroReader

class DoroDirector :
    def __init__(self):
        pass

    def get_data(self):
        df = pd.read_csv(_CSV_PATH, encoding='cp949')
        # 인덱스 1번 행만 반환 (DataFrame 형태 유지)
        return df.iloc[[1]].astype(object).where(df.iloc[[1]].notna(), None)
        
if __name__ == "__main__":
    print("도로 디렉터가 메인이다.")
    w = DoroReader()
    w.get_data()
