import ipaddress
import os

def cidr_to_mask(cidr):
    network = ipaddress.IPv4Network(f'0.0.0.0/{cidr}', strict=False)
    return str(network.netmask)

# Replace with the path to your input file on your desktop
input_file = "/path/to/input/file/fortigate-cidr-bulk-add-input.txt"

# Replace with the path to your output file on your desktop
output_file = "/path/to/output/file/fortigate-cidr-bulk-add-input.txt"

# Remove the old output file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

# Open files and process each line
with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
    for line in infile:
        ip, cidr = line.strip().split('/')
        mask = cidr_to_mask(cidr)

        outfile.write(f'edit "{ip}/{cidr}"\n')
        outfile.write(f'set subnet {ip} {mask}\n')
        outfile.write('next\n')
    

