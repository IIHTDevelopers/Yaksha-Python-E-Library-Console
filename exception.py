class ISBNDoesNotExistsError(Exception):
    def __init__(self,message):
        self.message=message
class ISBNAlreadyExistsError(Exception):
    def __init__(self,message):
        self.message=message
class BookNotAvailableError(Exception):
    def __init__(self,message):
        self.message=message
