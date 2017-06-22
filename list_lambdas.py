import boto3

client = boto3.client('lambda')

functions = client.list_functions()
#print(functions)

print([f['FunctionName'] for f in functions.get('Functions', [])])
