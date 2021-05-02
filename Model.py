# %% Imports
from pyspark.sql import SparkSession
from pyspark import SparkContext,  SparkConf
from pyspark.sql.types import *
from pyspark.sql.functions import col
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.evaluation import RegressionEvaluator 
from pyspark.mllib.evaluation import RankingMetrics
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
#%% Main

def main(spark, sc):
      
    #spark configs
    sc.setLogLevel("OFF")
    spark.conf.set("spark.blacklist.enabled", "False")
    spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)
    
  
    #read in file
    file_path = ['hdfs:/user/zm2114/cf_train_new.parquet',
                 'hdfs:/user/zm2114/cf_validation.parquet',
                 'hdfs:/user/zm2114/cf_test.parquet']

    train = spark.read.parquet(file_path[0])    
    #val = spark.read.parquet(file_path[1]) 
    #test = spark.read.parquet(file_path[2]) 
    cols = ['user_id','track_id']
    train = train.drop(*cols)
    train = train.rdd
    train.show()



    # #Training#####################################################
    # als = ALS(rank = 3, maxIter=2, regParam=.001,userCol="userId", itemCol="trackId", ratingCol="count",
    #                 alpha = .99, implicitPrefs = True,coldStartStrategy="drop")
    # model = als.fit(val)
    # ##############################################################

    # #error########################################################
    # predictions = model.transform(test)
    # evaluator = pyspark.ml.evaluation.RankingEvaluator(metricName="meanAveragePrecision", labelCol="count",
    #                             predictionCol="prediction")
    # MAP = evaluator.evaluate(predictions)
    # ##############################################################

    # print('-----------------------------------------------')
    # print('-----------------------------------------------')
    # print("MAP = " + str(MAP))
    # print('-----------------------------------------------')
    # print('-----------------------------------------------')
    
    # print('')
    # print('')
    # print('')

    # print('-----------------------------------------------')
    # print('Generate top 10 movie recommendations for a specified set of users')
    # print('-----------------------------------------------')
    # users = test.select(als.getUserCol()).distinct().limit(3)
    # userSubsetRecs = model.recommendForUserSubset(users, 10)
    # userSubsetRecs.show(truncate=False)
    # print('-----------------------------------------------')
    # print('Generate top 10 user recommendations for a specified set of movies')
    # print('-----------------------------------------------') 
    # movies = test.select(als.getItemCol()).distinct().limit(3)
    # movieSubSetRecs = model.recommendForItemSubset(movies, 10)
    # movieSubSetRecs.show(truncate=False)
    
    
  
    
#%% Func call
if __name__ == "__main__":

    # Create the spark session object
    spark = SparkSession.builder.appName('Test').getOrCreate()
    sc = spark.sparkContext
    main(spark, sc)