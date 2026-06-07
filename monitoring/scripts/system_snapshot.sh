#!/bin/bash

echo "===== System Snapshot ====="
echo

HOST=$(hostname)
NOW=$(date)
AVAILABLE_MEM=$(free -h | awk '/Mem:/ {print $7}')
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}')
LOAD_AVG=$(uptime | awk -F'load average:' '{print $2}')
UPTIME=$(uptime -p)
echo "Time: $NOW"
echo "Hostname: $HOST"
echo "Uptime: $UPTIME"
echo "Available Memory: $AVAILABLE_MEM"
echo "Load Average:$LOAD_AVG"
echo "Disk Usage: $DISK_USAGE"
