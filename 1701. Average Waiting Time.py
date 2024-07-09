class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_wait_time = 0
        for customer in customers:
            arrival, time = customer
            if current_time < arrival:
                current_time = arrival
            wait_time = current_time + time - arrival
            total_wait_time += wait_time
            current_time += time
        return total_wait_time/len(customers)
        
