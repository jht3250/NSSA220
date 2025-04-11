#!/bin/bash

letter_writer() {
    local first_name=$1
    local dept_name=$2
    local job_title=$3
    local home_dir=$4

    cat <<EOL > "$home_dir/welcome.txt"
Dear $first_name,
Welcome to Initech Corporation! We're so happy to have you in the $dept_name Department as a $job_title. Please don't forget to complete your TPS Reports in a timely manner.
Sincerely,
Bill Lumbergh
EOL
}

file_system_writer() {
    local username=$1
    local home_dir="/home/$username"

    mkdir -p "$home_dir/Desktop" "$home_dir/Documents" "$home_dir/Downloads" "$home_dir/Pictures"
    cp /home/student/ackbar.jpg "$home_dir/Pictures/"
    letter_writer "$2" "$3" "$4" "$home_dir"
}

permission_editor() {
    local username=$1
    local home_dir="/home/$username"

    chown -R "$username:$username" "$home_dir"
    chmod 0777 "$home_dir/welcome.txt"
}

while true; do
    read -p "Username: " username
    read -p "Full Name: " full_name
    read -p "Department: " dept_name
    read -p "Job Title: " job_title

    useradd "$username"
    file_system_writer "$username" "$full_name" "$dept_name" "$job_title"
    permission_editor "$username"

    echo "User $username added!"
    read -p "Would you like to add another user? (y/n): " response
    if [[ "$response" != "y" ]]; then
        break
    fi
done
