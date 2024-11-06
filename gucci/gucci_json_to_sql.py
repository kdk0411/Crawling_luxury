import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, DecimalType

spark_home = os.getenv('SPARK_HOME')

spark = SparkSession.builder \
	.appName('JsonToMysql') \
	.config('spark.home', spark_home) \
	.config('spark.jars', r"D:\mysql-connector-j-9.1.0\mysql-connector-j-9.1.0.jar") \
	.getOrCreate()

json_files = ['gucci_raw_data/gucci_man.json', 'gucci_raw_data/gucci_women.json']

schema = StructType([
	StructField("category", StringType(), True),
	StructField("name", StringType(), True),
	StructField("href", StringType(), True),
	StructField("price", DecimalType(10, 2), True),
	StructField("img_url", StringType(), True)
])

all_data = spark.createDataFrame([], schema=schema)

for json_file in json_files:
	json_data = spark.read.json(json_file)

	for category in json_data.columns:
		category_df = json_data.select(F.col(category).alias('products')).withColumn('category', F.lit(category))
		expanded_df = category_df.select(
			F.explode('products').alias('product')
		).select(
			'category',
			'product.name',
			'product.href',
			'product.price',
			'product.img_url'
		)

		all_data = all_data.union(expanded_df)

mysql_url = 'jdbc:mysql://localhost/lotto' # 실제 호스트와 DB Name으로 변경
mysql_properties = {
	'user': 'root',
	'password': 'urface0411',
	'driver': 'com.mysql.cj.jdbc.Driver' # MySQL JDBC Driver -> ?
}

all_data.write \
	.jdbc(url=mysql_url, table='gucci_product', mode='overwrite', properties=mysql_properties)

spark.stop()
