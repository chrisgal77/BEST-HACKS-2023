import json
import hashlib
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel


PATH = "/home/mb-pro-kg/best23/data/users.json"


class User(BaseModel):
    user_id: int = str(uuid4())
    name: str
    login: str
    password: str
    description: Optional[str] = ""


def load(path: str) -> dict:
    with open(path, "r") as file:
        return json.load(file)
    
def save(path: str, data: dict) -> dict:
    with open(path, "w") as file:
        return json.dump(data, file, indent=4)


class JSONDatabaseHandler:
    def __init__(self) -> None:
        self.users = load(PATH)["users"]

    def login(self, login: str, password: str):
        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))
        for user in self.users:
            if user["login"] == login and hasher.hexdigest() == user["password"]:
                return user["user_id"]
        return None

    def register(self, login: str, password: str, name: str, description: str):
        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))
        
        user = User(
            name=name,
            login=login,
            password=hasher.hexdigest(),
            description=description
        )

        self.users.append(
            dict(user)
        )
        save(path=PATH, data={"users": self.users})
        return user.user_id

    def update_description(self, user_id: int, description: str):
        for idx, user in enumerate(self.users):
            if user["user_id"] == user_id:
                self.users[idx]["description"] = description
        save(path=PATH, data={"users": self.users})
    
database = JSONDatabaseHandler()