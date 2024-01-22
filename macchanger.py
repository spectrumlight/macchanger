import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

# Disable network interface
output, error = run_command("sudo ifconfig wlan0 down")
print("ifconfig wlan is down")
print(output.decode(), error.decode())

# Change MAC address
output, error = run_command("sudo macchanger -r wlan0")
print("macchanger -r output:")
print(output.decode(), error.decode())

# Enable network interface
output, error = run_command("sudo ifconfig wlan0 up")
print("ifconfig is up:") 
print(output.decode(), error.decode())

# Display current MAC address
output, error = run_command("sudo macchanger -s wlan0")
print("macchanger -s output:") 
print(output.decode(), error.decode())
