import psutil
import platform
import time

def list_running_processes():
    """
    List information about running processes.

    Returns:
        list: List of dictionaries containing process details.
    """
    try:
        processes = []
        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'create_time']):
            processes.append({
                "PID": process.info['pid'],
                "Name": process.info['name'],
                "CPU Percent": process.info['cpu_percent'],
                "Memory Usage": format_bytes(process.info['memory_info'].rss),
                "Create Time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(process.info['create_time']))
            })
        return processes
    except Exception as e:
        print(f"Error listing running processes: {e}")
        return []

def process_resource_usage(pid):
    """
    Get resource usage (CPU, Memory) for a specific process.

    Args:
        pid (int): Process ID.

    Returns:
        dict: Dictionary containing resource usage details.
    """
    try:
        process = psutil.Process(pid)
        cpu_percent = process.cpu_percent(interval=1)
        memory_info = process.memory_info()
        return {
            "PID": pid,
            "CPU Percent": cpu_percent,
            "Memory Usage": format_bytes(memory_info.rss),
        }
    except Exception as e:
        print(f"Error getting resource usage for process {pid}: {e}")
        return {}

def terminate_process(pid):
    """
    Terminate a specific process.

    Args:
        pid (int): Process ID.
    """
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process {pid} terminated.")
    except Exception as e:
        print(f"Error terminating process {pid}: {e}")

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

if __name__ == "__main__":
    # Example usage and demonstration
    running_processes = list_running_processes()

    print("Running Processes:")
    for process in running_processes:
        print(f"PID: {process['PID']}, Name: {process['Name']}, CPU Percent: {process['CPU Percent']}, Memory Usage: {process['Memory Usage']}, Create Time: {process['Create Time']}")

    # Example: Get resource usage for a specific process
    if running_processes:
        pid_to_check = running_processes[0]['PID']
        resource_usage = process_resource_usage(pid_to_check)
        print(f"\nResource Usage for Process {pid_to_check}: {resource_usage}")

    # Example: Terminate a specific process
    if running_processes:
        pid_to_terminate = running_processes[0]['PID']
        terminate_process(pid_to_terminate)
