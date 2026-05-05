# =============================================================================
# Database Configuration
# =============================================================================
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/practicedb")
#
# engine = create_engine(DATABASE_URL, pool_size=5, max_overflow=10)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# def get_db():
#     """FastAPI dependency — yields a DB session, always closes it."""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
