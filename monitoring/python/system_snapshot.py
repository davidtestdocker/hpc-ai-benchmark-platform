#!/usr/bin/env python3

import socket
import json
from datetime import datetime, timezone
import shutil
import os

class SystemSnapshot:

    def get_mem_available(self) -> str:
        with open("/proc/meminfo", "r") as file:
            for line in file:
                if line.startswith("MemAvailable:"):
                    return line.split()[1] + " kB"

        return "unknown"

    def get_load_average(self) -> str:
        with open("/proc/loadavg", "r") as file:
            data = file.read().split()

        return f"{data[0]}, {data[1]}, {data[2]}"
  
    def get_disk_usage(self) -> str:
        total, used, free = shutil.disk_usage("/")

        percent = round((used / total) * 100)

        return f"{percent}%"

    def get_disk_status(self) -> str:
        disk_usage = self.get_disk_usage()
        disk_num = int(disk_usage.replace("%", ""))

        if disk_num > 80:
            return "WARNING"

        return "OK"
    def get_cpu_count(self) -> int:
        return os.cpu_count()
    
snapshot = SystemSnapshot()
load_average = snapshot.get_load_average()
hostname = socket.gethostname()
now = datetime.now(timezone.utc)
mem_available = snapshot.get_mem_available()
disk_usage =snapshot.get_disk_usage()
disk_status = snapshot.get_disk_status()
cpu_count = snapshot.get_cpu_count()

snapshot = {
    "time": str(now),
    "hostname": hostname,
    "memory_available": mem_available,
    "load_average": load_average,
    "disk_usage": disk_usage,
    "disk_status": disk_status,
    "cpu_count": cpu_count
}

with open("/root/hpc-ai-benchmark-platform/reports/system_snapshot.json", "w") as file:
    json.dump(snapshot, file, indent=4)
