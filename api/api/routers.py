from fastapi import APIRouter

from api.types import APIResponse


# TODO: For now we have one generic router, but this
#       will likely get broken up in the future.
demo_router = APIRouter()


# FIXME
@demo_router.get('/demo')
async def demo() -> APIResponse:
    return {'hello': 'world'}
