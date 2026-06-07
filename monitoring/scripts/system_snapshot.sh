#!/bin/bash

echo "===== System Snapshot ====="
echo

HOST=$(hostname)
NOW=$(date)
AVAILABLE_MEM=$(free -h | awk '/Mem:/ {print $7}')
LOAD_AVG=$(uptime | awk -F'load average:' '{print $2}')
UPTIME=$(uptime -p)
DISK_NUM=$(df -h / | awk 'NR==2 {gsub("%","",$5); print $5}')
echo "Time: $NOW"
echo "Hostname: $HOST"
echo "Uptime: $UPTIME"
echo "Available Memory: $AVAILABLE_MEM"
echo "Load Average:$LOAD_AVG"

if [ "$DISK_NUM" -gt 80 ]; then
    DISK_STATUS="WARNING"
else
    DISK_STATUS="OK"
fi

echo "Disk Usage: ${DISK_NUM}%"
echo "Disk Status: $DISK_STATUS"
