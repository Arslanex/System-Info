import psutil
import time


def convert_bytes_to_gb(bytes_value):
    """
    Convert bytes to gigabytes.

    Args:
        bytes_value (int): Value in bytes.

    Returns:
        float: Value in gigabytes.
    """
    gb_value = bytes_value / (1024 ** 3)  # 1 GB = 1024^3 bytes
    return round(gb_value, 2)


def get_network_interfaces_info():
    """
    Get detailed information about network interfaces.

    Returns:
        list: A list containing dictionaries with information for each network interface.
    """
    network_interfaces_info = []

    try:
        interfaces = psutil.net_if_stats()
        for interface, stats in interfaces.items():
            interface_info = {
                "name": interface,
                "status": 'Up' if stats.isup else 'Down',
                "speed": stats.speed,
                "duplex": stats.duplex,
                "mtu": stats.mtu,
            }
            network_interfaces_info.append(interface_info)

    except Exception as e:
        print(f"Error getting network interfaces information: {e}")

    return network_interfaces_info


def get_bandwidth_usage():
    """
    Get current network bandwidth usage.

    Returns:
        dict: A dictionary containing network bandwidth usage information.
    """
    bandwidth_usage = {
        "sent": None,
        "received": None,
    }

    try:
        io_counters = psutil.net_io_counters()
        bandwidth_usage["sent"] = convert_bytes_to_gb(io_counters.bytes_sent)
        bandwidth_usage["received"] = convert_bytes_to_gb(io_counters.bytes_recv)

    except Exception as e:
        print(f"Error getting network bandwidth usage: {e}")

    return bandwidth_usage


def get_connection_status(remote_address="www.google.com", port=80):
    """
    Check the connection status to a remote address.

    Args:
        remote_address (str): Remote address to check connection status.
        port (int): Port to check the connection.

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        connection_status = psutil.net_if_stats().get(remote_address) is not None
    except Exception as e:
        print(f"Error checking connection status: {e}")
        connection_status = False

    return connection_status


def get_packets_sent_received():
    """
    Get the total number of packets sent and received.

    Returns:
        dict: A dictionary containing the number of packets sent and received.
    """
    packets_info = {
        "packets_sent": None,
        "packets_received": None,
    }

    try:
        io_counters = psutil.net_io_counters()
        packets_info["packets_sent"] = io_counters.packets_sent
        packets_info["packets_received"] = io_counters.packets_recv

    except Exception as e:
        print(f"Error getting packets sent/received information: {e}")

    return packets_info


def real_time_network_monitoring(interval=1, duration=10):
    """
    Perform real-time network monitoring.

    Args:
        interval (int): Time interval between measurements.
        duration (int): Total duration of monitoring.
    """
    end_time = time.time() + duration

    try:
        print("\nReal-time Network Monitoring:")
        print("{:<15} {:<10} {:<10} {:<10}".format("Interface", "Status", "Sent (GB)", "Received (GB)"))

        while time.time() < end_time:
            bandwidth_usage = get_bandwidth_usage()
            network_interfaces = get_network_interfaces_info()

            for interface in network_interfaces:
                print("{:<15} {:<10} {:<10} {:<10}".format(
                    interface['name'],
                    interface['status'],
                    bandwidth_usage['sent'],
                    bandwidth_usage['received']
                ))

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nReal-time network monitoring stopped.")


if __name__ == "__main__":
    # Example usage and demonstration
    network_interfaces_info = get_network_interfaces_info()
    print("\nNetwork Interfaces Information:")
    for interface in network_interfaces_info:
        print("\nName: {}".format(interface['name']))
        print("Status: {}".format(interface['status']))
        print("Speed: {} Mbps".format(interface['speed']))
        print("Duplex: {}".format(interface['duplex']))
        print("MTU: {}".format(interface['mtu']))

    bandwidth_usage = get_bandwidth_usage()
    print("\nBandwidth Usage:")
    print("Sent: {} GB".format(bandwidth_usage['sent']))
    print("Received: {} GB".format(bandwidth_usage['received']))

    connection_status = get_connection_status()
    print("\nConnection Status to www.google.com: {}".format('Connected' if connection_status else 'Disconnected'))

    packets_info = get_packets_sent_received()
    print("\nPackets Sent/Received:")
    print("Packets Sent: {}".format(packets_info['packets_sent']))
    print("Packets Received: {}".format(packets_info['packets_received']))

    # Uncomment the next line to enable real-time network monitoring
    # real_time_network_monitoring(interval=1, duration=10)
