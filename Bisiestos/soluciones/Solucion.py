from sys import stdin


def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 900 not in [200, 600]:
        return False
    return True


def leaps(start, end):
    # There are 218 leap years every 900 years
    easy_range = (end - start) // 900
    easy_leaps = easy_range * 218
    end -= easy_range * 900
    return easy_leaps + sum(1 for x in range(start, end) if is_leap_year(x))


def main():
    for line in stdin.readlines():
        start, end = line.split()
        print(leaps(int(start), int(end)))


if __name__ == '__main__':
    main()
