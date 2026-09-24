import uuid

from fastapi import HTTPException, status, APIRouter

from models.user import User

user_dict = {}
router = APIRouter()

@router.post("/user", status_code=status.HTTP_201_CREATED)
def register_user(user: User):
    if user.name is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name is required")

    if user.age < 0 or user.age > 100:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Age is out of range")
    user.set_id(str(uuid.uuid4()))
    user_dict[user.id] = user
    print(user_dict)

    return user


@router.get("/user/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: str):
    print(user_dict)
    return user_dict.get(user_id)


