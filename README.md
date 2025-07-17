# Packet Replayer

This is an automated packet replay framework designed to test the effectiveness of network defense mechanisms against traffic replay attacks.

To use this tool effectively, you need to modify the configuration file to suit your environment or target system.  
For example, update placeholders, such as  `YOUR_PACKETS_FILE` and  `REPLAYED_PACKET_NUMBER` with actual values relevant to your replay scenario.

> ⚠️ **Note:** Avoid hardcoding sensitive credentials when sharing or storing modified files.

---

## Prerequisites

Before using this tool, ensure you have captured the target network traffic and saved it in `.pcap` or `.pcapng` format using a packet capture tool (e.g., Wireshark or tcpdump).
---

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/adultfishchen/PacketReplayer.git
   cd PacketReplayer
   ```
2. Modify the file
3. Run the Replayer：
   ```
   python3 packet_replay.py
   ```
---
Disclaimer
This tool is intended for authorized testing and research purposes only. Unauthorized usage against systems without permission is strictly prohibited.
