class MyHashMap:

    def __init__(self):
        self.myMap = [None for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.myMap[key] = value

    def get(self, key: int) -> int:
        return self.myMap[key] if self.myMap[key] != None else -1
        
    def remove(self, key: int) -> None:
        if self.myMap[key]:
            self.myMap[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)