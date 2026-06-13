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

    def generate_snapshot(self) -> dict:
        return {
            "time": str(datetime.now(timezone.utc)),
            "hostname": socket.gethostname(),
            "memory_available": self.get_mem_available(),
            "load_average": self.get_load_average(),
            "disk_usage": self.get_disk_usage(),
            "disk_status": self.get_disk_status(),
            "cpu_count": self.get_cpu_count()
        }

snapshot = SystemSnapshot()

snapshot_data = snapshot.generate_snapshot()

with open("/root/hpc-ai-benchmark-platform/reports/system_snapshot.json", "w") as file:
    json.dump(snapshot_data, file, indent=4)
