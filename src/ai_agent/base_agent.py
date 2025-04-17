from abc import ABC, abstractmethod


class BaseAgent(ABC):
    @abstractmethod
    async def generate(self, thread_id: str, query: str) -> str:
        raise NotImplemented
