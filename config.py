DATABASE = 'flask-demo'
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
PORT = 3306

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                          PORT,
                                                                          DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
#                                                                                         password=PASSWORD,
#                                                                                         host=HOSTNAME, port=PORT,
#                                                                                         db=DATABASE)
# SQLALCHEMY_TRACK_MODIFICATIONS = True
