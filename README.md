# Airport Simulator

## Description 
This project simulates an airport control terminal informing us about the incoming landings and takeoffs of the aiport. 
The system uses two queues, a Landing Queue and a Takeoff Queue while maintaining an emergency queue for emergency landings. 

## Features 
- Priority queues for landing, giving a higher priority to emergency landings.
- Simple queue for takeoff requests.
- Random generation of flight requests(taking already generated flight IDs from a text file).
- The system prioritizes landing over takeoffs.

## Installation
1. Install Python 3.8+
