from typing import Any, Type, Optional

import logging

from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool


logger = logging.getLogger(__name__)


class ClientProfileToolInput(BaseModel):
    name: str = Field(..., description="Имя клиента")
    # Other params
    ...


class ClientProfileTool(BaseTool):
    name: str = "ClientProfileTool"
    description: str = "Заполняет профиль нового клиента"
    args_schema: Optional[Type[BaseModel]] = ClientProfileToolInput

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def _run(self) -> ...:
        logger.info("---SAVE CLIENT PROFILE---")
        ...

    async def _arun(self) -> ...:
        logger.info("---SAVE CLIENT PROFILE---")
        ...
