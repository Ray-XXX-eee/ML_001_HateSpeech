import sys
 
def error_message_details(error,error_details: sys)-> str:
    _, _,exc_trackBack= error_details.exc_info()
    file_name = exc_trackBack.tb_frame.f_code.co_filename
    line_no = exc_trackBack.tb_lineno
    error_message = f"Error occured in [{file_name}] script, at line [{line_no}], with error message [{str(error)}]" #format(file_name,exc_trackBack.tb_lineno,str(error))
    return error_message

class CustomErrorMsg(Exception):
    def __init__(self, error_message, error_details):
        '''
        :param error_message : error message in string format'''
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message,error_details=error_details
        )
    
    def __str__(self):
        return self.error_message