"""Simple FastAPI application with hello-world endpoint."""

from fastapi import FastAPI

app = FastAPI(
    title="Hello World API",
    description="A simple FastAPI application",
    version="1.0.0"
)


@app.get("/hello-world")
async def hello_world() -> dict:
    """Return a hello world greeting."""
    return {"message": "Hello, World!"}


@app.get("/")
async def root() -> dict:
    """Root endpoint with API info."""
    return {
        "name": "Hello World API",
        "version": "1.0.0",
        "endpoints": ["/hello-world"]
    }
