import pandas as pd
import re
from unidecode import unidecode

# Cargar el archivo CSV en un dataframe
df = pd.read_csv('tweets_limpios.csv')

# Eliminar los tweets duplicados
df.drop_duplicates(inplace=True)

# Rellenar los tweets vacíos con una cadena vacía
df['tweet'].fillna('0', inplace=True)

df.columns = df.columns.str.strip()

# Definir una función genérica para limpiar los tweets
def clean_tweet(tweet):
    # Eliminar los links, usuarios y hashtags de los tweets
    tweet = re.sub(r"http\S+|@\S+|#\S+", "", tweet)
    # Convertir los caracteres especiales y emojis en caracteres ASCII equivalentes
    tweet = unidecode(tweet)
    # Eliminar los caracteres especiales y convertir todo a minúsculas
    tweet = re.sub(r'[^\w\s]', '', tweet.lower())
    return tweet

# Aplicar la función clean_tweet a la columna tweet del dataframe
df['tweet'] = df['tweet'].apply(clean_tweet)

# Guardar el dataframe de tweets limpios en un nuevo archivo CSV
df.to_csv('tweets_limpios_final.csv', index=False)

print("Los tweets limpios han sido guardados en el archivo 'tweets_limpios_final.csv'.")
