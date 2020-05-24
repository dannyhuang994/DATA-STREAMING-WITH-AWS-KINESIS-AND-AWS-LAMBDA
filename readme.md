## Streaming Stock Data with AWS Kinesis firehose and AWS lambda

In this project, we processed the data and then dumped it in a manner that facilitates querying and further analysis, either in real time or near real time capacity.

We first downloaded the data using [the Data-Collector lambda](https://github.com/dannyhuang994/DATA-STREAMING-WITH-AWS-KINESIS-AND-AWS-LAMBDA/blob/master/DataTransformer.py), and then the configured AWS Kinesis firehose with [the Transformer lambda](https://github.com/dannyhuang994/DATA-STREAMING-WITH-AWS-KINESIS-AND-AWS-LAMBDA/blob/master/DataTransformer.py) transformed the downloaded data and stored it into AWS S3 buckets.

The above process can be triggered by calling the [API gateway](https://b8mvv85tck.execute-api.us-east-2.amazonaws.com/default/DataCollector).

Finally, we perform simple [SQL queries](https://github.com/dannyhuang994/DATA-STREAMING-WITH-AWS-KINESIS-AND-AWS-LAMBDA/blob/master/query.sql) and save the results into [result.csv](https://github.com/dannyhuang994/DATA-STREAMING-WITH-AWS-KINESIS-AND-AWS-LAMBDA/blob/master/results.csv)

#### DataCollector Lambda configuration page

![img](https://github.com/dannyhuang994/DATA-STREAMING-WITH-AWS-KINESIS-AND-AWS-LAMBDA/blob/master/asset/DataCollector%20Lambda%20configuration%20page.png)

#### Kinesis Data Firehose Delivery Stream Monitoring

![img](https://github.com/dannyhuang994/DATA-STREAMING-WITH-AWS-KINESIS-AND-AWS-LAMBDA/blob/master/asset/Kinesis%20Data%20Firehose%20Delivery%20Stream%20Monitoring.png)


#### API Gateway of DataCollector
https://b8mvv85tck.execute-api.us-east-2.amazonaws.com/default/DataCollector

