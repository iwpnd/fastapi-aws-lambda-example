from fastapi import APIRouter

from example_app.core.models.output import OutputExample
from example_app.core.models.input import InputExample

router = APIRouter()

@router.post("/example/", response_model=OutputExample, tags=["example endpoint"])
def example_endpoint(inputs: InputExample):
    """
    Multiply two values

    This will multiply two inputs.

    And this path operation will:
    * return a*b
    """
    return {
        "a": inputs.a,
        "b": inputs.b,
        "result": inputs.a * inputs.b
    }