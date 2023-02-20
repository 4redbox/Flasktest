import json

def lambda_handler(event, context):
    # Parse the JSON input
    input_json = json.loads(event['body'])
    input_value = input_json['input']
    
    # Process the input
    output_value = input_value * 2
    
    # Return the output as a JSON response
    response = {
        'statusCode': 200,
        'body': json.dumps({'output': output_value})
    }
    return response
