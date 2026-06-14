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
    
    # 產生整數的 memory，方便用判斷式
    def get_mem_available_kb(self) -> int:
        with open("/proc/meminfo", "r") as file:
            for line in file:
                if line.startswith("MemAvailable:"):
                    return int(line.split()[1])

        return 0
    
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
    def health_check(self) -> dict:

        disk_usage_text = self.get_disk_usage()
        disk_usage = int(
            disk_usage_text.replace("%", "")
        )

        load_average_text = self.get_load_average()
        load_average = float(
            load_average_text.split(",")[0]
        )

        cpu_count = self.get_cpu_count()

        mem_available = self.get_mem_available_kb()
        mem_available_text = self.get_mem_available()
        

        checks = {
            "disk": {
                "status": "ok",
                "value": disk_usage_text
            },
            "load": {
                "status": "ok",
                "value": str(load_average)
            },
            "memory": {
                "status": "ok",
                "value": mem_available_text
            }
        }

        if disk_usage > 80:
            checks["disk"]["status"] = "warning"

        if load_average > cpu_count * 2:
            checks["load"]["status"] = "warning"

        if mem_available < 1000000:
            checks["memory"]["status"] = "warning"

        if "warning" in checks.values():
            return {
                "status": "degraded",
                "checks": checks
            }

        return {
            "status": "healthy",
            "checks": checks
        }

snapshot = SystemSnapshot()

snapshot_data = snapshot.generate_snapshot()

with open("/root/hpc-ai-benchmark-platform/reports/system_snapshot.json", "w") as file:
    json.dump(snapshot_data, file, indent=4)
