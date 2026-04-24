import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context


from dotenv import load_dotenv
load_dotenv()

# Pobierz konfigurację Alembica
config = context.config

# NADPISZ url danymi z pliku .env
db_url = os.getenv("DATABASE_URL")
if db_url:
    config.set_main_option("sqlalchemy.url", db_url)




# 1. Wskazujemy ścieżkę do folderu "kurs repository"
# Najpierw znajdujemy folder KURS_LOKALNY
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Potem dodajemy do niego podfolder "kurs_repository"
MODELS_DIR = os.path.join(BASE_DIR, "kurs_repository")

if MODELS_DIR not in sys.path:
    sys.path.insert(0, MODELS_DIR)

# 2. Teraz Python znajdzie plik models.py wewnątrz "kurs repository"
try:
    from models import Base
except ImportError as e:
    print(f"\nBŁĄD: Nie znaleziono pliku models.py w {MODELS_DIR}")
    print(f"Zawartość tego folderu: {os.listdir(MODELS_DIR) if os.path.exists(MODELS_DIR) else 'Folder nie istnieje'}")
    raise e

# --- Reszta konfiguracji ---
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "pyformat"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
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