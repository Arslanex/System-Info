import GPUtil

def get_gpu_temperature():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].temperature
    except Exception:
        pass
    return None

def get_gpu_memory_used():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].memoryUsed
    except Exception:
        pass
    return None

def get_gpu_load():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].load * 100
    except Exception:
        pass
    return None

if __name__ == "__main__":
    print("GPU Temperature (°C):", get_gpu_temperature())
    print("GPU Memory Used (MB):", get_gpu_memory_used())
    print("GPU Load (%):", get_gpu_load())