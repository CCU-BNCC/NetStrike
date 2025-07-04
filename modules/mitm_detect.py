from scapy.all import sniff, ARP

def detect_mitm(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        print(f"⚠️ Possible MITM Packet: {packet.psrc} => {packet.hwsrc}")

print("🔐 Monitoring ARP Packets...\n")
sniff(store=False, prn=detect_mitm)
