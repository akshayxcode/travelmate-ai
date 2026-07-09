from fastapi import APIRouter

from app.agent.router import TravelRouter
from app.models.request import ChatRequest
from app.models.response import ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    reply = TravelRouter.process(request.message)

    return ChatResponse(response=reply)