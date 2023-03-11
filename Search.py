from Solution import Solution
from Problem import Problem
from datetime import datetime
from PriorityQueue import PriorityQueue


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
            limit += 1
            if res is not None:
                return res

    @staticmethod
    def ucs(prb: Problem):
        start_time = datetime.now()
        state = prb.initState
        priority_queue = PriorityQueue()
        priority_queue.insert(state)
        explored = {}

        while not priority_queue.isEmpty():
            state = priority_queue.pop()
            explored[state.__hash__()] = state
            neighbors = prb.successor(state)

            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in explored:
                    priority_queue.insert(c)

        return None
