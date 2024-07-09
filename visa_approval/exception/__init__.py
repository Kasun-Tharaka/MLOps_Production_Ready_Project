import os
import sys


# sys module, which contains functions to interact with the interpreter
def error_message_detail(error, error_detail:sys):
    # extracts the traceback (exc_tb) from the current exception information
    _, _, exc_tb = error_detail.exc_info()
    # retrieves the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message

# Custom exception
# inherits from the built-in Exception class
class visa_approvalException(Exception):
    # constructor takes two arguments
    def __init__(self, error_message, error_detail):
        #  Calls the constructor of the parent Exception class with the original error message
        super().__init__(error_message)
        #  function to generate a detailed error message and assigns it to the instance variable
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message