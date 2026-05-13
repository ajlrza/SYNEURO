from fastapi import FastAPI, Request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import app_main
from "./db_server" import Query

origins = [
    "https://digital-sanctuary-kappa.vercel.app",  # Common for React/Vue
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Or ["*"] for public APIs         # Support cookies and auth headers
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers
)

@app.post("/chatKurisu")
async def read_request(request: Request):

    body = await request.json()
    
    User = body.get("User")
    Message = body.get("Message")

    api_response = app_main.appProxy(User, Message)
    return api_response['Response']

@app.post("/query")
async def read_request(request: Request):
    
    body = await request.json()

    UserID = body.get("userID")
    Message = body.get("message")
    Date = body.get("messageDate")

    db = db_server.


@app.post("/testChat")
async def read_request(request: Request):

    body = await request.json()

    requestReq = body.get("Test")
    return requestReq
