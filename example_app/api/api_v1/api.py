from fastapi import APIRouter

from .endpoints.example import router as example_router


router = APIRouter()
router.include_router(example_router)
