class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: dict[int, int] = {}

    def get(self, key: int) -> int:
        if key in self.items:
            # this key is now the most recently used key.
            # so we remove it, then add it to the end of the dict.
            value = self.items.pop(key)
            self.items[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            # this key is now the most recently used key.
            # so we remove it, then add it to the end of the dict.
            self.items.pop(key)
            self.items[key] = value
        else:
            if len(self.items) == self.capacity:
                # we're at capacity and about to add a new key,
                # so let's remove the very first key
                # (guaranteed to be the least-recently-used).
                self.items.pop(next(iter(self.items)))
            self.items[key] = value