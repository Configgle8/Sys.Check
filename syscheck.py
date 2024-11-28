import psutil
import time

def get_system_stats():
    """Fetch and print system stats like CPU, memory, and disk usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_info.percent}%")
    print(f"Available Memory: {memory_info.available / (1024 * 1024):.2f} MB")
    print(f"Disk Usage: {disk_usage.percent}%")
    print(f"Free Disk Space: {disk_usage.free / (1024 * 1024):.2f} MB")
    print("-" * 40)

if __name__ == "__main__":
    print("Starting System Monitor...")
    while True:
        get_system_stats()
        time.sleep(10) 
