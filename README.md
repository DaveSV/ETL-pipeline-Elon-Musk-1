# ETL-pipeline-Elon-Musk-1

About
ETL pipeline Comprendiendo a Elon Musk por sus tweets Parte 1

Creación de un conjunto de datos de Twitter con Pandas en Python utilizando la biblioteca Snscrape. Persistencia de datos en MySQL.
Este código busca tweets de Elon Musk desde el 1 de enero de 2021 hasta el 1 de enero de 2022 y guarda los resultados en un archivo CSV llamado "tweets.csv".

Instalar Snscrape y Pandas utilizando pip en tu entorno virtual de Python:

pip install snscrape pandas

Importar las bibliotecas necesarias:

import snscrape.modules.twitter as sntwitter
import pandas as pd

Definir una consulta de búsqueda utilizando el formato de consulta de búsqueda de Twitter:

query = "from:elonmusk since:2021-01-01 until:2022-01-01"

![image](https://user-images.githubusercontent.com/29576337/222800127-15db4a43-10c9-41ae-8593-3a1049a94340.png)

Opcionalmente, puedes guardar el dataframe en un archivo CSV para su posterior uso:

![Captura de pantalla dataset](https://user-images.githubusercontent.com/29576337/222799377-f63f3727-6404-456b-9618-5cd0f2754edb.png)

Para limpiar los datos obtenidos del archivo "tweets.csv" creado anteriormente, podemos utilizar Pandas para cargar el archivo CSV en un dataframe y luego realizar diversas operaciones de limpieza y preprocesamiento de datos.

![image](https://user-images.githubusercontent.com/29576337/222800293-0d3e06e7-d45b-4f21-87d5-08c07dc617d0.png)

Este es solo un ejemplo básico de algunas de las operaciones de limpieza que se pueden realizar en los datos de los tweets. Dependiendo de los datos específicos que se estén utilizando, puede ser necesario realizar otras operaciones de limpieza y preprocesamiento de datos.

Para guardar el dataset de tweets limpios en un nuevo archivo CSV llamado "tweets_limpios.csv", podemos utilizar el método to_csv() del dataframe de Pandas.

Aquí te dejo un ejemplo de cómo podrías hacerlo:

![image](https://user-images.githubusercontent.com/29576337/222800541-a213d0db-74eb-4623-b3b5-6a4ac3e68e02.png)

Para guardar los datos del archivo "tweets_limpios.csv" en una base de datos MySQL, necesitaremos instalar la librería de Python mysql-connector-python. También necesitaremos crear una base de datos y una tabla en MySQL para almacenar los datos.

A continuación te dejo un ejemplo de cómo podrías hacerlo:

Primero, instala la librería mysql-connector-python utilizando el siguiente comando en la terminal o en el símbolo del sistema (si estás utilizando Windows):

pip install mysql-connector-python

A continuación, crea una base de datos y una tabla en MySQL utilizando los siguientes scripts SQL:

![image](https://user-images.githubusercontent.com/29576337/222800804-8223bab2-c040-48c8-8fca-6c101bd9e6ae.png)

Este script creará una base de datos llamada tweets_db y una tabla llamada tweets con dos columnas: id (un número de identificación único para cada tweet) y tweet_text (el texto del tweet).

Ahora, puedes utilizar el siguiente script de Python para leer los datos del archivo "tweets_limpios.csv" y guardarlos en la base de datos:

![image](https://user-images.githubusercontent.com/29576337/222800983-10771306-103e-43ed-b9ab-dd85b3185bf5.png)

Asegúrate de cambiar los valores de host, user y password en la función mysql.connector.connect() para que coincidan con tu configuración de MySQL.

Este script carga los datos del archivo CSV en un dataframe de Pandas y luego se conecta a la base de datos MySQL utilizando la librería mysql-connector-python. A continuación, se crea un cursor para ejecutar comandos SQL y se inserta cada tweet en la tabla de la base de datos utilizando un bucle for y la función cursor.execute(). Finalmente, se cierra la conexión con la base de datos y se imprime un mensaje para confirmar que los datos se han guardado correctamente.

![image](https://user-images.githubusercontent.com/29576337/222815627-471c9ecd-ccbc-4fa4-9590-93b5d5a9b839.png)


Espero que esto te ayude a guardar los datos del archivo "tweets_limpios_final.csv" en una base de datos MySQL.

En la Parte 2 de este tutorial avanzaremos a programar, monitorear y administrar todo el flujo de trabajo de estos datos con Airflow.

En la Parte 3. analizaremos un Análisis de Sentimientos sobre el conjunto de datos y registrode la Base de Datos
