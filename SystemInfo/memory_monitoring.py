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

def get_memory_info():
    """
    Get memory information including total, used, and free memory.

    Returns:
        dict: A dictionary containing memory information.
    """
    memory_info = {
        "total": None,
        "used": None,
        "free": None,
    }

    try:
        virtual_memory = psutil.virtual_memory()
        memory_info["total"] = convert_bytes_to_gb(virtual_memory.total)
        memory_info["used"] = convert_bytes_to_gb(virtual_memory.used)
        memory_info["free"] = convert_bytes_to_gb(virtual_memory.free)
    except Exception as e:
        print(f"Error getting memory information: {e}")

    return memory_info

def get_memory_usage_percentage():
    """
    Get the current memory usage as a percentage.

    Returns:
        float: Current memory usage percentage.
    """
    try:
        memory_usage_percentage = psutil.virtual_memory().percent
    except Exception as e:
        print(f"Error getting memory usage percentage: {e}")
        memory_usage_percentage = None

    return memory_usage_percentage

def get_swap_space_info():
    """
    Get swap space information including total, used, and free swap space.

    Returns:
        dict: A dictionary containing swap space information.
    """
    swap_info = {
        "total": None,
        "used": None,
        "free": None,
    }

    try:
        swap_memory = psutil.swap_memory()
        swap_info["total"] = convert_bytes_to_gb(swap_memory.total)
        swap_info["used"] = convert_bytes_to_gb(swap_memory.used)
        swap_info["free"] = convert_bytes_to_gb(swap_memory.free)
    except Exception as e:
        print(f"Error getting swap space information: {e}")

    return swap_info

if __name__ == "__main__":
    # Example usage and demonstration
    memory_info = get_memory_info()
    print("Memory Information:")
    print(f"Total Memory: {memory_info['total']} GB")
    print(f"Used Memory: {memory_info['used']} GB")
    print(f"Free Memory: {memory_info['free']} GB")

    memory_usage_percentage = get_memory_usage_percentage()
    if memory_usage_percentage is not None:
        print(f"\nCurrent Memory Usage: {memory_usage_percentage}%")

    swap_info = get_swap_space_info()
    print("\nSwap Space Information:")
    print(f"Total Swap Space: {swap_info['total']} GB")
    print(f"Used Swap Space: {swap_info['used']} GB")
    print(f"Free Swap Space: {swap_info['free']} GB")
