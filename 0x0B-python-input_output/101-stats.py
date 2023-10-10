#!/usr/bin/python3
"""Student Class"""


import sys


def print_statistics(total_size, status_codes):
    """Prints the statistics since the beginning."""
    print(f'Total file size: {total_size} bytes')
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f'{code}: {status_codes[code]}')


def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            words = line.split()
            try:
                size = int(words[-1])
                total_size += size
                code = words[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except Exception as e:
                pass
            if count % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)


if __name__ == '__main__':
    main()
