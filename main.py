from datetime import datetime


def logger(path="func_log.log"):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            result = old_function(*args, **kwargs)
            func_name = old_function.__name__
            arguments = f"args: {args}\nkwargs:{kwargs}"
            with open(path, 'a', encoding="utf-8") as f:
                f.write(f"{'='*50}\n"
                        f"Date, time: {date_time}\n"
                        f"Function name: {func_name}\n"
                        f"Input arguments: \n{arguments}\n"
                        f"Result:\n"
                        f"{result}\n")

            return result

        return new_function
    print('Function is logged')
    return _logger


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', ['h', ['i']], False],
    [1, 2, None],
]


@logger("func_log.log")
def flat_generator(some_list):
    for element in some_list:
        if isinstance(element, list):
            for value in flat_generator(element):
                yield value
        else:
            yield element


if __name__ == '__main__':
    flat_generator(nested_list)
