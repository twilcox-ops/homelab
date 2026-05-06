# Ansible Playbooks

## Overview
Ansible playbooks for automating system maintenance and service verification
across the homelab Linux environment.

## Playbooks

### site.yml
Main system maintenance playbook. Performs the following tasks:
- Updates apt package cache
- Verifies Fail2ban is running and enabled
- Verifies OpenSearch is running and enabled
- Verifies OpenSearch Dashboards is running and enabled

## Usage
Run against localhost:
ansible-playbook site.yml

## Notes
- Requires passwordless sudo configured for the running user
- Designed for Ubuntu Server environment
- Connection mode: local
