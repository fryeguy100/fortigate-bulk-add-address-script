# fortigate-bulk-add-script
Fortigate Bulk Adding Address Objects

Overview:

This Python script automates the process of adding multiple address objects to a FortiGate firewall configuration. The script reads a list of CIDR notation IP address blocks from an input file and converts them into FortiGate CLI commands, which are then written to an output file. The output can be directly used to configure a FortiGate firewall.

Features:

Converts CIDR notation to subnet mask
Creates CLI commands for adding each IP address block
Generates an output file that can be used directly in FortiGate CLI
Adds config firewall address and end statements to the output file

Prerequisites:

Python 3.x
ipaddress module (built into Python's standard library)

Usage:

1) Clone the repository or download the script.
2) Modify the input_file and output_file variables in the script to specify your input and output file paths.

input_file = "path/to/your/fortigate-cidr-bulk-add-input.txt"
output_file = "path/to/your/fortigate-cidr-bulk-output.txt"

3) Ensure your input file contains CIDR notation IP address blocks, one per line.

Example:
192.168.1.0/24
10.0.0.0/16

4) Run the script.

python your_script_name.py

5) The output file will contain the CLI commands needed to add these address objects to a FortiGate firewall.
   
Example Output

config firewall address
edit "192.168.1.0/24"
set subnet 192.168.1.0 255.255.255.0
next
edit "10.0.0.0/16"
set subnet 10.0.0.0 255.255.0.0
next
end

Contributing:
Feel free to open issues or pull requests if you have suggestions for improvements or bug fixes.

