import sys

# Also, can do for count:
count = 0

for line in sys.stdin:
    count += 1
    
# print goes to sys.stdout
print(count)

# Run:
# echo "hello`nworld`nhello world" | python 2_line_count.py
# Output:
# 3