def sum_iter_value(iterable):
    iter_to_test = iterable.replace(" ", ",").split(",")
    sum = 0
    for item in iter_to_test:
        if item.isnumeric():
            sum += float(item)
    return int(sum)


def main():
    print(sum_iter_value())


if __name__ == "__main__":
    main()
