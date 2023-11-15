class Ducky:

    def __init__(self) -> None:
        pass

    def sum_iter_value(iterable):
        iter_to_test = iterable.replace(" ", ",").split(",")
        sum = 0
        for item in iter_to_test:
            if item.isnumeric():
                sum += float(item)
        return int(sum)

