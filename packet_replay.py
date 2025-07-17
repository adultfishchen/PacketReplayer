from scapy.all import *

# 讀取 PCAP 文件
packets = rdpcap("5.2.6.1_replay_a.pcapng")

'''
# 重送每一個封包
sendp(packets)

'''
# 重送10 times指定的封包

packet_to_replay = packets[42]  # Replay specific packet

for i in range(10):   
    send(packet_to_replay)
    print(f"Resend the packet for the {i+1} time.")
    
    time.sleep(1)  

