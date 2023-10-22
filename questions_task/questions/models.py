from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from questions_task.models import Base


class Question(Base):
    __tablename__ = "question"

    question_id: Mapped[int]
    question: Mapped[str]
    answer: Mapped[str]
    inserted_at: Mapped[datetime] = mapped_column(default=func.now())
