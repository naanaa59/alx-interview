#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0


def print_metrics():
    '''Prints the metrics'''
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 4:
            try:
                code = parts[-2]
                size = int(parts[-1])
                if code in status_codes:
                    status_codes[code] += 1
                total_size += size
                counter += 1
            except (IndexError, ValueError):
                continue

        if counter == 10:
            print_metrics()
            counter = 0

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)

print_metrics()
