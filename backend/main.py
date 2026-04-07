from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/talk")
async def read_message(request: Request, message: str):
    request_body = request.body()
