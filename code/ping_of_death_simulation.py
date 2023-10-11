import socket
import time

def simulate_large_icmp_packet(target_ip, packet_size=70000, duration=10):
    """
    Simulates sending a large ICMP packet in a loop for a specified duration.
    
    Args:
    - target_ip (str): The target IP address.
    - packet_size (int, optional): The size of the ICMP packet. Default is 70000 bytes.
    - duration (int, optional): The duration in seconds for which the simulation runs. Default is 10 seconds.
    """
    
    print(f"Attempting to create an ICMP packet of size {packet_size} bytes to {target_ip}...")
    
    if packet_size > 65535:
        print("Warning: The specified packet size exceeds the standard limit of 65535 bytes for ICMP.")
        print("In a real-world scenario, this could lead to buffer overflows and potential system crashes.")
    
    # Create a dummy packet of the specified size
    packet = b'O' * packet_size
    
    print(f"Starting simulation for {duration} seconds...")
    
    start_time = time.time()
    packet_count = 0
    
    while time.time() - start_time < duration:
        # Simulate sending the packet
        packet_count += 1
        print(f"Simulated sending packet {packet_count} to {target_ip}...")
        time.sleep(1)  # Pause for a second between packets for readability
    
    print(f"Simulation complete. Sent a total of {packet_count} packets.")
    print("In a real-world scenario, the target system might become unresponsive or crash if it cannot handle the continuous stream of oversized packets.")

def main():
    """
    Main function to interact with the user and gather input for the simulation.
    """
    
    # Get target IP from the user
    target_ip = input("Enter the target IP address: ")
    
    # Validate IP address format
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        print("Invalid IP address format.")
        return
    
    # Get packet size from the user
    try:
        packet_size = int(input("Enter the desired packet size (default is 70000 bytes): "))
    except ValueError:
        print("Invalid packet size. Using default value of 70000 bytes.")
        packet_size = 70000
    
    # Get simulation duration from the user
    try:
        duration = int(input("Enter the duration in seconds for the simulation (default is 10 seconds): "))
    except ValueError:
        print("Invalid duration. Using default value of 10 seconds.")
        duration = 10
    
    # Run the simulation
    simulate_large_icmp_packet(target_ip, packet_size, duration)

if __name__ == "__main__":
    main()
