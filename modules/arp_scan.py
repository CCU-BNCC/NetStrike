from scapy.all import ARP, Ether, srp

target_ip = input("🌐 Enter Network Range (e.g. 192.168.1.0/24): ")
print("🔎 Scanning local devices...\n")

arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp

result = srp(packet, timeout=2, verbose=0)[0]

for sent, received in result:
    print(f"✅ IP: {received.psrc} | MAC: {received.hwsrc}")
