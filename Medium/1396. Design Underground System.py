# medium

'''
An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.
'''

# https://leetcode.com/problems/design-underground-system/description/

from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.check = dict()
        self.time = defaultdict(int)
        self.count = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in = self.check.pop(id)
        dest_time = (check_in[0], stationName)

        self.time[dest_time] += t - check_in[1]
        self.count[dest_time] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.time[route] / self.count[route]

class UndergroundSystem:

    def __init__(self):
        self.check = dict()
        self.journey = defaultdict(lambda: [0, 0])
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in = self.check.pop(id)
        dest_time = (check_in[0], stationName)

        self.journey[dest_time][0] += t - check_in[1]
        self.journey[dest_time][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.journey[route][0] / self.journey[route][1]

# Time complexity = O(1)
# Space complexity = O(n) where n is the number of queries


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
