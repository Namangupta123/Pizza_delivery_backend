from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.getenv("JWT_SECRET")

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    model_config = {
        'from_attributes': True,
        'json_schema_extra': {
            'example': {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }
    }

class Settings(BaseModel):
    authjwt_secret_key: str = secret_key

class LoginModel(BaseModel):
    username: str
    password: str

class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = "PENDING"
    pizza_size: Optional[str] = "SMALL"
    user_id: Optional[int]

    model_config = {
        'from_attributes': True,
        'json_schema_extra': {
            "example": {
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }
    }

class OrderStatusModel(BaseModel):
    order_status: Optional[str] = "PENDING"

    model_config = {
        'from_attributes': True,
        'json_schema_extra': {
            "example": {
                "order_status": "PENDING"
            }
        }
    }