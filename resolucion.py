from sqlalchemy import create_engine
import pandas as pd

db_engine = create_engine('mysql+mysqlconnector://root:a123456B@localhost/eel')

# Load Excel File
xlsfile = 'D:\\UGEL05\\Resoluciones_2018.xlsx'
sheet   = 'RESOLUCIONES 2018'
df =  pd.read_excel(xlsfile, sheet_name = sheet)

# Drop empty rows
df.dropna(subset=['R.D.UGEL'], inplace=True)

df.columns = ['Apellidos','Ugel', 'Fecha', 'Asunto', 'ie', 'Expediente', 'Folios', 'Proyecto', 'Area', 'DNI', 'Otro']

# Copy to Table
df.to_sql(con=db_engine, name='_resoluciones2018', if_exists='replace')

print('Done...')
