import functools


# A class to calculate a running average
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


if __name__ == '__main__':
    avg = Averager()
    print(f"avg(10): {avg(10)}, avg(11): {avg(11)}, avg(12): {avg(12)}")

    data = functools.reduce(lambda a, b: a*b, range(1, 6))
    # data: 120
    print(f"data: {data}")