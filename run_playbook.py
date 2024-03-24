import ansible_runner

# Run playbook
r = ansible_runner.run(private_data_dir='.', playbook='hello.yml')
print("Playbook Results: ", r.stats)
