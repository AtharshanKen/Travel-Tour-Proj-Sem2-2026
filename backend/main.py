from fastapi import FastAPI
from pydantic import BaseModel
from Cal import Cal

app = FastAPI()

class Input(BaseModel):
    op:str
    x:int
    y:int

@app.post("/Cal")
async def operate(input:Input):
    print(input)
    print(type(input))
    result = Cal(input.op, input.x, input.y)
    return result
