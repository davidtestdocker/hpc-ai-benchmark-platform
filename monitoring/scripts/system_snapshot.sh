#!/bin/bash

echo "===== System Snapshot ====="
echo

echo "Time:"
date

echo
echo "Hostname:"
hostname

echo
echo "Uptime:"
uptime

echo
echo "Memory:"
free -h

echo
echo "Disk:"
df -h /
