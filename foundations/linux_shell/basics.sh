#!/usr/bin/env bash
# =============================================================================
# Linux/Shell — Basics
# =============================================================================
# Topics: filesystem navigation, file operations, permissions, pipes,
#         redirection, variables, conditionals, loops.
# Run: bash basics.sh
# Docs: https://www.gnu.org/software/bash/manual/
# =============================================================================

# -----------------------------------------------------------------------------
# TODO 1: Filesystem Navigation & File Operations
# -----------------------------------------------------------------------------
# Practice these commands (run them in your terminal, not in this script):
#   pwd, ls -la, cd, mkdir -p, touch, cp, mv, rm -rf, find, tree
#
# Exercise: Create this directory structure:
#   ~/practice/
#     ├── src/main.py
#     ├── tests/test_main.py
#     └── docs/README.md
#
# Commands to run:
# mkdir -p ~/practice/{src,tests,docs}
# touch ~/practice/src/main.py ~/practice/tests/test_main.py ~/practice/docs/README.md

# -----------------------------------------------------------------------------
# TODO 2: File Permissions
# -----------------------------------------------------------------------------
# Understand and practice chmod/chown.
# chmod uses octal: 4=read, 2=write, 1=execute
# Owner | Group | Others
#   755 = rwxr-xr-x (standard for executables/dirs)
#   644 = rw-r--r-- (standard for files)
#   600 = rw------- (private files, e.g. SSH keys)
#
# Exercise: Create a script and set it executable
# echo '#!/bin/bash; echo "hello"' > /tmp/test_script.sh
# chmod 755 /tmp/test_script.sh
# ls -la /tmp/test_script.sh
# /tmp/test_script.sh

# -----------------------------------------------------------------------------
# TODO 3: Variables and Quoting
# -----------------------------------------------------------------------------
# Implement these variable exercises:

# TODO 3a: Declare and use variables
# NAME="World"
# echo "Hello, $NAME!"
# echo 'Hello, $NAME!'   # single quotes: no expansion
# echo "Path: $PATH"

# TODO 3b: Command substitution
# DATE=$(date +%Y-%m-%d)
# FILES=$(ls -1 | wc -l)
# echo "Today: $DATE, Files in current dir: $FILES"

# TODO 3c: Arithmetic
# A=10; B=3
# echo $((A + B))     # addition
# echo $((A * B))     # multiply
# echo $((A / B))     # integer division
# echo $((A % B))     # modulo

# -----------------------------------------------------------------------------
# TODO 4: Conditionals
# -----------------------------------------------------------------------------
# TODO 4a: if/elif/else
# Write a script that checks if a file exists:
#
# FILE="/tmp/testfile"
# if [ -f "$FILE" ]; then
#     echo "File exists"
# elif [ -d "$FILE" ]; then
#     echo "It is a directory"
# else
#     echo "Does not exist"
# fi

# TODO 4b: String comparison
# STR="hello"
# if [[ "$STR" == "hello" ]]; then echo "match"; fi
# if [[ "$STR" =~ ^h.*o$ ]]; then echo "regex match"; fi

# TODO 4c: Numeric comparison
# NUM=42
# if (( NUM > 40 )); then echo "greater than 40"; fi

# -----------------------------------------------------------------------------
# TODO 5: Loops
# -----------------------------------------------------------------------------
# TODO 5a: for loop over a list
# for FRUIT in apple banana cherry; do
#     echo "Fruit: $FRUIT"
# done

# TODO 5b: for loop with range
# for i in {1..5}; do
#     echo "Count: $i"
# done

# TODO 5c: while loop
# COUNTER=0
# while (( COUNTER < 5 )); do
#     echo "Counter: $COUNTER"
#     ((COUNTER++))
# done

# TODO 5d: Loop over files
# for FILE in /tmp/*.sh; do
#     echo "Found script: $FILE"
# done

# -----------------------------------------------------------------------------
# TODO 6: Functions
# -----------------------------------------------------------------------------
# TODO 6a: Basic function
# greet() {
#     local NAME="$1"
#     echo "Hello, $NAME!"
# }
# greet "World"

# TODO 6b: Function with return value (exit code)
# is_even() {
#     (( $1 % 2 == 0 ))  # returns 0 (true) if even
# }
# if is_even 4; then echo "4 is even"; fi

# -----------------------------------------------------------------------------
# TODO 7: Pipes and Redirection
# -----------------------------------------------------------------------------
# Practice:
#   > file          — redirect stdout to file (overwrite)
#   >> file         — redirect stdout (append)
#   2> file         — redirect stderr
#   2>&1            — redirect stderr to stdout
#   | command       — pipe stdout to next command
#
# Exercises:
# ls /nonexistent 2>/dev/null    # suppress error
# ls /tmp | grep ".sh" | wc -l  # count .sh files
# echo "hello" > /tmp/out.txt && cat /tmp/out.txt

# -----------------------------------------------------------------------------
# TODO 8: Script — Count Files by Extension
# -----------------------------------------------------------------------------
# Write a script that takes a directory as argument and counts files by extension.
# Expected output:
#   .py: 5 files
#   .sh: 3 files
#   .txt: 2 files
#
# Usage: bash basics.sh /path/to/dir
#
# #!/usr/bin/env bash
# DIR="${1:-.}"
# declare -A counts
# while IFS= read -r -d '' file; do
#     ext="${file##*.}"
#     ((counts[".$ext"]++))
# done < <(find "$DIR" -maxdepth 1 -type f -print0)
# for ext in "${!counts[@]}"; do
#     echo "$ext: ${counts[$ext]} files"
# done | sort
