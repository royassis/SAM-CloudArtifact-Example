import json, os

def handler(event, context):
    return {"statusCode": 200, "body": json.dumps("hello")}
