import httpx
from fastapi import HTTPException


async def get_response(questions_num: int) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://jservice.io/api/random?count={questions_num}",
            )
        return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=503, detail="ConnectionError") from e
