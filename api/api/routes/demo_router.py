from fastapi import APIRouter

from api.types import APIResponse


# TODO: For now we have one generic router, but this
#       will likely get broken up in the future.
router = APIRouter()


@router.get('/demo')
async def demo() -> APIResponse:
    return {'hello': 'world'}
