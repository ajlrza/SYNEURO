from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from . import agent
import json

origins = [
    "https://digital-sanctuary-kappa.vercel.app",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_methods=["*"],             
    allow_headers=["*"],             
)

@app.post("/chat")
async def read_request(request: Request):

    body = await request.json()
    body = body or {}

    dataObject = {
        "UserID": body.get("UserID"),
        "Message": body.get("Message"),
        "Date": body.get("Date"),
        "Time": body.get("Time"),
        "Waifu": body.get("WaifuID"),
        "ConversationID": body.get("ConversationID"),
    }

    api_response = agent.appProxy(dataObject)
    if api_response is False:
        return f"Cannot message {dataObject["Waifu"]} at the moment."
    return api_response.get('Response')

@app.post("/saveMessage")
async def read_request(request: Request):
    
    body = await request.json()

    UserID = body.get("userID")
    Message = body.get("message")
    Date = body.get("messageDate")

    payload = {"userID": UserID, "message": Message, "messageDate": Date}
    with open("python_javascript_bridge.json", "w", encoding="utf-8") as File:
        json.dump(payload, File)

@app.post("/loadMessage")
async def read_request(request: Request):

    body = await request.json()

    UserID = body.get("userID")

    # Return stored data for the given user if available
    try:
        with open("python_javascript_bridge.json", "r", encoding="utf-8") as File:
            data = json.load(File)
    except FileNotFoundError:
        data = {}
    return data

@app.post("/loadConversationHistory")
async def read_request(request: Request):

    body = await request.json()

    UserID = body.get("userID")

    try:
        with open("python_javascript_bridge.json", "r", encoding="utf-8") as File:
            data = json.load(File)
    except FileNotFoundError:
        data = {}
    return data

@app.post("/testChat")
async def read_request(request: Request):

    body = await request.json()

    requestReq = body.get("Test")
    return requestReq
