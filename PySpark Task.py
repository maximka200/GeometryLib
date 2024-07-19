from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

# SparkSession init
spark = SparkSession.builder \
    .appName("ProductCategoryPairs") \
    .getOrCreate()

# Ваши продукты:
products_data = [
    (1, "Масло"),
    (2, "Молоко"),
    (3, "Кефир"),
    (4, "Шоколад"),
    (5, "Cгущенка"),
    (6, "Хлеб")
]

#Ваши категории:
categories_data = [
    (1, "Молочные"),
    (2, "Сладости"),
]

# Их связь (Номер продукта, Номер категории):
product_category_data = [
    (1, 1), 
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 1), 
    (5, 2),
]

# Создаем DataFram-ы:
products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

# Обьединяем:
product_category_pairs = products_df.join(product_category_df, "product_id", "left") \
    .join(categories_df, "category_id", "left") \
    .select("product_name", "category_name")

products_without_categories = products_df.join(product_category_df, "product_id", "left_anti") \
    .select("product_name")

# Вывод результата:
print("All couples:")
product_category_pairs.show()
print("Without category:")
products_without_categories.show()

# SparkSession close
spark.stop()