#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys
import os
import re


lines_count = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
total_size = 0
status_dict = {key: 0 for key in status_codes}

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        lines_count += 1

        # print(line.strip())
        status_size = re.findall(r'\d+', line.split('"')[2])
        status_code, file_size = status_size[0], status_size[1]
        for status in status_codes:
            if status == int(status_code):
                status_dict[status] += 1
                total_size += int(file_size)
        if lines_count == 10:
            print(f"File size: {total_size}")
            for code, rep in sorted(status_dict.items()):
                print(f"{code}: {rep}")
            lines_count = 0
            total_size = 0
            status_dict = {key: 0 for key in status_codes}
    except KeyboardInterrupt:
        break
