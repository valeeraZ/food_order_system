class UserNotFoundException(Exception):
    def __init__(self, phone_number: str):
        super().__init__(f"User with phone number {phone_number} not found")


class UserNotCreatedException(Exception):
    def __init__(self, phone_number: str, error: str):
        super().__init__(f"User with phone number {phone_number} not created. {error}")
