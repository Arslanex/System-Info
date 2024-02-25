import psutil
import platform
import time


def get_operating_system_details():
    """
    Get details about the operating system.

    Returns:
        str: Operating system details.
    """
    os_details = platform.uname()
    return f"{os_details.system} {os_details.release} {os_details.version}"


def get_system_architecture():
    """
    Get the system architecture.

    Returns:
        str: System architecture.
    """
    return platform.architecture()[0]


def get_kernel_version():
    """
    Get the kernel version.

    Returns:
        str: Kernel version.
    """
    return platform.uname().version


def get_system_uptime():
    """
    Get the system uptime.

    Returns:
        float: System uptime in seconds.
    """
    return time.time() - psutil.boot_time()


def get_hardware_information():
    """
    Get hardware information.

    Returns:
        str: Hardware information.
    """
    try:
        cpu_info = platform.processor()
        memory_info = psutil.virtual_memory()
        return f"CPU: {cpu_info}\nRAM: {format_bytes(memory_info.total)}"
    except Exception as e:
        print(f"Error getting hardware information: {e}")
        return "N/A"


def get_battery_information():
    """
    Get information about the battery.

    Returns:
        str: Battery information.
    """
    try:
        battery = psutil.sensors_battery()
        if battery:
            return f"Battery: {battery.percent}% ({'Plugged In' if battery.power_plugged else 'Not Plugged In'})"
        else:
            return "Battery information not available"
    except Exception as e:
        print(f"Error getting battery information: {e}")
        return "N/A"


def get_network_interfaces():
    """
    Get details about network interfaces.

    Returns:
        list: List of dictionaries containing network interface details.
    """
    try:
        interfaces = psutil.net_if_addrs()
        interface_details = []
        for name, addresses in interfaces.items():
            details = {"Name": name}
            for addr in addresses:
                if addr.family == socket.AF_INET:
                    details["IPv4 Address"] = addr.address
            interface_details.append(details)
        return interface_details
    except Exception as e:
        print(f"Error getting network interfaces: {e}")
        return []


def get_user_information():
    """
    Get information about the current logged-in user.

    Returns:
        str: User information.
    """
    try:
        user = psutil.users()[0]
        return f"User: {user.name} (Terminal: {user.terminal})"
    except Exception as e:
        print(f"Error getting user information: {e}")
        return "N/A"


def format_bytes(bytes_value):
    """
    Format bytes into a human-readable format.

    Args:
        bytes_value (int): Value in bytes.

    Returns:
        str: Formatted string.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            break
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} {unit}"


def format_time(seconds):
    """
    Format seconds into a human-readable time.

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted string.
    """
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"


if __name__ == "__main__":
    # Example usage and demonstration
    os_details = get_operating_system_details()
    system_architecture = get_system_architecture()
    kernel_version = get_kernel_version()
    system_uptime = get_system_uptime()
    hardware_info = get_hardware_information()
    battery_info = get_battery_information()
    network_interfaces = get_network_interfaces()
    user_info = get_user_information()

    print("System Information:")
    print(f"Operating System: {os_details}")
    print(f"System Architecture: {system_architecture}")
    print(f"Kernel Version: {kernel_version}")
    print(f"System Uptime: {format_time(system_uptime)}")
    print(f"Hardware Information:\n{hardware_info}")
    print(f"{battery_info}")

    print("\nNetwork Interfaces:")
    for interface in network_interfaces:
        print(f"{interface['Name']}: {interface.get('IPv4 Address', 'N/A')}")

    print(f"\n{user_info}")
