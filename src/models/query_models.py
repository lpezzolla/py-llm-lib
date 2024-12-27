from pydantic import BaseModel

class QueryPayload(BaseModel):
    prompt: str
    user_id: str

class QueryOutput(BaseModel):
    response: str