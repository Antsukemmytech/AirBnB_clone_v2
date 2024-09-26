#!/user/bin/python3
"""user class"""

from models.base_model import BaseModel


class user(BaseModel):
    """user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""


