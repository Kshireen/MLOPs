from us_visa.logger import logging

from us_visa.exception import USvisaException
import sys



logging.info("Welcome to our project")  

try:
    q = 2/0
    logging.info(q)
except Exception as e :
    logging.info("Error has occured")
    raise USvisaException(e,sys)



