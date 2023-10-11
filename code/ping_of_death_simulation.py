import socket
import time

def introduction():
    """Provides a brief introduction to the 'Ping of Death' attack."""
    print("Welcome to the 'Ping of Death' attack simulation!")
    print("\nThe 'Ping of Death' attack involves sending oversized ICMP packets to a target system.")
    print("Historically, some systems were unable to handle these oversized packets, leading to buffer overflows and system crashes.")
    print("This simulation will demonstrate the concept of the attack without causing actual harm.\n")

def choose_mode():
    """Allows the user to choose a simulation mode."""
    print("Choose a mode of simulation:")
    print("1. Single Packet Mode: Send a single oversized packet.")
    print("2. Continuous Packet Mode: Send packets in a loop.")
    print("3. Safe Packet Mode: Send a packet of a typical size to demonstrate normal behavior.")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def feedback_on_packet_size(packet_size):
    """Provides feedback based on the chosen packet size."""
    if packet_size > 65535:
        print("\nWarning: The specified packet size exceeds the standard limit of 65535 bytes for ICMP.")
        print("In a real-world scenario, this could lead to buffer overflows and potential system crashes.")
    else:
        print("\nThe specified packet size is within the typical range for ICMP packets.")
        print("In most modern systems, this would not cause any issues.\n")

def potential_outcomes(mode, packet_size):
    """Displays potential outcomes based on the chosen mode and packet size."""
    if mode == "1" and packet_size > 65535:
        print("\nPotential Outcome: The target system might become unresponsive or crash due to the oversized packet.")
    elif mode == "2":
        print("\nPotential Outcome: Continuous sending of oversized packets might lead to sustained unresponsiveness or crashes.")
    else:
        print("\nPotential Outcome: The target system should handle the packet without any issues.")

def recommendations():
    """Provides recommendations on defending against the 'Ping of Death' attack."""
    print("\nRecommendations:")
    print("- Keep systems and software updated to ensure vulnerabilities are patched.")
    print("- Monitor network traffic for unusual patterns or sizes of ICMP packets.")
    print("- Implement network rules or firewalls to block or limit ICMP traffic if necessary.")
    print("- Educate network users about the risks and signs of potential attacks.\n")

def simulate_large_icmp_packet(target_ip, packet_size, mode):
    """Simulates sending ICMP packets based on the chosen mode and packet size."""
    packet = b'O' * packet_size
    packet_count = 0
    
    if mode == "1":
        packet_count += 1
        print(f"\nSimulated sending packet {packet_count} to {target_ip}...")
    
    elif mode == "2":
        duration = 10
        print(f"\nStarting continuous packet simulation for {duration} seconds...")
        start_time = time.time()
        while time.time() - start_time < duration:
            packet_count += 1
            print(f"Simulated sending packet {packet_count} to {target_ip}...")
            time.sleep(1)
    
    else:
        packet_count += 1
        print(f"\nSimulated sending safe packet {packet_count} to {target_ip}...")

    print("\nSimulation complete.")

def main():
    """Main function to guide the user through the simulation."""
    introduction()
    
    mode = choose_mode()
    
    target_ip = input("\nEnter the target IP address: ")
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        print("Invalid IP address format.")
        return
    
    if mode in ["1", "2"]:
        try:
            packet_size = int(input("Enter the desired packet size (default is 70000 bytes): "))
        except ValueError:
            print("Invalid packet size. Using default value of 70000 bytes.")
            packet_size = 70000
    else:
        packet_size = 1400  # Typical size for a safe ICMP packet
    
    feedback_on_packet_size(packet_size)
    simulate_large_icmp_packet(target_ip, packet_size, mode)
    potential_outcomes(mode, packet_size)
    recommendations()

if __name__ == "__main__":
    main()
