from pydantic import BaseModel, EmailStr, Field

class AdminResponse(BaseModel):
    discord_id: str
    username: str
    password: str
    role: str
    email: EmailStr
    reddit_id: str | None
