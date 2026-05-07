from pathlib import Path
import math

import pandas as pd


class Walter:
    def __init__(self):
        pass

    def get_data(self):
        df = pd.read_csv(_CSV_PATH)
        # 인덱스 1번 행만 반환 (DataFrame 형태 유지)
        return df.iloc[[1]].astype(object).where(df.iloc[[1]].notna(), None)

    def get_data(self, limit: int = 10):
        csv_path = Path(__file__).resolve().parent / "Titanic-Dataset.csv"
        df = pd.read_csv(csv_path)
        rows = df.head(limit).to_dict(orient="records")

        # JSON 직렬화 호환을 위해 NaN(float)을 None으로 치환
        for row in rows:
            for k, v in row.items():
                if isinstance(v, float) and math.isnan(v):
                    row[k] = None

        return rows