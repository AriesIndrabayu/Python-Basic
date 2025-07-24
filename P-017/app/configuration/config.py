from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_DRIVER: str = "mysql+mysqlconnector"
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = ""
    DB_NAME: str = "catatan_db_v2"
    model_config: SettingsConfigDict = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"{self.DB_DRIVER.strip()}://{self.DB_USER.strip()}:{self.DB_PASSWORD.strip()}@"
            f"{self.DB_HOST.strip()}:{self.DB_PORT}/{self.DB_NAME.strip()}"
        )


settings = Settings()
