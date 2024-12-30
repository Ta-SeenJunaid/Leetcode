class MyCalendarTwo:

    def __init__(self):
        self.cal = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        overlap = 0
        for s, e in self.cal:
            if s < endTime and e > startTime:
                overlap += 1            
            if overlap == 2:
                return False
        self.cal.append((startTime, endTime))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
