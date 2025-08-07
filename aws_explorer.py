import boto3

# This script lists all available AWS regions and prints the submission details.

def list_aws_regions():
    """
    Lists all available AWS regions using the boto3 library.
    """
    try:
        # Use a low-impact service like 'ec2' to get a list of all regions.
        # This works even if the IAM user has minimal permissions.
        ec2_client = boto3.client('ec2', region_name='us-east-1')
        response = ec2_client.describe_regions()
        regions = [region['RegionName'] for region in response['Regions']]
        print("Successfully connected to AWS!")
        print("Available AWS Regions:")
        for region in sorted(regions):
            print(f"- {region}")
        return True
    except Exception as e:
        print("An error occurred while trying to connect to AWS or list regions.")
        print(f"Error: {e}")
        return False

def main():
    """
    Main function to execute the script and print the required output.
    """
    # Replace 'your_muid' with your actual MUID from µLearn.
    your_muid = "lezinvm@mulearn" 

    if list_aws_regions():
        print("\n--- Submission Details ---")
        print(f'{{"submitted_by": "{your_muid}"}}')
    else:
        print("\nScript failed to execute. Please check your AWS credentials and permissions.")

if __name__ == "__main__":
    main()

