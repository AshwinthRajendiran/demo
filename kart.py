from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# 1. Initialize Spark Session
spark = SparkSession.builder \
    .appName("ChurnPredictionLab") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR") # Hide unnecessary info logs

print("--- Spark Session Started ---\n")

# 2. Load Data (Creating a Mock Dataset for the Lab)
# In a real scenario, you would use: df = spark.read.csv("data.csv", header=True, inferSchema=True)
data = [
    (1, 0, 25, 100.5, "Yes"), # ID, Gender(0=M), Age, MonthlyBill, Churn
    (2, 1, 34, 50.0, "No"),
    (3, 0, 45, 120.2, "Yes"),
    (4, 1, 23, 30.5, "No"),
    (5, 1, 56, 45.0, "No"),
    (6, 0, 32, 90.0, "Yes"),
    (7, 1, 40, 85.5, "No"),
    (8, 0, 29, 110.0, "Yes"),
    (9, 1, 21, 25.0, "No"),
    (10, 0, 38, 95.5, "Yes")
]
columns = ["CustomerID", "Gender", "Age", "MonthlyBill", "Churn_Label"]
df = spark.createDataFrame(data, columns)

print("Sample Data:")
df.show(5)

# 3. Data Preprocessing & Feature Engineering
# Convert String Label (Yes/No) to Numerical (1.0/0.0)
indexer = StringIndexer(inputCol="Churn_Label", outputCol="label")
df_indexed = indexer.fit(df).transform(df)

# Combine features into a single vector column
assembler = VectorAssembler(
    inputCols=["Gender", "Age", "MonthlyBill"],
    outputCol="features"
)
output_data = assembler.transform(df_indexed)

# 4. Split the Data
# 70% Training, 30% Testing
train_data, test_data = output_data.randomSplit([0.7, 0.3], seed=42)

print(f"Training Set Count: {train_data.count()}")
print(f"Test Set Count: {test_data.count()}\n")

# 5. Train the Model (Logistic Regression)
lr = LogisticRegression(featuresCol="features", labelCol="label")
model = lr.fit(train_data)

# 6. Model Evaluation
predictions = model.transform(test_data)

print("Predictions (label vs prediction):")
predictions.select("features", "label", "prediction").show()

# Calculate Accuracy
evaluator = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="accuracy"
)
accuracy = evaluator.evaluate(predictions)

print("="*40)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("="*40)

# Stop the session
spark.stop()