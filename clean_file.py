import pandas as pd
import re

# Cargar el archivo CSV en un dataframe
df = pd.read_csv('tweets.csv')

# Eliminar los tweets duplicados
df.drop_duplicates(inplace=True)

# Eliminar los tweets vacíos
df.dropna(subset=['tweet'], inplace=True)

# Eliminar los links de los tweets
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"http\S+", "", x))

# Eliminar los usuarios mencionados en los tweets
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"@\S+", "", x))

# Eliminar los hashtags de los tweets
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r"#\S+", "", x))

# Eliminar los caracteres especiales y los emojis
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
df['tweet'] = df['tweet'].apply(lambda x: re.sub(r'[^\x00-\x7f]', '', x))

# Convertir todos los caracteres a minúsculas
df['tweet'] = df['tweet'].apply(lambda x: x.lower())

# Guardar el dataframe de tweets limpios en un nuevo archivo CSV
df.to_csv('tweets_limpios.csv', index=False)

print("Los tweets limpios han sido guardados en el archivo 'tweets_limpios.csv'.")
