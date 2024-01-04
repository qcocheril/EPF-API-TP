"""API Router for Fast API."""
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from src.api.routes import hello, data, utils, parameters

router = APIRouter()

@router.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

router.include_router(hello.router, tags=["Hello"])
router.include_router(data.router, prefix="/api")
router.include_router(utils.router, prefix="/api")
router.include_router(parameters.router, prefix="/api")