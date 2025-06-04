from scapy.all import sniff, get_if_list

def packet_handler(pkt):
    print(pkt.summary())  # You can customize this for detailed output

def start_sniffing():
    print("Available Interfaces:")
    interfaces = get_if_list()
    for i, iface in enumerate(interfaces):
        print(f"{i}: {iface}")
    
    try:
        choice = int(input("\nSelect interface number to sniff on: "))
        selected_iface = interfaces[choice]
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        return

    print(f"\n[*] Starting packet sniffing on: {selected_iface}")
    try:
        sniff(iface=selected_iface, prn=packet_handler, store=0)
    except PermissionError:
        print("Permission denied. Try running the script as Administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_sniffing()
