import psutil

def get_cpu_physical_cores():
    return psutil.cpu_count(logical=False)

def get_cpu_logical_cores():
    return psutil.cpu_count(logical=True)

def get_max_cpu_frequency():
    cpufreq = psutil.cpu_freq()
    return cpufreq.max

def get_min_cpu_frequency():
    cpufreq = psutil.cpu_freq()
    return cpufreq.min

def get_current_cpu_frequency():
    cpufreq = psutil.cpu_freq()
    return cpufreq.current

def get_cpu_usage_per_core():
    return psutil.cpu_percent(percpu=True, interval=1)

def get_total_cpu_usage():
    return psutil.cpu_percent()

if __name__ == "__main__":
    print("Number of physical CPU cores:", get_cpu_physical_cores())
    print("Number of logical CPU cores:", get_cpu_logical_cores())
    print("Max CPU Frequency (MHz):", get_max_cpu_frequency())
    print("Min CPU Frequency (MHz):", get_min_cpu_frequency())
    print("Current CPU Frequency (MHz):", get_current_cpu_frequency())
    print("CPU Usage Per Core:", get_cpu_usage_per_core())
    print("Total CPU Usage:", get_total_cpu_usage())