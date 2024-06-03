from pydantic import BaseModel

class StoryBase(BaseModel):
    title: str
    description: str
    category: str

class StoryCreate(StoryBase):
    pass

class StoryDisplay(StoryBase):
    id: int

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserDisplay(UserBase):
    id: int
    is_active: bool
