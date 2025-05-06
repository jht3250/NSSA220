import sys

def read_md5_file(filepath):
    """Reads an MD5 file and returns a dictionary of hashes and their corresponding executable names."""
    md5_dict = {}
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                md5_dict[parts[0]] = parts[1]  # Swap hash and executable name
    return md5_dict

def main():
    if len(sys.argv) != 3:
        print("Usage: python Lab3_Task2.py <md5_original.txt> <md5_new.txt>")
        sys.exit(1)

    # Read both files into hashmaps
    original_md5s = read_md5_file(sys.argv[1])
    new_md5s = read_md5_file(sys.argv[2])

    # Compare the hashmaps and print differences
    for original_md5, executable in original_md5s.items():
        if original_md5 in new_md5s:
            new_executable = new_md5s[original_md5]
            if executable != new_executable:
                print(f"{original_md5}: MD5 original = {executable}, MD5 new = {new_executable}")

if __name__ == "__main__":
    main()
