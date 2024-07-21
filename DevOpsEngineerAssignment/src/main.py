import boto3

def list_aws_resources():
    regions = boto3.session.Session().get_available_regions('ec2')
    for region in regions:
        ec2 = boto3.client('ec2', region_name=region)
        rds = boto3.client('rds', region_name=region)
        print(f"Resources in region: {region}")
        
        instances = ec2.describe_instances()
        print("EC2 Instances:")
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

        databases = rds.describe_db_instances()
        print("RDS Instances:")
        for db in databases['DBInstances']:
            print(f"DB Instance ID: {db['DBInstanceIdentifier']}, Status: {db['DBInstanceStatus']}")

def main():
    list_aws_resources()

if __name__ == "__main__":
    main()
