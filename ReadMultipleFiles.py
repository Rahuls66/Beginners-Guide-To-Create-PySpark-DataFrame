files = ['Fish.csv', 'Salary.csv']
df = spark.read.csv(files, sep = ',' ,  inferSchema=True, header=True)
