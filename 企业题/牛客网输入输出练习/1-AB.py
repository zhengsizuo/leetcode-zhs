# import sys
# for line in sys.stdin:
#     a = line.split()
#     a = [int(x) for x in a]
#     print(a[0]+a[1])

import sys
for line in sys.stdin:
    new_line = line.split()
    print(new_line)
    new_line.sort()
    print(' '.join(new_line))