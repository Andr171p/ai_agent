import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class EmbeddingsSettings(BaseSettings):
    model_name: str = "intfloat/multilingual-e5-large"
    model_kwargs: dict = {"device": "cpu"}
    encode_kwargs: dict = {'normalize_embeddings': False}


class ElasticsearchSettings(BaseSettings):
    host: str = os.getenv("ELASTIC_HOST")
    user: str = os.getenv("ELASTIC_USER")
    password: str = os.getenv("ELASTIC_PASSWORD")


class RedisSettings(BaseSettings):
    host: str = os.getenv("REDIS_HOST")
    port: int = os.getenv("REDIS_PORT")
    user: str = os.getenv("REDIS_USER")
    password: str = os.getenv("REDIS_PASSWORD")


class GigaChatSettings(BaseSettings):
    api_key: str = os.getenv("GIGACHAT_API_KEY")
    scope: str = os.getenv("GIGACHAT_SCOPE")
    model_name: str = os.getenv("GIGACHAT_MODEL_NAME")


class YandexGPTSettings(BaseSettings):
    folder_id: str = os.getenv("YANDEX_FOLDER_ID")
    api_key: str = os.getenv("YANDEX_GPT_API_KEY")


class Settings(BaseSettings):
    embeddings: EmbeddingsSettings = EmbeddingsSettings()
    elasticsearch: ElasticsearchSettings = ElasticsearchSettings()
    redis: RedisSettings = RedisSettings()
    giga_chat: GigaChatSettings = GigaChatSettings()
    yandex_gpt: YandexGPTSettings = YandexGPTSettings()


settings = Settings()
