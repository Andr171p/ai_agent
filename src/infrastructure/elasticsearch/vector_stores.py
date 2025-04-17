from typing import Any

from langchain_core.embeddings import Embeddings
from langchain_elasticsearch import ElasticsearchStore


class PriceListElasticsearchStore(ElasticsearchStore):
    def __init__(
            self,
            es_url: str,
            es_user: str,
            es_password: str,
            embeddings: Embeddings,
            index_name: str = "price-list-vector-index",
            **kwargs: Any
    ) -> None:
        super().__init__(
            es_url=es_url,
            es_user=es_user,
            es_password=es_password,
            index_name=index_name,
            embedding=embeddings,
            **kwargs
        )


class ProgramInstructionsElasticsearchStore(ElasticsearchStore):
    def __init__(
            self,
            es_url: str,
            es_user: str,
            es_password: str,
            embeddings: Embeddings,
            index_name: str = "program-instructions-vector-index",
            **kwargs: Any
    ) -> None:
        super().__init__(
            es_url=es_url,
            es_user=es_user,
            es_password=es_password,
            index_name=index_name,
            embedding=embeddings,
            **kwargs
        )
