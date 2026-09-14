from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://expense_tracker_db_31ny_user:fJcPHhNLGYINDbfmfnPeeffqt8rhqO99@dpg-daiijduk1f9s738bs490-a/expense_tracker_db_31ny"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()