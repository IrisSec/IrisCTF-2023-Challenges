with open("nginx.yaml.base", "r") as f:
    base = f.read()

import json
with open("ports.json", "r") as f:
    ports = json.load(f)

data1 = "\n".join(f"  {port}: \"default/{challenge}:1337\"" for challenge, port in ports.items())
ports = {k.replace("_", "-") : v for k, v in ports.items()}
data2 = "\n".join(f"  - appProtocol: tcp\n    name: {challenge}\n    port: {port}\n    protocol: TCP\n    targetPort: {challenge}" for challenge, port in ports.items())
data3 = "\n".join(f"        - containerPort: {port}\n          name: {challenge}\n          protocol: TCP" for challenge, port in ports.items())

with open("nginx.yaml", "w") as f:
    f.write(base.replace("{data1}", data1).replace("{data2}", data2).replace("{data3}", data3))
