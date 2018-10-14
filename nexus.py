from sqlalchemy import create_engine
from sqlalchemy import select

import argparse
import pandas as pd

__author__ = 'jaquinoa'

db_engine = create_engine('mysql+pymysql://user:password@localhost/pydb')

parser = argparse.ArgumentParser(description='Copiar Nexus en Excel a DB')
parser.add_argument('-e', '--excel', help='Archivo Excel', required=True)
parser.add_argument('-s', '--sheet', help='Hoja Excel data Nexus', required=False)
args = parser.parse_args()

print("-----------------------------------------------------")
print("")
print("*******  Copiar Excel Nexus a una Tabla MySQL *******")

print("Leyendo archivo Excel...")
xlsfile = args.excel
sheet   = args.sheet
df =  pd.read_excel(xlsfile, skiprows = 4, dtype = str)

# Set columns names
df.columns = ['region', 'distrito', 'ugel', 'provincia', 'distrito', 'tipo_ie', 'gestion', 'zona', 'codmod_ie', 'clave8', 'niveleducativo', 'nombre_ie', 'codigo_plaza', 'tipo_trabajador', 'subtipo_trabajador', 'cargo', 'situacion_laboral', 'motivo_vacante', 'paterno', 'materno', 'nombres', 'categoria_remunerativa', 'jornada_laboral', 'estado', 'codigo_modular', 'fecha_nacimiento', 'dni', 'fecha_inicio', 'fecha_termino', 'tipo_registro', 'ley', 'preventiva', 'referencia_preventiva']

print(df.info())

print("Copiar a Base de Datos...")
df.to_sql(con=db_engine, name='_nexus2018', if_exists='replace', index_label = 'id')

print('Done...')
