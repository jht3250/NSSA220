#!/usr/bin/env python3
# filepath: c:\Users\4ujtr\OneDrive\RIT\NSSA220\LAB5\add_user.py
# Author: John Treon
# This script adds users to the system based on a CSV file input.

import os
import csv
import subprocess
import time
import re


def clear_terminal():
    os.system('clear')

def create_group(group_name):
    try:
        subprocess.run(['getent', 'group', group_name], check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        subprocess.run(['groupadd', group_name])

def add_user(username, group, home_dir, shell, password="password"):
    try:
        subprocess.run(['useradd', '-m', '-d', home_dir, '-s', shell, '-g', group, username], check=True)
        subprocess.run(['echo', f'{username}:{password}'], shell=True, stdout=subprocess.PIPE)
        subprocess.run(['passwd', '--expire', username], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding user {username}: {e}")

def process_csv(file_path):
    print("Adding new users to the system.")
    print("Please Note: The default password for new users is password.")
    print("For testing purhjnposes. Change the password to 1$4pizz@.\n")

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
                    print(f"Processing employee ID {employee_id:>8}.\t '\033[32m{username:>20}\033[0m' added to system.")
                    time.sleep(1)

                except ValueError as e:
                    print(f"Processing employee ID {row.get('EmployeeID', 'Unknown'):>8}.\t \033[31m Skipping record due to error: {e}\033[0m")
                    time.sleep(1)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    clear_terminal()
    csv_file_path = "linux_users.csv"  
    process_csv(csv_file_path)