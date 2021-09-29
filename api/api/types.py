from typing import Any


# The FastAPI response annotation is variable:
# https://github.com/tiangolo/fastapi/issues/101.
APIResponse = Any

# TODO: add more languages
Language = Literal[
    'English',
    'Spanish',
    'Norwegian',
]
