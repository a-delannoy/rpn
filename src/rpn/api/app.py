from fastapi import FastAPI

from rpn.api.endpoints import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="RPN API",
        version="1.0.0",
        description="A simple Reverse Polish Notation calculator API",
    )

    app.include_router(router, prefix="/api", tags=["stacks"])
    return app
