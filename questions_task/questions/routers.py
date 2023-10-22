from typing import Annotated, Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from questions_task.questions.crud import (
    add_question,
    get_questions_from_database,
    quantity,
)
from questions_task.questions.schemas import QuestionQuantity, Questions
from questions_task.questions.utils import get_response
from questions_task.utils import check_db

router = APIRouter(prefix="/question", tags=["questions"])


@router.post(
    "/",
    summary="Get questions",
    response_model=Union[List[Questions], Questions],
)
async def request_question(
    quest_num: int,
    db: Annotated[AsyncSession, Depends(check_db)],
) -> List[Dict[str, str]]:
    response = await get_response(quest_num)
    await add_question(response, db)
    return await get_questions_from_database(quest_num, db)


@router.get(
    "/",
    summary="Quantity questions",
    response_model=QuestionQuantity,
)
async def get_quantity(
    db: Annotated[AsyncSession, Depends(check_db)],
) -> Dict[str, int]:
    return await quantity(db)


@router.get(
    "/{num}",
    summary="Get questions",
    response_model=Union[List[Questions], Questions],
)
async def get_quest(
    num: int,
    db: Annotated[AsyncSession, Depends(check_db)],
) -> List[Dict[str, str]]:
    question_results = await get_questions_from_database(num, db)
    if len(question_results) < num:
        total = await quantity(db)
        raise HTTPException(
            status_code=400,
            detail=f"Only {total.quantity} question available",
        )
    return question_results
