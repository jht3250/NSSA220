import matplotlib.pyplot as plt
import pandas as pd
import os

# Define file paths
metrics_folder = "metrics"
apm_files = [f"APM{i}_metrics.csv" for i in range(1, 7)]
system_metrics_file = "system_metrics.csv"

# Define colors for APM metrics
apm_colors = {
    "APM1": "blue",
    "APM2": "black",
    "APM3": "red",
    "APM4": "green",
    "APM5": "yellow",
    "APM6": "cyan"
}

# Plot CPU utilization
plt.figure()
for apm_file, color in zip(apm_files, apm_colors.values()):
    data = pd.read_csv(os.path.join(metrics_folder, apm_file), header=None)
    plt.plot(data[0], data[1], label=apm_file.split("_")[0], color=color)
plt.title("CPU Utilization")
plt.xlabel("Time (s)")
plt.ylabel("CPU Utilization (%)")
plt.legend()
plt.savefig("cpu.png")
plt.close()

# Plot Memory utilization
plt.figure()
for apm_file, color in zip(apm_files, apm_colors.values()):
    data = pd.read_csv(os.path.join(metrics_folder, apm_file), header=None)
    plt.plot(data[0], data[2], label=apm_file.split("_")[0], color=color)
plt.title("Memory Utilization")
plt.xlabel("Time (s)")
plt.ylabel("Memory Utilization (%)")
plt.legend()
plt.savefig("memory.png")
plt.close()

# Plot Bandwidth utilization
system_data = pd.read_csv(os.path.join(metrics_folder, system_metrics_file), header=None)
plt.figure()
plt.plot(system_data[0], system_data[1], label="Incoming Bandwidth", color="blue")
plt.plot(system_data[0], system_data[2], label="Outgoing Bandwidth", color="orange")
plt.title("Bandwidth Utilization")
plt.xlabel("Time (s)")
plt.ylabel("Bandwidth (KB/s)")
plt.legend()
plt.savefig("bandwidth.png")
plt.close()

# Plot Hard disk access rates
plt.figure()
plt.plot(system_data[0], system_data[3], label="Disk Access Rate", color="green")
plt.title("Hard Disk Access Rates")
plt.xlabel("Time (s)")
plt.ylabel("Access Rate (ops/s)")
plt.legend()
plt.savefig("disk_access.png")
plt.close()

# Plot Hard disk utilization
plt.figure()
plt.plot(system_data[0], system_data[4], label="Disk Utilization", color="purple")
plt.title("Hard Disk Utilization")
plt.xlabel("Time (s)")
plt.ylabel("Disk Utilization (GB)")
plt.legend()
plt.savefig("disk_util.png")
plt.close()