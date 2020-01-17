from pydantic import BaseModel, Field


class OutputExample(BaseModel):
    a: int = Field(..., title="Input value a")
    b: int = Field(..., title="Input value b")
    result: int = Field(..., title="Result of a * b")
