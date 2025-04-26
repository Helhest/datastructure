## code by Theodore Dardavilas ( 2331851 )
## for DATA STRUCTURE AND ALGORITHMS ( SWE5002 )


import random 
import time
import heapq
from collections import deque



class Flight:
    def __init__(self, flight_id , sos = False):
        self.flight_id = flight_id
        self.sos = sos 

        # flight_id is how we are going to keep track of the flights 
        # sos attribute is to classify a flight as an emergency flight 

        def __It__ (self, other):
            return self.sos > other.sos
        
        # We make the priority of an emergency flight higher

class AirportControl: 
    def __init__(self):
        self.q = [] #Landing queue
        self.takeoffq = deque() #Takeoff queue 



    def req_landing(self, flight_id , sos = False):
        flight = Flight(flight_id , sos)
        heapq.heappush(self.q , flight)
        if sos:
            print(f"Flight with ID {flight_id} requests EMERGENCY landing.")
        else:
            print(f"Flight with ID {flight_id} requests landing.")



    def req_takeoff(self, fligh_id):
        self.takeoffq.append(fligh_id)
        print(f"Flight with ID  {fligh_id} requests takeoff.")



    def control(self):
        if self.q:
            flight = heapq.heappop(self.q)
            print(f"CONTROL: {flight.flight_id} land.")
        elif self.takeoffq:
            flight_id = self.takeoffq.popleft()
            print(f"CONTROL: {flight_id} takeoff.")
        else: 
            print("No flights waiting.")



    def sim(self, num_events=20):
        with open('id.txt', 'r') as file:
            ids = file.read().splitlines()
        flight_number = random.choice(ids)
        starting_id = flight_number
        for _ in range(num_events):
            action = random.choice(['landing', 'takeoff' , 'emergency landing'])
            if action == 'landing':
                self.req_landing(flight_number)
            elif action == 'takeoff' : 
                self.req_takeoff(flight_number)
            elif action == 'emergency landing':
                self.req_landing(flight_number, sos = True)
                
            flight_number = random.choice(ids)
            while flight_number == starting_id : 
                flight_number == random.choice(ids)
            else:
                self.control()
                time.sleep(1.5)


if __name__ == "__main__":
    airport = AirportControl()
    airport.sim()