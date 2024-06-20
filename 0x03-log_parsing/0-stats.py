#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys
import os
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
    raise KeyboardInterrupt


signal(SIGINT, handler)


try:
    for line in sys.stdin:
        # print(line.strip())
        status_size = re.findall(r'\d+', line.split('"')[2])
        status_code, file_size = status_size[0], status_size[1]
        if status_code and file_size:
            # print("///")
            lines_count += 1
        for status in status_codes:
            if status == int(status_code):
                status_dict[status] += 1
                total_size += int(file_size)
        if lines_count % 10 == 0:
            print_metrics()
except Exception as e:
    pass