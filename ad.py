import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

min_value = config['thresholds']['min']
max_value = config['thresholds']['max']

if min_value > 0 or max_value < 0:
    raise ValueError("Threshold values must include zero.")

print(f"Threshold values set from {min_value} to {max_value}")
