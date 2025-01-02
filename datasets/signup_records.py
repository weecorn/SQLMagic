import csv
import random
from faker import Faker

def generate_sample_data(file_name, num_rows):
    """
    Generate sample data for SQL exercises and save it to a CSV file.

    :param file_name: Name of the output CSV file
    :param num_rows: Number of rows of data to generate
    """
    # Initialize Faker
    fake = Faker()

    # Define the structure of the table
    headers = ["id", "name", "email", "signup_date", "is_active", "age"]

    # Generate data
    data = []
    for i in range(1, num_rows + 1):
        row = {
            "id": i,
            "name": fake.name(),
            "email": fake.email(),
            "signup_date": fake.date_between(start_date="-5y", end_date="today"),
            "is_active": random.choice([True, False]),
            "age": random.randint(18, 70),
        }
        data.append(row)

    # Write data to a CSV file
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"Sample data with {num_rows} rows saved to '{file_name}'.")

generate_sample_data("signup_records_1000.csv", 1000)

