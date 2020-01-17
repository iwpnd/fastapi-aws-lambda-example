from pydantic import BaseModel, Field


class InputExample(BaseModel):
    a: int = Field(..., title="Input value a")
    b: int = Field(..., title="Input value b")
