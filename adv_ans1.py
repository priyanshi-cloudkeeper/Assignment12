import boto3
import csv

def types():
    ec2_client = boto3.client('ec2', region_name='ap-south-1')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    csv_file = 'ec2_instance_types.csv'
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['region', 'instance_type'])
        
        for region in regions:
            print("Fetching instance types for region:", region)
            ec2 = boto3.client('ec2', region_name=region)
            
            instance_types = set()
            response = ec2.describe_instance_types()

            for itype in response['InstanceTypes']:
                instance_types.add(itype['InstanceType'])
            for itype in instance_types:
                writer.writerow([region, itype])
            

    print("Instance types have been written to", csv_file)

types()

