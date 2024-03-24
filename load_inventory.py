import ansible_runner
import yaml

# Load inventory as YAML
with open('hosts.yml', 'r') as file:
    inventory = yaml.safe_load(file)

# Print host names, IP addresses, and group names
for group, group_data in inventory.items():
    for host, host_data in group_data['hosts'].items():
        print(f"Host: {host}, IP: {host_data['ansible_host']}, Group: {group}")

# Ping all hosts
r = ansible_runner.run(private_data_dir='.', playbook='ping.yml')
print("Ping Results: ", r.stats)

