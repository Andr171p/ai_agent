from typing import Any, Type, Optional

import logging

from pydantic import BaseModel, Field

from langchain_core.tools import BaseTool
from langchain_core.retrievers import BaseRetriever

from src.ai_agent.utils import format_documents


logger = logging.getLogger(__name__)


class ConsultationToolInput(BaseModel):
    question: str = Field(..., description="Вопрос пользователя")


class ConsultationTool(BaseTool):
    name: str = "ConsultationTool"
    description: str = "Ищет информацию для консультации пользователя по продуктам 1С"
    args_schema: Optional[Type[BaseModel]] = ConsultationToolInput

    def __init__(self, retriever: BaseRetriever, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._retriever = retriever

    def _run(self, question: str) -> str:
        logger.info("---RETRIEVE FROM 1C---")
        documents = self._retriever.invoke(question)
        return format_documents(documents)

    async def _arun(self, question: str) -> str:
        logger.info("---RETRIEVE FROM 1C---")
        documents = await self._retriever.ainvoke(question)
        return format_documents(documents)
