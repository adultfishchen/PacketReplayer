from scapy.all import *

# 讀取 PCAP 文件
packets = rdpcap("YOUR_PACKETS_FILE")

'''
# 重送每一個封包
sendp(packets)

'''
# 重送10 times指定的封包

packet_to_replay = packets[REPLAYED_PACKET_NUMBER]  # Replay specific packet [No-1]

for i in range(10):   
    send(packet_to_replay)
    print(f"Resend the packet for the {i+1} time.")
    
    time.sleep(1)  

