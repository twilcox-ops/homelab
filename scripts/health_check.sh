#!/bin/bash

echo " Homelab Health Check "
echo "Date: $(date)"
echo ""

echo "--- Service Status ---"
for service in fail2ban opensearch opensearch-dashboards; do
    status=$(systemctl is-active $service)
    echo "$service: $status"
done

echo ""
echo "--- Disk Usage ---"
df -h / | tail -1

echo ""
echo "--- Memory Usage ----"
free -h | grep Mem

echo ""
echo "--- Last 5 Failed SSH Logins ---"
journalctl _SYSTEMD_UNIT=sshd.service | grep "Failed" | tail -5

echo ""
echo "=== Done ==="
