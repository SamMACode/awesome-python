import functools


# A class to calculate a running average
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value): # 自定义异常信息的初始化
        self.value = value

    def __str__(self): # 自定义异常类型的string表达式
        return "{} is invalid input".format(repr(self.value))


if __name__ == '__main__':
    avg = Averager()
    print(f"avg(10): {avg(10)}, avg(11): {avg(11)}, avg(12): {avg(12)}")

    data = functools.reduce(lambda a, b: a*b, range(1, 6))
    # data: 120
    print(f"data: {data}")

    try:
        # error: 1 is invalid input
        raise MyInputError(1)
    except MyInputError as err:
        print('error: {}'.format(err))
