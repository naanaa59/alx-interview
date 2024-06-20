#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys
import re
from signal import signal, SIGINT


lines_count = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
total_size = 0
status_dict = {code: 0 for code in status_codes}


def print_metrics():
    """ print method"""
    print(f"File size: {total_size}")
    for code, count in sorted(status_dict.items()):
        if count > 0:
            print(f"{code}: {count}")


def handler(signum, frame):
    """ signal handler"""
    print_metrics()
    sys.exit(0)


signal(SIGINT, handler)


try:
    for line in sys.stdin:
        try:
            # print(line.strip())
            parts = line.split()
            status_code, file_size = int(parts[-2]), int(parts[-1])
            # print(status_code, file_size)
            # print("///")
            if status_code in status_dict:
                # print("///")
                status_dict[status_code] += 1
                total_size += file_size
            lines_count += 1
            if lines_count % 10 == 0:
                print_metrics()
        except (IndexError, ValueError):
            continue
except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
