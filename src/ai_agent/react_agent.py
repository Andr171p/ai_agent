from typing import List

from langgraph.prebuilt import create_react_agent
from langgraph.graph.state import CompiledStateGraph
from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.graph import START, StateGraph, MessagesState

from langchain_core.tools import BaseTool
from langchain_core.language_models import BaseChatModel

from src.ai_agent.base_agent import BaseAgent


class ReACTAgent(BaseAgent):
    def __init__(
            self,
            checkpoint_saver: BaseCheckpointSaver,
            tools: List[BaseTool],
            prompt: str,
            model: BaseChatModel
    ) -> None:
        self._checkpoint_saver = checkpoint_saver
        self._tools = tools
        self._prompt = prompt
        self._model = model

    async def generate(self, thread_id: str, query: str) -> str:
        config = {"configurable": {"thread_id": thread_id}}
        inputs = {"messages": [{"role": "human", "content": query}]}
        compiled_graph = self._build_compiled_graph()
        response = await compiled_graph.ainvoke(inputs, config=config)
        message = response.get("messages")[-1]
        generated = message.content
        return generated

    def _build_compiled_graph(self) -> CompiledStateGraph:
        react_agent = create_react_agent(
            tools=self._tools,
            state_modifier=self._prompt,
            model=self._model
        )
        graph = StateGraph(MessagesState)
        graph.add_node("agent", react_agent)
        graph.add_edge(START, "agent")
        compiled_graph = graph.compile(checkpointer=self._checkpoint_saver)
        return compiled_graph
