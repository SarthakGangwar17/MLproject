import sys
def error_message(error,errorDetails:sys):
    _,_,exc_tb=errorDetails.excinfo()
    fileName=exc_tb.tb_frame.f_code.co_filename
    errorMessage="Error occured in pythob script name[{0}] line number [{1}] error message [{2}]"
    fileName,exc_tb.tb_lineno,str(error)
    return errorMessage




class customException(Exception):
    def __init__(self, error,errorMessage,errorDetails:sys):
        super().__init__(errorMessage)
        self.errorMessage=error_message(error,errorDetails=errorDetails)

    def __str__(self) -> str:
        return self.errorMessage