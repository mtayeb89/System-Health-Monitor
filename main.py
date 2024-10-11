import psutil  # psutil library provides system and process utilities
import time  # time library is used to handle intervals

# Function to get CPU usage percentage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)  # Returns CPU usage as a percentage

# Function to get Memory usage percentage
def get_memory_usage():
    memory = psutil.virtual_memory()  # Get memory details
    return memory.percent  # Returns Memory usage as a percentage

# Function to get Disk usage percentage
def get_disk_usage():
    disk = psutil.disk_usage('/')  # Get disk usage for root directory '/'
    return disk.percent  # Returns Disk usage as a percentage

# Function to display system health information in a formatted way
def display_system_health():
    print(f"{'='*40}")  # Print separator line
    print(f"{'System Health Monitor':^40}")  # Print title centered within 40 characters
    print(f"{'='*40}")  # Print separator line
    print(f"CPU Usage: {get_cpu_usage()}%")  # Print CPU usage percentage
    print(f"Memory Usage: {get_memory_usage()}%")  # Print Memory usage percentage
    print(f"Disk Usage: {get_disk_usage()}%")  # Print Disk usage percentage
    print(f"{'='*40}")  # Print separator line

# Function to monitor system health continuously at a given interval
def monitor_system(interval=5):
    while True:  # Infinite loop to continuously monitor the system
        display_system_health()  # Call the function to display system health
        time.sleep(interval)  # Pause the execution for the given interval in seconds

# Main entry point of the program
if __name__ == "__main__":
    interval = int(input("Enter monitoring interval (seconds): "))  # Ask user for interval
    monitor_system(interval)  # Start monitoring with the given interval
