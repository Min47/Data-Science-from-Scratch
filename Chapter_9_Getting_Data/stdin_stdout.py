import sys,re

# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys.argv[1]

# for every line passed into the script
for line in sys.stdin:
# if it matches the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)


# Powershell run using this format:
# Write-Output {sys.stdin} | python {pyfile} {regex/sys.argv[1]}

# Example:
# Write-Output "hello`nworld`nhello world" | python stdin_stdout.py "hello"

# Output:
# hello
# hello world

# Also can use echo:
# echo "hello`nworld`nhello world" | python stdin_stdout.py "hello"