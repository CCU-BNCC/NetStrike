import os

subnet = input("🌐 Enter Subnet (e.g. 192.168.1): ")

print(f"🔎 Scanning live hosts in {subnet}.0/24...\n")

for i in range(1, 255):
    ip = f"{subnet}.{i}"
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    if response == 0:
        print(f"✅ Host Alive: {ip}")
