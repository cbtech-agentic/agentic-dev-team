"""FastAPI application with time endpoint."""

from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Time API",
    description="A simple API that returns the current server time",
    version="1.0.0",
)


class TimeResponse(BaseModel):
    """Response model for the time endpoint."""

    current_time: str
    timezone: str
    unix_timestamp: int


@app.get("/time", response_model=TimeResponse)
async def get_time() -> TimeResponse:
    """Get the current server time.

    Returns:
        TimeResponse: The current time in ISO 8601 format,
        timezone information, and Unix timestamp.
    """
    now = datetime.now(timezone.utc)
    return TimeResponse(
        current_time=now.isoformat(),
        timezone="UTC",
        unix_timestamp=int(now.timestamp()),
    )


@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}
