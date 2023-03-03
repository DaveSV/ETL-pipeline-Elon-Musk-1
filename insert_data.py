import mysql.connector
import pandas as pd

# Cargar el archivo CSV en un dataframe
df = pd.read_csv('tweets_limpios_final.csv')

# Conectar a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tweets_db"
)

# Crear un cursor para ejecutar comandos SQL
cursor = db.cursor()

# Insertar los tweets en la tabla de la base de datos
for i, row in df.iterrows():
    tweet_text = row['tweet']
    cursor.execute("INSERT INTO tweets (tweet_text) VALUES (%s)", (tweet_text,))
    db.commit()

# Cerrar la conexión con la base de datos
db.close()

print("Los tweets han sido guardados en la base de datos.")
