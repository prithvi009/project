from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

from schema.verification_req import PanVerificationReq

app = FastAPI()



def load_data_pan():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        return []


@app.post("/pan/verify")
def verify_pan(request : PanVerificationReq):
    pan_data = load_data_pan()
    for pan in pan_data:
        data = pan.get("data", {})
        if data.get("pan_number") == request.pan and data.get("dob") == request.dob:
            return {"matchingFlag": True}
    return {"matchingFlag": False}

@app.get("/")
def read_root():
    return {"Hello": "World"}