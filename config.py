from urllib.parse import quote_plus
import pandas as pd

params = pd.read_csv('config.txt', sep=' = ', header=None, engine='python')

SECRET_KEY = params.loc[params[0] == 'SECRET_KEY'][1].values[0]
senha = params.loc[params[0] == 'senha'][1].values[0]

SQLALCHEMY_DATABASE_URI = \
           '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
               SGBD = 'mysql+mysqlconnector',
               usuario = 'root',
               senha = quote_plus(senha),
               servidor = 'localhost',
               database = params.loc[params[0] == 'database'][1].values[0]
           )