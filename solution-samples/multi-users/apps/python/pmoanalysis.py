from pyspark.sql import SparkSession, SQLContext
spark = SparkSession.builder.appName("project deadline").getOrCreate()
hconf = spark.sparkContext._jsc.hadoopConfiguration()
hconf.set("fs.cos.prj.iam.api.key", "CHANGEME")
hconf.set("fs.cos.prj.endpoint", "CHANGEME")
projects_df = spark.read.parquet("cos://pmobucket.prj/projectparquet/project.parquet" )
projects_df.show()
projects_df.printSchema()
projects_df.registerTempTable('projects')
sqlContext = SQLContext(spark.sparkContext)
sqlContext.sql('select VENDORNAME,   PROJECTCOST/EFFORT AS AVGCOST from projects ORDER BY AVGCOST').show()
