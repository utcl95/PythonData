from sqlalchemy import create_engine

import argparse
import pandas as pd

__author__ = 'jaquinoa'

db_engine = create_engine('mysql+mysqlconnector://root:a123456B@localhost/eel')

parser = argparse.ArgumentParser(description='Copiar Resoluciones en Excel a DB')
parser.add_argument('-e', '--excel', help='Archivo Excel', required=True)
parser.add_argument('-s', '--sheet', help='Hoja Excel con las Resoluciones', required=True)
args = parser.parse_args()

# Load Excel File
xlsfile = args.excel
sheet   = args.sheet
df =  pd.read_excel(xlsfile, sheet_name = sheet)

# Drop empty rows
df.dropna(subset=['R.D.UGEL'], inplace=True)

# Set columns names
df.columns = ['Apellidos','rd', 'Fecha', 'Asunto', 'ie', 'Expediente', 'Folios', 'Proyecto', 'Area', 'DNI', 'Otro']

# Dates
df["Fecha"] = df["Fecha"].dt.strftime("%d/%m/%Y")

# rfecha
df["rfecha"] = "2018_" + df["rd"].str[:4]

#print(df.head())
#print(df["rfecha"])

print("Hello World...")
# Copy to Table
# df.to_sql(con=db_engine, name='_resoluciones2018', if_exists='replace')

print('Done...')
