import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}
checks = [circle.area(0), square.perimeter(0)]


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    if size[0] < 0:
        raise ValueError("Size can't have a negative value")
    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space,\
                                    1 for circle and square\n").split(' ')))

    calc(fig, func, size)
