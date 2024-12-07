import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:ORupxs59KTNbCWprN9YbIaCIRAlBiGi2@dpg-cta3frogph6c73ejjog0-a.oregon-postgres.render.com/test_93i0'
#interna
#SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:ORupxs59KTNbCWprN9YbIaCIRAlBiGi2@dpg-cta3frogph6c73ejjog0-a/test_93i0'
SQLALCHEMY_TRACK_MODIFICATIONS=False
