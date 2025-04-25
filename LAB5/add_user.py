#!/usr/bin/env python3
# filepath: c:\Users\4ujtr\OneDrive\RIT\NSSA220\LAB5\add_user.py

"""
Author: [Your Name]
Date: April 24, 2025
Description: Automates adding user accounts to a Linux system based on a CSV file.
"""

import os
import csv
import subprocess

def clear_terminal():
    """Clears the terminal screen."""
    os.system('clear')

def create_group(group_name):
    """Creates a group if it does not exist."""
    try:
        subprocess.run(['getent', 'group', group_name], check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        subprocess.run(['groupadd', group_name])

def add_user(username, group, home_dir, shell, password="password"):
    """Adds a user to the system."""
    try:
        subprocess.run(['useradd', '-m', '-d', home_dir, '-s', shell, '-g', group, username], check=True)
        subprocess.run(['echo', f'{username}:{password}'], shell=True, stdout=subprocess.PIPE)
        subprocess.run(['passwd', '--expire', username], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding user {username}: {e}")

def process_csv(file_path):
    """Processes the CSV file and adds users."""
    print("Adding new users to the system.")
    print("Please Note: The default password for new users is password.")
    print("For testing purposes. Change the password to 1$4pizz@.\n")

    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            usernames = set()
            for row in reader:
                try:
                    # Extract and validate fields
                    employee_id = row.get('EmployeeID', '').strip()
                    first_name = row.get('FirstName', '').strip()
                    last_name = row.get('LastName', '').strip()
                    department = row.get('Department', '').strip().lower()
                    group = row.get('Group', '').strip().lower()

                    if not employee_id or not first_name or not last_name or not department or not group:
                        raise ValueError("Missing required fields.")

                    # Generate unique username
                    base_username = f"{first_name[0].lower()}{last_name.lower()}"
                    username = base_username
                    counter = 1
                    while username in usernames:
                        username = f"{base_username}{counter}"
                        counter += 1
                    usernames.add(username)

                    # Create group if it doesn't exist
                    create_group(group)

                    # Determine home directory and shell
                    home_dir = f"/home/{department}/{username}"
                    shell = '/bin/csh' if group == 'office' else '/bin/bash'

                    # Add user
                    add_user(username, group, home_dir, shell)

                    # Display success message
                    print(f"Processing employee ID {employee_id:>8}. {username:>20} added to system.")

                except ValueError as e:
                    print(f"Processing employee ID {row.get('EmployeeID', 'Unknown'):>8}. Skipping record due to error: {e}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    clear_terminal()
    csv_file_path = "linux_users.csv"  # Update this path if necessary
    process_csv(csv_file_path)