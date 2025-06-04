# 🕵️ Packet Sniffer using Scapy

This is a simple Python script that utilizes the powerful **Scapy** library to sniff and display network packets in real time from a selected network interface.

## 🚀 Features

* Lists all available network interfaces.
* Allows the user to select an interface to monitor.
* Captures and displays packet summaries live.
* Minimal dependencies, easy to run.

## 🧾 Requirements

* Python 3.x
* Scapy

Install Scapy via pip:

```bash
pip install scapy
```

> ⚠️ **Important:** This script may require administrative privileges to access network interfaces. Run it as Administrator on Windows or with `sudo` on Linux/macOS.

## 📝 Usage

1. Save the script to a file, e.g., `packet_sniffer.py`.

2. Run the script:

   ```bash
   python packet_sniffer.py
   ```

3. Choose the interface number from the list shown.

4. Watch as packet summaries appear in real time.

## 🔒 Permissions

* On **Linux/macOS**: Run with `sudo`:

  ```bash
  sudo python packet_sniffer.py
  ```

* On **Windows**: Right-click the terminal and select **Run as Administrator** before executing the script.

## 🛠 Customization

You can modify the `packet_handler(pkt)` function to print detailed information, filter specific types of packets, or log data to a file:

```python
def packet_handler(pkt):
    if pkt.haslayer(TCP):
        print(pkt[TCP].summary())
```

## 📦 Example Output

```
Available Interfaces:
0: eth0
1: wlan0
2: lo

Select interface number to sniff on: 1

[*] Starting packet sniffing on: wlan0
Ether / IP / TCP 192.168.1.2:443 > 192.168.1.100:54321 S
Ether / IP / UDP 192.168.1.100:137 > 192.168.1.255:137
```
---
