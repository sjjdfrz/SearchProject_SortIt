from Pipe import Pipe
from Problem import Problem
from State import State
from Search import Search

if __name__ == '__main__':
    test_path = 'tests/test1.txt'
    file = open(test_path, 'r')
    p = []
    for i in file.readlines():
        a = i.replace('\n', '')
        a = a.replace(' ', '')
        a = a.split(',')
        p.append(Pipe(a[:-1], int(a[-1])))

    s = Search.ids(Problem(State(p, None, 0, (0, 0))))
    s.print_path()
    s.execute_gui()
