import linux,aws,docker
import os

def execute_custom_command():
    command = input("Enter a custom command to execute: ")
    os.system(command)

def display_menu():
    os.system('clear')
    print("""
          Main menu
          Select options from following menu
          """)
    print("=======================================")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            linux.linux()

        elif choice == '2':
            aws.AWS()

        elif choice == '3':
            docker.docker()

        elif choice == '4':
            print("Exit")
            break

        else:
            print("Invalid choice!!!")

main()