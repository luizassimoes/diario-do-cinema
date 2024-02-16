from urllib.parse import quote_plus

SECRET_KEY = 'LuEThi_Filminhos'
senha = 'lss003@MySQL'

SQLALCHEMY_DATABASE_URI = \
           '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
               SGBD = 'mysql+mysqlconnector',
               usuario = 'root',
               senha = quote_plus(senha),
               servidor = 'localhost',
               database = 'lu_e_thi'
           )