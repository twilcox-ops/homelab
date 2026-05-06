#!/usr/bin/env python3


# A list of fake login events
events = [
    {
        "event_id": 4625,
        "username": "tom",
        "domain": "WORKGROUP",
        "ip": "10.0.0.55",
        "timestamp": "2025-12-04 14:33:21",
        "success": False
    },
    {
        "event_id": 4625,
        "username": "tom",
        "domain": "WORKGROUP",
        "ip": "10.0.0.55",
        "timestamp": "2025-12-04 14:34:02",
        "success": False
    },
    {
        "event_id": 4624,
        "username": "tom",
        "domain": "WORKGROUP",
        "ip": "10.0.0.55",
        "timestamp": "2025-12-04 14:35:10",
        "success": True
    },
    {
        "event_id": 4625,
        "username": "admin",
        "domain": "WORKGROUP",
        "ip": "10.0.0.99",
        "timestamp": "2025-12-04 14:40:50",
        "success": False
    },
    {
        "event_id": 4625,
        "username": "admin",
        "domain": "WORKGROUP",
        "ip": "10.0.0.99",
        "timestamp": "2025-12-04 14:41:12",
        "success": False
    },
    {
        "event_id": 4625,
        "username": "admin",
        "domain": "WORKGROUP",
        "ip": "10.0.0.99",
        "timestamp": "2025-12-04 14:41:45",
        "success": False
    },
]


# Threshold for failed logins from the same IP
THRESHOLD = 3

# Dictionary to count failures per IP
failed_logins_by_ip = {}

print("\nProcessing events...")
for event in events:
    event_id = event["event_id"]
    success = event["success"]
    ip = event["ip"]

    # Only worried/care about failed logons
    if event_id == 4625 and not success:
        if ip not in failed_logins_by_ip:
            failed_logins_by_ip[ip] = 0
        failed_logins_by_ip[ip] += 1

        print(f"Failed logon from {ip} at {event['timestamp']} (user={event['username']})")

# After processing, analyze counts
print("\n=== Failed Login Counts By IP ===")
for ip, count in failed_logins_by_ip.items():
    print(f"{ip}: {count} failed login(s)")

print("\n=== Possible Brute-Force Alerts ===")
for ip, count in failed_logins_by_ip.items():
    if count >= THRESHOLD:
        print(f" ALERT: {ip} has {count} failed logins (>= {THRESHOLD})")
    else:
        print(f"- {ip} is below threshold ({count}/{THRESHOLD})")

print("\nDone.")
