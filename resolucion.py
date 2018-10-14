from sqlalchemy import create_engine

import argparse
import pandas as pd

__author__ = 'jaquinoa'

def split_rfecha(rd):
    s = rd.split('-')
    r = '000' + s[0]
    r = '2018_' + r[-5:]
    return r

db_engine = create_engine('mysql+pymysql://user:password@localhost/pydb')

parser = argparse.ArgumentParser(description='Copiar Resoluciones en Excel a DB')
parser.add_argument('-e', '--excel', help='Archivo Excel', required=True)
parser.add_argument('-s', '--sheet', help='Hoja Excel con las Resoluciones', required=True)
args = parser.parse_args()

print("**** Copiar Excel resoluciones a una Tabla MySQL ****")

print("Leyendo archivo Excel...")
xlsfile = args.excel
sheet   = args.sheet
df =  pd.read_excel(xlsfile, sheet_name = sheet, usecols = 10)

print("Borrar filas vacias...")
df.dropna(subset=['R.D.UGEL'], inplace=True)

# Set columns names
df.columns = ['Apellidos','rd', 'Fecha', 'Asunto', 'ie', 'Expediente', 'Folios', 'Proyecto', 'Area', 'DNI', 'Otro']


# Dates
df["Fecha"] = df["Fecha"].dt.strftime("%d/%m/%Y")

# rfecha
df["rfecha"] = df["rd"].apply(split_rfecha)

print(df.head())

print("Copiar a Base de Datos...")
df.to_sql(con=db_engine, name='_resoluciones2018', if_exists='replace', index_label = 'id')

print('Done...')
