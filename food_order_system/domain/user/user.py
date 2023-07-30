"""User domain"""
from dataclasses import dataclass, field
from datetime import datetime

from phonenumbers import parse

from food_order_system.exception.base_exception import NotCreatedException


@dataclass
class User:
    name: str
    phone_number: str
    is_verified: bool = False
    created_at: datetime = field(default_factory=lambda: datetime.now())
    updated_at: datetime = field(default_factory=lambda: datetime.now())

    def __eq__(self, obj: object) -> bool:
        return self.phone_number == obj.phone_number if isinstance(obj, User) else False

    def authenticate_sending_sms(self) -> None:
        if parse(self.phone_number, None).country_code != 33:
            raise NotCreatedException("User", "Phone number must be French")
        # TODO: Send SMS to user to authenticate
        self.is_verified = True
