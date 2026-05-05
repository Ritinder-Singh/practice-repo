#!/usr/bin/env bash
# =============================================================================
# Linux/Shell — Advanced
# =============================================================================
# Topics: awk, sed, grep/regex, process management, systemd, cron, networking
#         tools, file descriptors, advanced scripting patterns.
# Run: bash advanced.sh
# =============================================================================

# -----------------------------------------------------------------------------
# TODO 1: grep & Regular Expressions
# -----------------------------------------------------------------------------
# grep -E (extended regex), -i (case insensitive), -r (recursive), -l (files only)
#
# Practice:
# grep -rE "TODO|FIXME" /path/to/project --include="*.py"
# grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' /var/log/syslog  # IPs
# grep -v "^#" /etc/hosts | grep -v "^$"   # non-comment, non-empty lines
#
# TODO 1a: Write a command to find all Python files importing 'os' module:
# grep -rl "^import os" /path/to/project --include="*.py"

# -----------------------------------------------------------------------------
# TODO 2: awk — Field Processing
# -----------------------------------------------------------------------------
# awk 'pattern { action }' file
# Built-in vars: NR (row num), NF (field count), $1 $2 (fields), FS (separator)
#
# TODO 2a: Print second column of a CSV
# awk -F',' '{print $2}' data.csv
#
# TODO 2b: Sum all values in column 3
# awk -F',' '{sum += $3} END {print "Total:", sum}' data.csv
#
# TODO 2c: Print lines where field 4 > 100
# awk -F',' '$4 > 100 {print $0}' data.csv
#
# TODO 2d: Write awk to count occurrences of each word in a file:
# awk '{for(i=1;i<=NF;i++) count[$i]++} END {for(w in count) print count[w], w}' file | sort -rn

# -----------------------------------------------------------------------------
# TODO 3: sed — Stream Editor
# -----------------------------------------------------------------------------
# sed 's/old/new/g'           — substitute
# sed -n '10,20p'             — print lines 10-20
# sed '/pattern/d'            — delete matching lines
# sed -i 's/foo/bar/g' file   — in-place edit
#
# TODO 3a: Replace all occurrences of 'localhost' with '0.0.0.0' in a config:
# sed -i 's/localhost/0.0.0.0/g' config.ini
#
# TODO 3b: Remove all blank lines from a file:
# sed '/^$/d' input.txt > output.txt
#
# TODO 3c: Add line numbers to a file:
# sed '=' input.txt | sed 'N; s/\n/\t/'

# -----------------------------------------------------------------------------
# TODO 4: Process Management
# -----------------------------------------------------------------------------
# ps aux               — all processes
# ps aux | grep nginx  — find specific process
# kill -9 PID          — force kill
# kill -15 PID         — graceful terminate (SIGTERM)
# pkill process_name   — kill by name
# pgrep process_name   — get PIDs by name
# top / htop           — interactive process viewer
# lsof -i :8080        — what's using port 8080
# ss -tlnp             — listening TCP sockets
#
# TODO 4a: Write a function that kills all processes by name:
# kill_by_name() {
#     local NAME="$1"
#     pkill -f "$NAME" && echo "Killed $NAME" || echo "No process named $NAME"
# }

# -----------------------------------------------------------------------------
# TODO 5: Cron Jobs
# -----------------------------------------------------------------------------
# crontab -e     — edit cron jobs
# crontab -l     — list cron jobs
# Format: minute hour day month weekday command
#   *  — any value
#   */5 — every 5 units
#
# TODO 5a: Schedule a backup script every day at 2:30 AM:
# 30 2 * * * /home/user/backup.sh >> /var/log/backup.log 2>&1
#
# TODO 5b: Run a cleanup script every Monday at 9 AM:
# 0 9 * * 1 /home/user/cleanup.sh
#
# TODO 5c: Write a backup script that:
#   - Archives a directory with tar
#   - Names the archive with a timestamp
#   - Removes archives older than 7 days
#
# #!/usr/bin/env bash
# BACKUP_DIR="/var/backups"
# SOURCE_DIR="/home/user/data"
# TIMESTAMP=$(date +%Y%m%d_%H%M%S)
# tar -czf "$BACKUP_DIR/backup_$TIMESTAMP.tar.gz" "$SOURCE_DIR"
# find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -delete

# -----------------------------------------------------------------------------
# TODO 6: Networking Tools
# -----------------------------------------------------------------------------
# curl -I url         — HTTP headers only
# curl -o file url    — download to file
# wget url            — download file
# ss -tlnp            — listening sockets (modern netstat)
# nc -zv host port    — check if port is open
# dig domain          — DNS lookup
# nslookup domain     — DNS lookup (older)
# ping -c 4 host      — ICMP ping
# traceroute host     — trace network path
# tcpdump -i eth0     — capture packets
#
# TODO 6a: Write a port scanner using nc:
# port_scan() {
#     local HOST="$1"
#     for PORT in {20..1024}; do
#         (echo >/dev/tcp/"$HOST"/"$PORT") 2>/dev/null && echo "Port $PORT open"
#     done
# }

# -----------------------------------------------------------------------------
# TODO 7: Advanced Script — Log Parser
# -----------------------------------------------------------------------------
# Write a script that parses an nginx/apache access log and reports:
#   - Top 10 most frequent IP addresses
#   - Top 10 most requested URLs
#   - Count of each HTTP status code
#   - Total bandwidth served (sum of bytes column)
#
# Nginx log format: IP - - [datetime] "METHOD URL HTTP/1.1" STATUS BYTES
#
# #!/usr/bin/env bash
# LOG="${1:-/var/log/nginx/access.log}"
#
# echo "=== Top 10 IPs ==="
# awk '{print $1}' "$LOG" | sort | uniq -c | sort -rn | head -10
#
# echo "=== Top 10 URLs ==="
# awk '{print $7}' "$LOG" | sort | uniq -c | sort -rn | head -10
#
# echo "=== Status Code Distribution ==="
# awk '{print $9}' "$LOG" | sort | uniq -c | sort -rn
#
# echo "=== Total Bandwidth (bytes) ==="
# awk '{sum += $10} END {printf "%.2f MB\n", sum/1024/1024}' "$LOG"

# -----------------------------------------------------------------------------
# TODO 8: File Descriptors and Here Documents
# -----------------------------------------------------------------------------
# TODO 8a: Write to multiple files simultaneously using tee:
# { echo "log entry"; } | tee -a log1.txt log2.txt > /dev/null
#
# TODO 8b: Use heredoc to write a multi-line config file:
# cat > /tmp/config.ini << 'EOF'
# [database]
# host = localhost
# port = 5432
# name = mydb
# EOF
#
# TODO 8c: Open file descriptors manually:
# exec 3>/tmp/myfd.txt    # open fd 3 for writing
# echo "hello" >&3
# exec 3>&-               # close fd 3
