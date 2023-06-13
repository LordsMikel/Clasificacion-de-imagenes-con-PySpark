from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import Pipeline
from pyspark.ml.image import ImageSchema
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType

# Crear una sesión de Spark
spark = SparkSession.builder.appName("Clasificación de imágenes con PySpark").getOrCreate()

# Cargar las imágenes en un DataFrame utilizando ImageSchema
df = ImageSchema.readImages("ruta/de/los/archivos/de/imagen/")

# Agregar una columna con la etiqueta de cada imagen
df = df.withColumn("label", when(df.origin.endswith("gato.jpg"), "gato")
                   .when(df.origin.endswith("perro.jpg"), "perro")
                   .otherwise("otro"))

# Definir las funciones UDF
def mean_intensity(image):
    # Esta función calcula la intensidad promedio de los píxeles en una imagen
    return float(image.array.flatten().mean())

def intensity_variance(image):
    # Esta función calcula la varianza de la intensidad de los píxeles en una imagen
    return float(image.array.flatten().var())

mean_intensity_udf = udf(mean_intensity, FloatType())
intensity_variance_udf = udf(intensity_variance, FloatType())

# Agregar las características de las imágenes al DataFrame
df = df.withColumn("mean_intensity", mean_intensity_udf(df["image"]))
df = df.withColumn("intensity_variance", intensity_variance_udf(df["image"]))

# Dividir el DataFrame en conjuntos de entrenamiento y prueba
train, test = df.randomSplit([0.8, 0.2])

# Crear un vector de características utilizando VectorAssembler
assembler = VectorAssembler(
    inputCols=["image.width", "image.height", "image.nChannels", "mean_intensity", "intensity_variance"],
    outputCol="features"
)
train = assembler.transform(train)
test = assembler.transform(test)

# Crear un modelo de Random Forest
rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=10)

# Crear un Pipeline para entrenar y evaluar el modelo
pipeline = Pipeline(stages=[rf])
model = pipeline.fit(train)
predictions = model.transform(test)

# Evaluar la precisión del modelo utilizando la función "MulticlassClassificationEvaluator"
evaluator = MulticlassClassificationEvaluator(predictionCol="prediction", labelCol="label", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Precisión del modelo: {:.2f}%".format(accuracy * 100))

# Cerrar la sesión de Spark
spark.stop()
