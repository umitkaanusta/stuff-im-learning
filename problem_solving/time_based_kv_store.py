import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.db = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = {"values": [], "timestamps": []}
        self.db[key]["values"].append(value)
        self.db[key]["timestamps"].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        if self.db[key]["timestamps"][0] > timestamp:
            return ""
        if self.db[key]["timestamps"][-1] < timestamp:
            return self.db[key]["values"][-1]
        return self._search(key, timestamp)
    
    def _search(self, key, timestamp):
        idx = bisect.bisect_right(self.db[key]["timestamps"], timestamp)
        if idx:
            return self.db[key]["values"][idx - 1]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
