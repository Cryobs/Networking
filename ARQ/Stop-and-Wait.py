import random
import time

def sender(packets):
    for seq, packet in enumerate(packets):
        print(f"[SENDER] Sending packet #{seq}: packet")
        ack = receiver(packet, seq)
        if ack:
            print(f"[SENDER] ACK received for packet #{seq}")
        else:
            print(f"[SENDER] Timeout, resending packet #{seq}")
            ack = receiver(packet, seq)
        time.sleep(1)


def receiver(packet, seq):
    if random.random() < 0.8: # 80%
        print(f"    [RECEIVER] Received packet #{seq}: {packet}")
        return True 
    else:
        print(f"    [RECEIVER] Packet #{seq} lost")
        return False

packets = ["Hello", "This", "Is", "ARQ", "Test"]
sender(packets)
