class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val=self.cache.pop(key)
            self.cache[key]=val
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache)==self.capacity:
                    lru=next(iter((self.cache)))
                    self.cache.pop(lru)
        else:
            self.cache.pop(key)
        self.cache[key]=value
            

