import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_TRACK_MODIFICATIONS = False
#Externo
#SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:ORupxs59KTNbCWprN9YbIaCIRAlBiGi2@dpg-cta3frogph6c73ejjog0-a.oregon-postgres.render.com/test_93i0'
#interna
#postgresql://test_m4mc_user:7Ts2lHx5HdsW2dpiEfIEKy33MlTQqezw@dpg-ctui1gbtq21c73bio7sg-a/test_m4mc
SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://test_m4mc_user:7Ts2lHx5HdsW2dpiEfIEKy33MlTQqezw@dpg-ctui1gbtq21c73bio7sg-a/test_m4mc'
SQLALCHEMY_TRACK_MODIFICATIONS=False
