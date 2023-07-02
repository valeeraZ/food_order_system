import phonenumbers
from pydantic import BaseModel, validator


class UserCreateModel(BaseModel):
    name: str
    phone_number: str

    @validator("phone_number")
    def validate_phone_number(cls, value):
        try:
            phone_number = phonenumbers.parse(value, None)
            if not phonenumbers.is_valid_number(phone_number):
                raise ValueError("Invalid phone number")
        except:
            raise ValueError("Invalid phone number")
        return value
