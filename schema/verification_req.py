from pydantic import BaseModel

class PanVerificationReq(BaseModel):
    pan: str
    dob: str