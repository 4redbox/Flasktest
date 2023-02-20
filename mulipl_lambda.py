import json

def lambda_handler(event, context):
    # Extract input data from the event
    input_data = json.loads(event['body'])

    # Process the input data
    output_data = {'result': input_data['value'] * 2}

    # Return the output data as JSON
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(output_data)
    }
