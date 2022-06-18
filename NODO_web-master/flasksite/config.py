import os


class Config:
    #must hide SECRET_KEY and SQLALCHEMY_DATABASE_URI before deployment
    SECRET_KEY="5791628bb0b13ce0c676dfde280ba245"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #change to Nodo's official email(gmail)
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')