from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
    POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE")

    BOOK_GRPC_SERVER_ADDR = os.environ.get("BOOK_GRPC_SERVER_ADDR")
