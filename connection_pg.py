import psycopg2

URL = "postgres://nezir:S7WUsSJ2to8uIfHtpdAqriGDCeD1Hrxu@dpg-chd4qpm7avjcvo5maee0-a.frankfurt-postgres.render.com/data_fast_fashion"

connexion = psycopg2.connect(URL)

cursor = connexion.cursor()

cursor.execute("""
    CREATE TABLE fashion (
               id SERIAL PRIMARY KEY NOT NULL,
               fast_influent VARCHAR(150), 
               fast_frequency VARCHAR(150), 
               fast_site VARCHAR(150), 
               ethic_importance VARCHAR(150), 
               ethic_select VARCHAR(200), 
               ethic_price VARCHAR(150),
               recycling_constumer VARCHAR(50), 
               recycling VARCHAR(200), 
               environment VARCHAR(200), 
               material VARCHAR(50), 
               situation VARCHAR(50), 
               sex VARCHAR(50), 
               age INTEGER)
""")
               

cursor.execute("""
    SELECT * FROM posts
""")
results = cursor.fetchall()

print(results)
#Enregister de la requête           
connexion.commit()


cursor.close()
connexion.close()
