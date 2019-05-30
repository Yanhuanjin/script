import datetime

def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
    return int_time


def fab(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

@count_time
def main():
    n = 0
    while n<10:
        # n = int(input("Input n: "))
        print("The n th Fibernacii number is: %d" % fab(n))
        n += 1

if __name__ == "__main__":
    main()