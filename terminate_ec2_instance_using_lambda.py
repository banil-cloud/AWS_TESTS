import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    terminated_instance_ids = []

    # Describe instances with the specified tag
    instances = ec2.describe_instances(Filters=[
        {'Name': 'tag:termination', 'Values': ['true']}
    ])

    # Terminate instances
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2.terminate_instances(InstanceIds=[instance_id])
            terminated_instance_ids.append(instance_id)
            print(f'Terminated instance: {instance_id}')

    return {
        'statusCode': 200,
        'body': f'Instances terminated successfully: {terminated_instance_ids}'
    }
