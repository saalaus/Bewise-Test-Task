from typing import AsyncGenerator

from fastapi import HTTPException
from sqlalchemy.exc import OperationalError

from questions_task.database import SessionLocal


async def check_db() -> AsyncGenerator:
    try:
        async with SessionLocal() as session:
            yield session
    except OperationalError as e:
        raise HTTPException(
            status_code=503,
            detail="Server closed the connection unexpectedly",
        ) from e
