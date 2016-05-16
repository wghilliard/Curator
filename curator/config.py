# CURATOR
PATH = "/Users/wghilliard/E_TEST"

# CELERY
CELERY_RESULT_BACKEND = 'amqp'
CELERY_TASK_RESULT_EXPIRES = None
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
# BROKER_URL = 'amqp://celery:catsinfrats@localhost:5672/myvhost/'


# MONGO
MONGODB_DB = 'dqm'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

PW = 'password'

IGNORE = ['.DS_Store', 'config.json', 'config_test.json']

