# SSH Hardening

## Overview
Hardened SSH access on Ubuntu Server to eliminate password-based authentication
and reduce attack surface.

## Configuration Changes
- Disabled password authentication (PasswordAuthentication no)
- SSH access restricted to high port
- Root login disabled
- Key-based authentication enforced using ED25519 keys

## Tools Used
- OpenSSH
- UFW (Uncomplicated Firewall)
- Fail2ban

## Fail2ban Configuration
- Max retries: 5
- Find time: 30 minutes
- Ban time: 24 hours
- Monitoring ports: 22, high port

## Lessons Learned
- Always add firewall rules before deleting old ones
- Test new SSH key login before disabling password auth
- Keep an active session open when making SSH config changes
