#!/usr/bin/python3
from models.user import User

print(type(User.last_name) is str)
print(User.last_name == "")
