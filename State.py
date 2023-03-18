# this class only for the first time setup init state for problem and is given to every search
class State:
    def __init__(self, pipes: list, parent, g_n: int, prev_action: tuple):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n
        self.prev_action = prev_action

    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.pipes[pipe_dest_ind].add_ball(self.pipes[pipe_src_ind].remove_ball())

    def __hash__(self):
        hash_strings = []
        for i in self.pipes:
            hash_strings.append(i.__hash__())
        hash_strings = sorted(hash_strings)
        hash_string = ''
        for i in hash_strings:
            hash_string += i + '###'
        return hash_string

    def h(self):

        points = []
        point = 0
        for pipe in self.pipes:
            if len(pipe.stack) != 0:
                current_ball = pipe.stack[0]
                point = 1

                for i in range(1, len(pipe.stack)):

                    if pipe.stack[i] == current_ball:
                        point += 1
                    else:
                        point -= (len(pipe.stack) - i)
                        break

            points.append(point)

        return -sum(points)
