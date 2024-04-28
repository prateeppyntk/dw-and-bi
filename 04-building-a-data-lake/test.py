from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("GCS Example") \
    .getOrCreate()

# Set Google Cloud Storage credentials
spark._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
spark._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")

# Set your GCS credentials (replace 'YOUR_CREDENTIALS_FILE.json' with your actual JSON file)
spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile", "YOUR_CREDENTIALS_FILE.json")

# Set GCS bucket name and path to your data file
bucket_name = "your_bucket_name"
file_path = "gs://{}/path/to/your/file.csv".format(bucket_name)

# Read data from GCS into a PySpark DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show the DataFrame
df.show()

# Stop SparkSession
spark.stop()
