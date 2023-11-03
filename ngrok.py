import os
import yaml
import subprocess

config_file_path = os.path.expanduser("~/.config/ngrok/ngrok.yml")

# Load and parse the YAML configuration file
with open(config_file_path, 'r') as file:
    config = yaml.safe_load(file)

# Check if the tunnels are already defined in the configuration
if 'tunnels' not in config:
    # Define the tunnels for the first time
    config['tunnels'] = {
        'first': {
            'addr': '',
            'proto': 'http'
        },
        'second': {
            'addr': '',
            'proto': 'http'
        }
    }

# Ask the user for the desired ports
first_tunnel_port = input("Enter the port for the first tunnel: ")
second_tunnel_port = input("Enter the port for the second tunnel: ")

# Update the ports in the configuration
config['tunnels']['first']['addr'] = int(first_tunnel_port)
config['tunnels']['second']['addr'] = int(second_tunnel_port)

# Save the updated configuration back to the file
with open(config_file_path, 'w') as file:
    yaml.safe_dump(config, file)

# Run the ngrok command
subprocess.run(["./ngrok", "start", "--all"])
