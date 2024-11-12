from pydantic import BaseModel


class Output(BaseModel):
    status: int
    details: dict