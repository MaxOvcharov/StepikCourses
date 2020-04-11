from collections import deque

FORWARD_BRACKETS = ('(', '[', '{')
BACKWARD_BRACKETS = (')', ']', '}')
BACKWARD_TO_FORWARD_BRACKETS = {
    v: FORWARD_BRACKETS[i] for i, v in enumerate(BACKWARD_BRACKETS)
}


def check(data):
    dq = deque()
    for i, v in enumerate(data, start=1):
        if v in FORWARD_BRACKETS:
            dq.append((v, i))
        elif v in BACKWARD_BRACKETS:
            try:
                v_from_dq, _ = dq.pop()
                if BACKWARD_TO_FORWARD_BRACKETS[v] != v_from_dq:
                    return i
            except IndexError:
                return i
    i = 0
    if len(dq) != 0:
        _, i = dq.pop()

    return 0 if len(dq) == 0 and i == 0 else i


def run_check():
    data = input('Введите стороку:\n')
    print(f'{check(data) if check(data) != 0 else "Success"}')


if __name__ == '__main__':
    assert check('([](){([])})') == 0
    assert check('()[]}') == 5
    assert check('{{[()]]') == 7
    assert check('{{{[][][]') == 3
    assert check('{*{{}') == 3
    assert check('[[*') == 2
    assert check('{*}') == 0
    assert check('{{') == 2
    assert check('{}') == 0
    assert check('') == 0
    assert check('}') == 1
    assert check('*{}') == 0
    assert check('{{{**[][][]') == 3
    assert check('[]([]') == 3

    run_check()


