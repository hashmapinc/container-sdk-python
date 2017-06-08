class HALBaseException(Exception):
    def __init__(self, *args, **kwargs):
        super(HALBaseException, self).__init__(*args, **kwargs)


class HALException(HALBaseException):
    def __init__(self, code=0, message='Unexpected error'):
        self.code = code
        self.message = message

    def __str__(self):
        return 'Error code: {}, reason: {}'.format(self.code, self.message)