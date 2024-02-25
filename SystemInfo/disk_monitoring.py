import psutil

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

def get_disk_info():
    """
    Get disk information including total, used, and free disk space for all disks.

    Returns:
        dict: A dictionary containing disk information.
    """
    total_disk_info = {
        "total": 0,
        "used": 0,
        "free": 0,
    }

    try:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            partition_info = psutil.disk_usage(partition.mountpoint)
            total_disk_info["total"] += partition_info.total
            total_disk_info["used"] += partition_info.used
            total_disk_info["free"] += partition_info.free

    except Exception as e:
        print(f"Error getting disk information: {e}")

    return total_disk_info

def get_disk_usage_percentage():
    """
    Get the current disk usage as a percentage for all disks.

    Returns:
        float: Current disk usage percentage.
    """
    try:
        disk_usage_percentage = psutil.disk_usage('/').percent
    except Exception as e:
        print(f"Error getting disk usage percentage: {e}")
        disk_usage_percentage = None

    return disk_usage_percentage

def get_individual_disk_info():
    """
    Get information about each individual disk.

    Returns:
        list: A list containing dictionaries with information for each disk.
    """
    individual_disk_info = []

    try:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            partition_info = psutil.disk_usage(partition.mountpoint)
            disk_info = {
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "total": convert_bytes_to_gb(partition_info.total),
                "used": convert_bytes_to_gb(partition_info.used),
                "free": convert_bytes_to_gb(partition_info.free),
            }
            individual_disk_info.append(disk_info)

    except Exception as e:
        print(f"Error getting individual disk information: {e}")

    return individual_disk_info

if __name__ == "__main__":
    # Example usage and demonstration
    total_disk_info = get_disk_info()
    print("Total Disk Information:")
    print(f"Total Disk Space: {convert_bytes_to_gb(total_disk_info['total'])} GB")
    print(f"Used Disk Space: {convert_bytes_to_gb(total_disk_info['used'])} GB")
    print(f"Free Disk Space: {convert_bytes_to_gb(total_disk_info['free'])} GB")

    disk_usage_percentage = get_disk_usage_percentage()
    if disk_usage_percentage is not None:
        print(f"\nCurrent Disk Usage: {disk_usage_percentage}%")

    individual_disk_info = get_individual_disk_info()
    if individual_disk_info:
        print("\nIndividual Disk Information:")
        for disk in individual_disk_info:
            print(f"\nDevice: {disk['device']}")
            print(f"Mountpoint: {disk['mountpoint']}")
            print(f"Total: {disk['total']} GB")
            print(f"Used: {disk['used']} GB")
            print(f"Free: {disk['free']} GB")
