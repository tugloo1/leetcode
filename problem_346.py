from queue import Queue


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.rolling_sum = 0
        self.size = size
        self.q = Queue()

    def next(self, val: int) -> float:
        self.q.put(val)
        self.rolling_sum += val
        if self.q.qsize() > self.size:
            old = self.q.get()
            self.rolling_sum -= old
        return self.rolling_sum / self.q.qsize()

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)