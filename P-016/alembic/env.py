from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
import os
import sys

"""Menambahkan path folder app ke sistem path --> Biar bisa import dari folder app"""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
"""Import konfigurasi & Base"""
from app.database.connection import Base
from app.configuration.config import settings
from app.models import note_model

# Ambil kofigurasi alembic
config = context.config

# Set URL database dari settings FastAPI
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Metadata model yang mau di-track Alembic
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
