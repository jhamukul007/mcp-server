from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    id: Optional[int] = None

    def get_name(self) -> str:
        return self.name

    def get_age(self):
        return self.age

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
