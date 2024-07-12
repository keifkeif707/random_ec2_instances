import random
import string

def get_user_input():
    num_instances = int(input("Enter the number of EC2 instances: "))
    department_name = input("Enter the department name: ")
    return num_instances, department_name

def generate_unique_name(department_name, length=8):
    characters = string.ascii_letters + string.digits
    random_part = ''.join(random.choice(characters) for _ in range(length))
    return f"{department_name}-{random_part}"

def main():
    num_instances, department_name = get_user_input()
    for _ in range(num_instances):
        unique_name = generate_unique_name(department_name)
        print(unique_name)

if __name__ == "__main__":
    main()
