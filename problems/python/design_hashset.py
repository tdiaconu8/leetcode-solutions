class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.set:
            return True
        else:
            return False