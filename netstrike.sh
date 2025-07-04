#!/bin/bash

PASS="0801121221040201"

read -p "🔑 Enter Access Key: " key
if [ "$key" != "$PASS" ]; then
    echo "❌ Access Denied!"
    exit 1
fi

clear
cat banner.txt 2>/dev/null

while true; do
  echo ""
  echo "🎯 Choose Network Module:"
  echo "1. Port Scan"
  echo "2. Ping Sweep"
  echo "3. ARP Scan"
  echo "4. Packet Sniffer"
  echo "5. MITM Detector"
  echo "0. Exit"
  echo ""
  read -p "➤ Enter your choice: " choice

  case $choice in
    1) python3 modules/port_scan.py ;;
    2) python3 modules/ping_sweep.py ;;
    3) python3 modules/arp_scan.py ;;
    4) python3 modules/sniff.py ;;
    5) python3 modules/mitm_detect.py ;;
    0) echo "🔒 Exiting NetStrike..."; exit 0 ;;
    *) echo "❗ Invalid Option" ;;
  esac
done
