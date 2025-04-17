from typing import Any, Type, Optional

import logging

from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
from langchain_core.retrievers import BaseRetriever

from src.ai_agent.utils import format_documents


logger = logging.getLogger(__name__)


class PriceListToolInput(BaseModel):
    query: str = Field(..., description="Запрос пользователя")


class PriceListTool(BaseTool):
    name: str = "PriceListTool"
    description: str = "Ищет информацию для ответа на вопрос клиента по прайс-листу 1С"
    args_schema: Optional[Type[BaseModel]] = PriceListToolInput

    def __init__(self, retriever: BaseRetriever, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._retriever = retriever

    def _run(self, query: str) -> str:
        logger.info("---RETRIEVE FROM PRICE-LIST---")
        documents = self._retriever.invoke(query)
        return format_documents(documents)

    async def _arun(self, query: str) -> str:
        logger.info("---RETRIEVE FROM PRICE-LIST---")
        documents = await self._retriever.ainvoke(query)
        return format_documents(documents)
