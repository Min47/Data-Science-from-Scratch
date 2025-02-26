# 'r' means read-only, it's assumed if you leave it out
file_for_reading = open('reading_file.txt', 'r')
file_for_reading2 = open('reading_file.txt')

# 'w' is write -- will destroy the file if it already exists!
file_for_writing = open('writing_file.txt', 'w')

# 'a' is append -- for adding to the end of the file
file_for_appending = open('appending_file.txt', 'a')

# don't forget to close your files when you're done
file_for_writing.close()


# Because it is easy to forget to close your files, you should always use them in a with block, at the end of which they will be closed automatically:
filename = 'xxx.txt'
with open(filename) as f:
    data = []
    for line in f:
        data.append(line)
# at this point f has already been closed, so don't try to use it


# If you need to read a whole text file, you can just iterate over the lines of the file using 'for':
import re
starts_with_hash = 0

with open('input.txt') as f:
    for line in f: # look at each line in the file
        if re.match("^#",line): # use a regex to see if it starts with '#'
            starts_with_hash += 1 # if it does, add 1 to the count


# For example, imagine you have a file full of email addresses, one per line, and you need to generate a histogram of the domains. 
# The rules for correctly extracting domains are somewhat subtle—see, e.g., the Public Suffix List — 
# but a good first approximation is to just take the parts of the email addresses that come after the @
# (this gives the wrong answer for email addresses like joel@mail.datasciencester.com,
# but for the purposes of this example we’re willing to live with that):
def get_domain(email_address: str) -> str:
    """Split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]

# a couple of tests
assert get_domain('joelgrus@gmail.com') == 'gmail.com'
assert get_domain('joel@m.datasciencester.com') == 'm.datasciencester.com'

from collections import Counter

with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)