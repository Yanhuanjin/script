import math
import datetime
from decimal import Decimal


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
    return int_time

@count_time
def main():
    i = 100000
    # while i<10000:
        # i = int(input("Input n:"))
    fi = (1 + math.sqrt(5)) / 2
    Fi = (Decimal(fi)**Decimal(i)/Decimal(math.sqrt(5)) + Decimal(1/2))
    print("The n th of Fibernacci is: %d" % Fi)
    # i += 1

if __name__ == "__main__":
    main()