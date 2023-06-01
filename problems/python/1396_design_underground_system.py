class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {} # client id -> (startStation, startTime)
        self.times = defaultdict(int) # (startStation, endStation) -> sum of times
        self.data = defaultdict(int)  # (startStation, endStation) -> number of data
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedIn:
            self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedIn:
            startStation, startTime = self.checkedIn[id]
            self.times[(startStation, stationName)] += t - startTime
            self.data[(startStation, stationName)] += 1
            del self.checkedIn[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = self.times.get((startStation, endStation))
        dataNumber = self.data.get((startStation, endStation))
        return totalTime/dataNumber


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
