import datetime
import boto3
import subprocess
import sys
import json
def install(package):
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "--target",
        "/tmp",
        package])
install('yfinance')
sys.path.append('/tmp')
import yfinance

def lambda_handler(event, context):

    '''get the data for STOCK from time start to end at each minute
    '''
    STOCK = ['FB', 'SHOP', 'BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DDOG']
    time1 = datetime.datetime(2020,5,14,0,0,0)
    time2 = datetime.datetime(2020,5,14,23,0,0)
    data = []
    fh = boto3.client( "firehose" , region_name="us-east-2" ) # initialize boto3 client

    for item in STOCK:
        record = yfinance.Ticker(item)
        hist   = record.history(interval = '1m', start=time1, end=time2)

        for time in hist.index:
            temp = {
                'high':hist.loc[time].get('High'),
                'low': hist.loc[time].get('Low'),
                'ts': time.strftime('%Y/%m/%d %H:%M:%S'),
                'name': item
            }
            data.append(temp)
            # convert it to JSON
            as_jsonstr = json.dumps(temp)

            fh.put_record(
                DeliveryStreamName= "yfinance-data" ,
                Record={ "Data" : as_jsonstr.encode( 'utf-8' )}
                )
    return {
    'statusCode' : 200,
    'body' : json.dumps( f'Done! Recorded: {data}' )
    }
