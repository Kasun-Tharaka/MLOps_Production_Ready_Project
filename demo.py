from visa_approval.logger import logging
from visa_approval.exception import visa_approvalException
import sys

logging.info('checking the logging works')


try:
    a = 5/0
except Exception as e:
    raise visa_approvalException(e, sys)