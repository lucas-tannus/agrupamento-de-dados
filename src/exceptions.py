class ArgumentsError(BaseException):

    def __init__(self, message='Argumentos passados são inconsistentes'):
        self.message = message


class DatasetError(BaseException):
    def __init__(self, message='Erro no dataset'):
        self.message = message
