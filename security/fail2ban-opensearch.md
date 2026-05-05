# Security Monitoring Setup

## Overview
Configured Fail2ban for intrusion prevention and OpenSearch with OpenSearch
Dashboard for log monitoring and visualization.

## Fail2ban
Monitors SSH ports and automatically bans IPs that exceed failed login threshold.

### Configuration
- Monitoring SSH on standard and high ports
- Max retries: 5
- Find time: 30 minutes  
- Ban time: 24 hours
- Log backend: systemd journal

## OpenSearch
Deployed OpenSearch and OpenSearch Dashboard for centralized log monitoring.

## Log Ingestion
- Configured Fail2ban logs to feed into OpenSearch
- Logs visible and searchable via OpenSearch Dashboard
- Collaborated with a senior Linux engineer to configure log pipeline

## Lessons Learned
- Security monitoring requires both prevention (Fail2ban) and visibility (OpenSearch)
- Log aggregation enables pattern recognition across security events
- Collaboration with experienced engineers accelerates learning
