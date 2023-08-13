#!/usr/bin/python3
"""
Defines User class
"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """
    The User class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
