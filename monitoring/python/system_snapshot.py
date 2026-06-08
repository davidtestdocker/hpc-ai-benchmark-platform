#!/usr/bin/env python3

import socket
import json
from datetime import datetime
import shutil


def get_mem_available() -> str:
    with open("/proc/meminfo", "r") as file:
        for line in file:
            if line.startswith("MemAvailable:"):
                return line.split()[1] + " kB"

    return "unknown"

def get_load_average() -> str:
    with open("/proc/loadavg", "r") as file:
        data = file.read().split()

    return f"{data[0]}, {data[1]}, {data[2]}"

def get_disk_usage() -> str:
    total, used, free = shutil.disk_usage("/")

    percent = round((used / total) * 100)

    return f"{percent}%"

def get_disk_status() -> str:
    disk_usage = get_disk_usage()
    disk_num = int(disk_usage.replace("%", ""))

    if disk_num > 80:
        return "WARNING"

    return "OK"

load_average = get_load_average()
hostname = socket.gethostname()
now = datetime.utcnow()
mem_available = get_mem_available()
disk_usage = get_disk_usage()
disk_status = get_disk_status()

snapshot = {
    "time": str(now),
    "hostname": hostname,
    "memory_available": mem_available,
    "load_average": load_average,
    "disk_usage": disk_usage,
    "disk_status": disk_status
}

with open("../../reports/system_snapshot.json", "w") as file:
    json.dump(snapshot, file, indent=4)
