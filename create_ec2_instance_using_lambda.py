# Import the Boto3 library, the AWS SDK for Python
import boto3

# Lambda function handler
def lambda_handler(event, context):
    # Define EC2 instance parameters
    instance_type = "t2.micro"                     # Type of EC2 instance
    ami_id = "your_ami_id"                         # AMI ID for the instance
    key_name = "your_key_pair_name"                # Key pair name for SSH access
    security_group_ids = ["your_security_group_id"] # List of security group IDs
    subnet_id = "your_subnet_id"                   # Subnet ID for the instance

    # Initialize EC2 client using Boto3
    ec2 = boto3.client('ec2')

    # Launch EC2 instance
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=security_group_ids,
        SubnetId=subnet_id,
        MinCount=1,
        MaxCount=1
    )

    # Extract instance ID from the response
    instance_id = response['Instances'][0]['InstanceId']

    # Prepare the response to be returned by the Lambda function
    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance_id} launched successfully!'
    }
