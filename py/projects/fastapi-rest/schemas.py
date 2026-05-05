# =============================================================================
# Pydantic Schemas
# =============================================================================
# from pydantic import BaseModel, Field, field_validator
# from datetime import datetime
#
# class ProductCreate(BaseModel):
#     name:     str   = Field(..., min_length=1, max_length=200)
#     price:    float = Field(..., gt=0, description="Must be positive")
#     category: str | None = None
#     stock:    int   = Field(default=0, ge=0)
#
# class ProductUpdate(BaseModel):
#     name:     str | None = None
#     price:    float | None = Field(default=None, gt=0)
#     category: str | None = None
#     stock:    int | None = None
#
# class ProductResponse(ProductCreate):
#     id:         int
#     created_at: datetime
#     class Config:
#         from_attributes = True
#
# class Token(BaseModel):
#     access_token: str
#     token_type:   str = "bearer"
