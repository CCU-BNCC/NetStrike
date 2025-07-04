from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("🔎 Starting packet sniffing... (Press Ctrl+C to stop)\n")
sniff(prn=packet_callback, count=50)
