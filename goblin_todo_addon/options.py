import json

# Load user options
with open('/data/options.json') as f:
    opts = json.load(f)
username = opts.get('username')
password = opts.get('password')
