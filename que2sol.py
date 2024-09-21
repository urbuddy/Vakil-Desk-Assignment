"""Python script that reads a CSV file with user data,
removes duplicate entries based on user_id,
filters out rows with invalid email formats,
and writes the cleaned data to a new CSV file."""
import csv
import re


def is_valid_email(email):
    """
    Function to validate email format
    :param email: email value to validate
    :return: Boolean value as True if email is valid or false if email invalid.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def clean_user_data(input_file, output_file):
    """
    Function to clean user data from CSV
    :param input_file: Input CSV file with user data
    :param output_file: Output CSV file for cleaned data
    :return: status check variable
    """
    unique_users = {}

    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        if 'user_id' not in fieldnames or 'email' not in fieldnames:
            print("CSV file must contain 'user_id' and 'email' columns.")
            return 0

        for row in reader:
            user_id = row['user_id']
            email = row['email']

            # Check for duplicate user_id and validate email
            if user_id not in unique_users and is_valid_email(email):
                unique_users[user_id] = row

    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_users.values())

    print(f"Cleaned data has been written to {output_file}")
    return 1


# Example
if __name__ == "__main__":
    input_file = 'input_users.csv'
    output_file = 'cleaned_users.csv'
    status = clean_user_data(input_file, output_file)

