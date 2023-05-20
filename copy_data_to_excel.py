import psycopg2
from openpyxl import Workbook
from decouple import config

URL = config('URL_DATABASE_CONNEXION')

connexion = psycopg2.connect(URL)
cursor = connexion.cursor()
query = "SELECT * FROM fashion"
cursor.execute(query)

results = cursor.fetchall()


#Tableur excel
tab = Workbook()
sheet = tab.active

headers = [desc[0] for desc in cursor.description]
sheet.append(headers)

for row in results:
    sheet.append(row)

tab.save('mes_donnees.xlsx')



cursor.close()
connexion.close()
