#!/usr/bin/env python3
# filepath: c:\Users\4ujtr\OneDrive\RIT\NSSA220\LAB5\add_user.py

"""
Author: John Treon
Date: April 24, 2025
Description: Automates adding user accounts to a Linux system based on a CSV file input.
"""

import os
import csv
import time
import re


def clear_terminal():
    os.system('clear')


def create_group(group_name):
    group_check = os.system(f"getent group {group_name} > /dev/null 2>&1")
    if group_check != 0:  # Group does not exist
        os.system(f"groupadd {group_name} > /dev/null 2>&1")


def add_user(username, group, home_dir, shell, password="password"):
    try:
        os.system(f"useradd -m -d {home_dir} -s {shell} -g {group} {username} > /dev/null 2>&1")
        os.system(f"echo '{username}:{password}' | chpasswd > /dev/null 2>&1")
        os.system(f"passwd --expire {username} > /dev/null 2>&1")
    except Exception as e:
        print(f"Error adding user {username}: {e}")


def process_csv(file_path):
    print("Adding new users to the system.")
    print("Please Note: The default password for new users is \033[32m password\033[0m.")
    print("For testing purposes. Change the password to \033[32m 1$4pizz@\033[0m.\n")

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

                    missing_fields = []
                    if not employee_id:
                        missing_fields.append("EmployeeID")
                    if not first_name:
                        missing_fields.append("FirstName")
                    if not last_name:
                        missing_fields.append("LastName")
                    if not department:
                        missing_fields.append("Department")
                    if not group:
                        missing_fields.append("Group")
                    if group not in ['office', 'pubsafety']:
                        raise ValueError(f"Invalid group: {group}.")
                    if missing_fields:
                        raise ValueError(f"Missing required field(s): {', '.join(missing_fields)}")

                    # Generate unique username
                    base_username = f"{first_name[0].lower()}{last_name.lower()}"
                    username = base_username
                    username = re.sub(r"[^A-Za-z ]", "", username)
                    counter = 1
                    while username in usernames:
                        username = f"{base_username}{counter}"
                        counter += 1
                    usernames.add(username)

                    # Create group if it doesn't exist
                    create_group(group)

                    # Determine home directory and shell
                    home_dir = f"/home/{department}/{username}"
                    if group == 'office':  
                        shell = '/bin/csh'
                    else:
                        shell = '/bin/bash'

                    # Add user
                    add_user(username, group, home_dir, shell)

                    # Display success message
                    print(f"Processing employee ID {employee_id:>8}.\t  \033[32m{username:>20}\033[0m added to system.\n")
                    time.sleep(1)

                except ValueError as e:
                    print(f"Processing employee ID {row.get('EmployeeID', 'Unknown'):>8}.\t\t \033[31m Skipping record due to error: {e}\033[0m\n")
                    time.sleep(1)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    clear_terminal()
    csv_file_path = "linux_users.csv"  # Update this path if necessary
    process_csv(csv_file_path)