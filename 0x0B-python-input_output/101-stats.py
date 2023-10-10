#!/usr/bin/python3
"""Student Class"""


import sys


def print_statistics(total_size, status_codes):
    """Prints the statistics since the beginning."""
    print(f'Total file size: {total_size} bytes')
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(key, status_codes[key]))

def main():
    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

if __name__ == '__main__':
    main()
