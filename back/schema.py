from pydantic import BaseModel


class ContactResponse(BaseModel):
    id: int
    name: str
    email: str
    message: str

    class Config:
        from_attributes = True