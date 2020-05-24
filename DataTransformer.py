def lambda_handler(event, context):
    output_records = []
    for record in event["records"]:
        output_records.append({
            "recordId": record['recordId'],
            "result": "Ok",
            "data": record["data"] + "Cg==" ##'Cg==' makes sure one record per line
        })
    return { "records": output_records }

