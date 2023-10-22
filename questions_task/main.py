from fastapi import FastAPI

from questions_task.questions.routers import router

app = FastAPI(
    title="Bewise.Quiz",
    description="Service for generate questions",
)

app.include_router(router)
