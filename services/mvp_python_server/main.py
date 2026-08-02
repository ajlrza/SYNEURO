from fastapi import FastAPI

app = FastAPI(
    debug=False,
)

@app.get("/interact")

def read_data(request: object):
    pass