from Solution import Solution
from Problem import Problem
from datetime import datetime


class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        state = prb.initState
        if prb.is_goal(state):
            return Solution(state, prb, start_time)
        queue = [state]
        explored = {}

        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if c.__hash__() not in explored:
                    if prb.is_goal(c):
                        return Solution(c, prb, start_time)
                    queue.append(c)
        return None

    @staticmethod
    def dfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        state = prb.initState
        stack = [state]
        explored = {}

        while len(stack) > 0:
            state = stack.pop()
            explored[state.__hash__()] = state
            neighbors = prb.successor(state)

            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in explored:
                    stack.append(c)
        return None

    @staticmethod
    def dls(prb: Problem, limit) -> Solution:
        start_time = datetime.now()
        queue = []
        explored = {}
        state = prb.initState
        queue.append(state)

        while len(queue) > 0:
            state = queue.pop()
            explored[state.__hash__()] = state
            neighbors = prb.successor(state)

            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in explored and c.g_n <= limit:
                    queue.append(c)
        return None

    @staticmethod
    def ids(prb: Problem) -> Solution:

        limit = 0
        while True:
            res = Search.dls(prb, limit)
            if res is not None:
                return res
            limit += 1

    @staticmethod
    def ucs(prb: Problem):
        start_time = datetime.now()
        state = prb.initState
        priority_queue = []
        priority_queue.append(state)
        explored = {}

        while len(priority_queue) != 0:
            priority_queue.sort(key=lambda state: state.g_n)
            state = priority_queue.pop(0)
            explored[state.__hash__()] = state
            neighbors = prb.successor(state)

            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in explored:
                    priority_queue.append(c)

        return None

    @staticmethod
    def a_star(prb: Problem):
        start_time = datetime.now()
        state = prb.initState
        priority_queue = []
        priority_queue.append(state)
        explored = {}

        while len(priority_queue) != 0:
            priority_queue.sort(key= lambda state: state.g_n + state.h())
            state = priority_queue.pop(0)
            explored[state.__hash__()] = state
            neighbors = prb.successor(state)

            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in explored:
                    priority_queue.append(c)

        return None

    @staticmethod
    def dla_star(prb: Problem, cutoff: int):
        start_time = datetime.now()
        queue = []
        explored = {}
        leaf_nodes = []
        state = prb.initState
        queue.append(state)

        while len(queue) > 0:
            state = queue.pop()
            explored[state.__hash__()] = state
            neighbors = prb.successor(state)
            leaf_nodes.extend(neighbors)

            for c in neighbors:

                if prb.is_goal(c):
                    return Solution(c, prb, start_time)

                if c.__hash__() not in explored and c.g_n + c.h() <= cutoff:
                    queue.append(c)
                    leaf_nodes.remove(c)

        min_value = min(leaf_nodes, key=lambda node: node.g_n + node.h())
        return min_value.g_n + min_value.h()


    @staticmethod
    def ida_star(prb: Problem):

        state = prb.initState
        cutoff = state.g_n + state.h()

        while True:
            res = Search.dla_star(prb, cutoff)
            print(res)
            if type(res) == Solution:
                return res
            else:
                cutoff = res
