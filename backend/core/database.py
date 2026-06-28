from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def connect_db():
    """Verify database connectivity."""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("PostgreSQL connected successfully.")
    except Exception as e:
        print(f"Failed to connect to PostgreSQL: {e}")
        raise


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()