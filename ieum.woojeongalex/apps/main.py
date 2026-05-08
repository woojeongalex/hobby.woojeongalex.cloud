from fastapi import FastAPI

from titanic.app.james import James
from doro.app.doro_director import DoroDirector

app = FastAPI(title="WooJeongAlex Main Page")

@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지", "docs": "/docs"}


@app.get("/titanic/data")
def read_titanic_data():
    james = James()
    df = james.get_data()
    return df.to_dict(orient="records")

@app.get("/titanic/count")
def read_titanic_count():
    james = James()
    count = james.get_count()
    return {"count": count}

@app.get("/titanic/count/survived")
def read_titanic_survived_count():
    james = James()
    count = james.get_survived_count()
    return {"survived_count": count}

@app.get("/titanic/count/dead")
def read_titanic_dead_count():
    james = James()
    count = james.get_dead_count()
    return {"dead_count": count}

@app.get("/titanic/tree")
def read_titanic_tree():
    james = James()
    tree = james.has_decision_tree_model()

    return {"tree": tree}


@app.get("/doro/data")
def read_doro_data():
    doro_director = DoroDirector()
    df = doro_director.get_data()


    return df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)