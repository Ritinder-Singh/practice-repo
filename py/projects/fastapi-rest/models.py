# =============================================================================
# SQLAlchemy Models
# =============================================================================
# from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime
#
# Base = declarative_base()
#
# class Product(Base):
#     __tablename__ = "products"
#     id         = Column(Integer, primary_key=True, index=True)
#     name       = Column(String(200), nullable=False)
#     price      = Column(Float, nullable=False)
#     category   = Column(String(100))
#     stock      = Column(Integer, default=0)
#     deleted_at = Column(DateTime, nullable=True)
#     created_at = Column(DateTime, default=datetime.utcnow)
#
# class User(Base):
#     __tablename__ = "users"
#     id             = Column(Integer, primary_key=True, index=True)
#     email          = Column(String(255), unique=True, nullable=False, index=True)
#     hashed_password = Column(String, nullable=False)
#     is_active      = Column(Boolean, default=True)
#     created_at     = Column(DateTime, default=datetime.utcnow)
