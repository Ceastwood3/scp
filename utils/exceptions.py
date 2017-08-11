"""Comprehensive list of all base module exceptions"""

class BaseError(Exception):

    def __init__(self, message=None, logger_function=None):
        super(BaseError, self).__init__(message)
        self.logger_function = logger_function
        if logger_function:
            logger_function(message)

    def get_logger(self):
        return self.logger_function


class BaseCallException(BaseError):
    def __init__(self, message=None, logger_function=None):
        super(BaseCallException, self).__init__(message, logger_function)


class PandasUtilsException(BaseCallException):
    def __init__(self, message=None, logger_function=None):
        super(PandasUtilsException, self).__init__('PandasUtilException: ' + message, logger_function)


class GeneralUtilsException(BaseCallException):
    def __init__(self, message=None, logger_function=None):
        super(GeneralUtilsException, self).__init__('GeneralUtilException: ' + message, logger_function)







