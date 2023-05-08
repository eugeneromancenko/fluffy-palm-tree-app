from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

@app.route("/")
def hello():
    """
    Display a 'Timestamp' message.
    """
    return "Timestamp app Ver1"

# Insert a timestamp into DynamoDB
@app.route('/timestamp', methods=['POST'])
def insert_timestamp():
    # Get the timestamp from the request body
    timestamp = request.json['timestamp']

    # Insert the timestamp into DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('timestamps')
    response = table.put_item(
        Item={
            'timestamp': timestamp
        }
    )

    return jsonify(response)

# List all timestamps from DynamoDB
@app.route('/list')
def list_timestamps():
    # Get all items from DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('timestamps')
    response = table.scan()

    # Extract the timestamps from the response
    timestamps = [item['timestamp'] for item in response['Items']]

    return jsonify(timestamps)

if __name__ == '__main__':
    app.run()
