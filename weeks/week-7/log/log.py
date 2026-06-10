from datetime import datetime
import logging
import json


logging.basicConfig(
      filename='app.log',
      encoding='utf-8',
      level=logging.DEBUG,
      format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
  )

logger = logging.getLogger('payments')
def process_payment(user_id, amount):
    logger.info(f'Starting payment for user {user_id}, amount: {amount}')
    if amount <= 0:
        logger.error(f'Invalid amount: {amount}')
        return
    logger.info(f'Payment of {amount} completed for user {user_id}')


#8
def read_config(filepath):
    logger.debug(f'Attempting to read config from {filepath}')
    try:
        with open(filepath) as f:
            data = f.read()
            logger.info(f'Successfully read config from {filepath}')
            return data
    except FileNotFoundError:
        logger.exception(f'Config file not found: {filepath}')
        return None    

#9
def write_structured_log(level, module, message, **extra):
     log_entry = {
      "timestamp": datetime.utcnow().isoformat(),
      "level": level,
      "module": module,
      "message": message,
      **extra
  }
     print(json.dumps(log_entry))   


#12
logger = logging.getLogger(__name__)
def register_user(email, password, age):
    logger.debug(f'Starting registration for {email}')
    if age < 18:
        logger.error(f'Registration failed: age {age} is under 18')
        return
    logger.info(f'User registered successfully: {email}')
    logger.info(f'Registration completed for {email}')
