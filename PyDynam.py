from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')

def insert_item(table_name, item):
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=item)
    return response

@app.route('/insert', methods=['POST'])
def insert():
    # Extract the JSON input from the request
    input_json = request.get_json()
    table_name = input_json['table']
    item = input_json['item']
    
    # Insert the item into the table
    response = insert_item(table_name, item)
    
    # Return the response as a JSON string
    output_json = {'status': 'success', 'response': str(response)}
    return jsonify(output_json)
