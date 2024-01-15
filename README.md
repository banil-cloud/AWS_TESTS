# AWS Lambda for EC2 Instance Management

This project demonstrates how to use AWS Lambda functions to create and terminate EC2 instances programmatically.

## Create EC2 Instance

### Lambda Function: CreateEC2Instance

#### Overview
This Lambda function uses Boto3, the AWS SDK for Python, to launch a new EC2 instance. It is triggered by a manual invocation or can be integrated into your workflow.

#### Configuration
Make sure to configure the following parameters in the Lambda function code:
- `instance_type`: The type of EC2 instance (e.g., "t2.micro").
- `ami_id`: The Amazon Machine Image (AMI) ID.
- `key_name`: The name of your key pair.
- `security_group_ids`: List of security group IDs.
- `subnet_id`: The ID of the subnet.

#### Execution
1. Deploy the Lambda function.
2. Test the function using the Lambda console.

## Terminate EC2 Instances

### Lambda Function: TerminateEC2Instances

#### Overview
This Lambda function terminates EC2 instances based on a specified tag. Instances with the tag `termination=true` will be terminated.

#### Configuration
Ensure that you configure the Lambda function code properly. No additional configuration is required unless you want to modify the termination condition.

#### Execution
1. Deploy the Lambda function.
2. Test the function using the Lambda console.

## Trigger (Optional)

If you want to automate the execution of the TerminateEC2Instances function, you can set up a trigger using CloudWatch Events to schedule it at specific intervals.

---

Feel free to reach out if you have any questions or issues!
