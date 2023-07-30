from typing import Optional


class NotFoundException(Exception):
    def __init__(self, name: str):
        super().__init__(f"{name} not found")


class NotCreatedException(Exception):
    def __init__(self, name: str, error: Optional[str] = None):
        super().__init__(f"{name} not created. {error}")


class NotUpdatedException(Exception):
    def __init__(self, name: str, error: Optional[str] = None):
        super().__init__(f"{name} not updated. {error}")


class NotDeletedException(Exception):
    def __init__(self, name: str, error: Optional[str] = None):
        super().__init__(f"{name} not deleted. {error}")
