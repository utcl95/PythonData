from sqlalchemy import create_engine
from sqlalchemy import select

import argparse
import pandas as pd

__author__ = 'jaquinoa'

db_engine = create_engine('mysql+pymysql://jaquino:a123456B@localhost/eel')

parser = argparse.ArgumentParser(description='Copiar Nexus en Excel a DB')
parser.add_argument('-e', '--excel', help='Archivo Excel', required=True)
parser.add_argument('-s', '--sheet', help='Hoja Excel data Nexus', required=False)
args = parser.parse_args()

print("-----------------------------------------------------")
print("")
print("*******  Copiar Excel SUP Planilla a una Tabla MySQL *******")

cols = [0, 3, 5, 6, 7, 8, 9, 11, 16, 22, 23, 25, 26, 27, 54]

print("Leyendo archivo Excel...")
xlsfile = args.excel
sheet   = args.sheet
df =  pd.read_excel(xlsfile, usecols=cols, dtype = str)

# Set columns names
df.columns = ['CodigoModular', 'Situacion', 'Paterno', 'Materno', 'Nombres', 'Sexo', 'FechaNacimiento', 'dni', 'IIEE', 'Condicion',  'TipoServidor', 'NivelMagisterial', 'EscalaMagisterial', 'Grupo', 'Ley']

print("Copiar a Base de Datos...")
df.to_sql(con=db_engine, name='_sup2018', if_exists='replace', index_label = 'id')

print('Done...')
