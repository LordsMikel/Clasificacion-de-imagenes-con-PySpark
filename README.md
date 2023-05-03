## ⚠️ Advertencia

Este proyecto está actualmente en desarrollo y puede contener errores o funcionar de manera impredecible. Utilícelo bajo su propio riesgo y no lo utilice en producción hasta que se publique una versión estable.


# Clasificación de imágenes con PySpark

Este proyecto utiliza PySpark y técnicas de aprendizaje automático para clasificar imágenes en diferentes categorías.

## Requisitos

- PySpark 2.4.7 o superior
- Conjunto de datos de imágenes (por ejemplo, desde Kaggle)

## Instrucciones

1. Descarga el conjunto de datos de imágenes y extrae los archivos.
2. Abre un terminal y navega hasta la carpeta del proyecto.
3. Ejecuta el archivo "clasificacion_imagenes.py" utilizando el siguiente comando:


4. El programa cargará las imágenes, creará un vector de características para cada una y entrenará un modelo de Random Forest utilizando el conjunto de entrenamiento.
5. El modelo se utilizará para predecir la categoría de las imágenes del conjunto de prueba.
6. El programa mostrará la precisión del modelo utilizando la función "multiclassClassificationEvaluator".

## Paso a paso

### Descargar el conjunto de datos de imágenes

Descarga un conjunto de datos de imágenes para entrenar y probar el modelo. Puedes encontrar conjuntos de datos en línea, por ejemplo, en Kaggle.

### Navegar hasta la carpeta del proyecto

Abre un terminal y navega hasta la carpeta donde se encuentra el archivo "clasificacion_imagenes.py".

### Ejecutar el archivo "clasificacion_imagenes.py"

Ejecuta el archivo "clasificacion_imagenes.py" utilizando el siguiente comando:

```bash
spark-submit clasificacion_imagenes.py
````


### Revisar los resultados

El programa cargará las imágenes, creará un vector de características para cada una y entrenará un modelo de Random Forest utilizando el conjunto de entrenamiento. El modelo se utilizará para predecir la categoría de las imágenes del conjunto de prueba. El programa mostrará la precisión del modelo utilizando la función "multiclassClassificationEvaluator".

## Personalización

Puedes personalizar el proyecto cambiando los parámetros del modelo de Random Forest (por ejemplo, el número de árboles, la profundidad máxima, etc.) para mejorar la precisión del modelo.

## Créditos

Este proyecto fue creado por [Miguel Medina Cantos] como parte de un proyecto de aprendizaje personal de PySpark.

## Licencia

Este proyecto que está bajo *DESARROLLO* está bajo la licencia [MIT].

La cual implica:
Licencia MIT: es una licencia de software libre permisiva que permite la distribución de software libre y de código abierto sin restricciones en su uso, copia, modificación y distribución, siempre y cuando se incluya el aviso de copyright y la licencia.


#Pasos a hacer:
## Instrucciones

### Descargar el conjunto de datos de imágenes

1. Descarga un conjunto de datos de imágenes para entrenar y probar el modelo. Puedes encontrar conjuntos de datos en línea, por ejemplo, en Kaggle.

### Importar PySpark y crear una sesión de Spark

2. Abre un editor de código y crea un nuevo archivo de PySpark.
3. Importa PySpark y crea una sesión de Spark.

### Cargar las imágenes en un DataFrame

4. Carga las imágenes en un DataFrame utilizando la función "imageSchema.readImages".

### Visualizar las imágenes

5. Utiliza la función "show" para visualizar las imágenes y asegurarte de que se hayan cargado correctamente.

### Agregar etiquetas al DataFrame

6. Utiliza la función "withColumn" para agregar una columna al DataFrame con la etiqueta correspondiente a cada imagen.

### Dividir el DataFrame en conjuntos de entrenamiento y prueba

7. Divide el DataFrame en conjuntos de entrenamiento y prueba utilizando la función "randomSplit".

### Crear un vector de características para cada imagen

8. Utiliza la función "ml.feature" para crear un vector de características para cada imagen.

### Entrenar un modelo de aprendizaje automático

9. Utiliza un modelo de aprendizaje automático (como Random Forest) para entrenar el modelo utilizando el conjunto de entrenamiento.

### Predecir la categoría de las imágenes del conjunto de prueba

10. Utiliza el modelo entrenado para predecir la categoría de las imágenes del conjunto de prueba.

### Evaluar la precisión del modelo

11. Utiliza la función "multiclassClassificationEvaluator" para evaluar la precisión del modelo.

Este proyecto te permitirá trabajar con técnicas de aprendizaje automático y visión por computadora utilizando PySpark. Es un proyecto más avanzado, pero muy interesante. ¡Diviértete!



