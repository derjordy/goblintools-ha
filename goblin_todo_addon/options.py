import json
with open('/data/options.json', 'r') as f:
    opts = json.load(f)
username = opts.get('username')
password = opts.get('password')
