import json
with open('/data/options.yaml', 'r') as f:
    opts = yaml.safe_load(f)
username = opts.get("username")
password = opts.get("password")
