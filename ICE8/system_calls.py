import os
import re

os.system("ifconfig ens33 > result.txt")

with open("result.txt", "r") as file:
    output = file.read()

match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', output)
if match:
    IP_address = match.group(1)
    print("IP_address =", IP_address)
else:
    print("IP_address not found.")
