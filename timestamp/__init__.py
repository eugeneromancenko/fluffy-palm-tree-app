from flask import Flask, request, jsonify, render_template
import boto3
import os

def create_app():
    """
    Create and configure a Flask application instance.
    """
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        """
        Render the index page with buttons and a text field.
        """
        return render_template("index.html")

    @app.route('/timestamp', methods=['POST'])
    def insert_timestamp():
        # Get the timestamp from the request body
        timestamp = request.form['timestamp']

        # Insert the timestamp into DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('timestamps')
        response = table.put_item(
            Item={
                'timestamp': timestamp
            }
        )

        # Render the updated template with the response message
        message = f"Timestamp {timestamp} added successfully"
        return render_template('index.html', message=message)


    @app.route('/list')
    def list_timestamps():
        # Get all items from DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('timestamps')
        response = table.scan()

        # Extract the timestamps from the response
        timestamps = [item['timestamp'] for item in response['Items']]

        # Render the updated template with the list of timestamps
        return render_template('index.html', timestamps=timestamps)
        

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
