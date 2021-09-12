import json

with open('/etc/gooselit_config.json') as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config.get('SECRET_KEY')

    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_DEFAULT_SENDER = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PW')

    MAIL_PORT = 587
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = True