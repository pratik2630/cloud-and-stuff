
import boto3
def AWS_menu():
    
    print("""
    AWS MENU
          
          1)EC2
          2)S3
          3)SNS
          4)Exit
    """)

def ec2():
    print("EC2")
    client = boto3.client('ec2')
    while True:
        print("""
          1) Create Instance:
          2) Display All instance:
          3) Delete instance:
          4) Exit
        """)

        ec2_choice = input("Enter option number:")

        if ec2_choice == '1':
                print("Enter following details to create instance")
                name  = input("Instance name:")
                imgId=input("Instace id:") #ami-0ded8326293d3201b
                instanceType = input("Instance Type:") #t2.micro
                min = int(input("Minimum count:")) #1
                max = int(input("Miximum count:")) #1

                response = client.run_instances(
                            ImageId=imgId,
                            InstanceType=instanceType,
                            MinCount=min,
                            MaxCount=max,
                            TagSpecifications=[{
                                 'ResourceType': 'instance',
                                 'Tags': [{
                                      'Key': 'Name',
                                      'Value': name
                                      },]
                                    },]
                                    )


        elif ec2_choice == '2':
                print("Display all instances")

        elif ec2_choice == '3':
                sns()

        elif ec2_choice == '4':
                print("Exit")
                break

        else:
                print("Invalid choice!!!")


def s3():
    print("S3")

def sns():
    print("sns")

def AWS():
    while True:
        AWS_menu()
        aws_choice=input("Enter your choice:")
        
        if aws_choice == '1':
            ec2()

        elif aws_choice == '2':
            s3()

        elif aws_choice == '3':
            sns()

        elif aws_choice == '4':
            print("Exit")
            break

        else:
            print("Invalid choice!!!")
