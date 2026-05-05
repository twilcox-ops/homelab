# UFW Firewall Configuration

## Overview
Configured UFW firewall on Ubuntu Server to restrict access to internal
network only. No services are exposed to the internet.

## Rules
- SSH (port 22) — allowed from internal network /24
- SSH high port — allowed from internal network /24
- OpenSearch Dashboard (port 5601) — allowed from internal network /24

## Best Practices Applied
- All rules restricted to internal subnet /24
- No external internet exposure
- Rules audited and cleaned up to remove stale or overly broad entries
- Port forwarding disabled on router to eliminate external attack surface

## Maintenance
- Regularly audit rules with: sudo ufw status numbered
- Remove any rules that are no longer needed
- Verify router port forwards match UFW rules
