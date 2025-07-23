# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 2 - Data Processing
# MAGIC 
# MAGIC This notebook runs after Notebook 1 to demonstrate sequential workflow.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Processing
# MAGIC 
# MAGIC Here we process the data from the previous notebook.

# COMMAND ----------

# Create a sample dataframe
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data, ["name", "value"])

# Display the dataframe
display(df)