"""
This class simulates the flight control system, managing airplane takeoff and landing requests through a control tower mediator.
"""
from typing import List

from control_tower import ControlTower
from airplane import Airplane

class Exercise:
    def main(self):
        control_tower: ControlTower = ControlTower()
        airplane_list: List[Airplane] = list()

        for i in range(4):
            airplane_id = input(f"Enter airplane id: ")
            # Initialise the airplane
            airplane: Airplane = Airplane(airplane_id)
    
            # Register the airplane
            control_tower.register_airplane(airplane)

            # Request for takeoff
            airplane.request_take_off()

            airplane_list.append(airplane)

        # Mark the first airplane as having completed takeoff and free a runway
        airplane_list[0].complete_takeoff()

        # Mark the second airplane as having completed takeoff and free a runway
        airplane_list[1].complete_takeoff()

        airplane_list[2].request_take_off()
        airplane_list[3].request_take_off()

        # Mark the third airplane as having completed takeoff and free a runway
        airplane_list[2].complete_takeoff()

        # Mark the fourth airplane as having completed takeoff and free a runway
        airplane_list[3].complete_takeoff()

        # Landing requests
        airplane_list[0].request_landing()
        airplane_list[1].request_landing()

        # Mark the first airplane as having completed landing and free a runway
        airplane_list[0].complete_landing()

        # Mark the second airplane as having completed landing and free a runway
        airplane_list[1].complete_landing()

        airplane_list[2].request_landing()
        airplane_list[3].request_landing()

        # Mark the third airplane as having completed landing and free a runway
        airplane_list[2].complete_landing()
        
        # Mark the fourth airplane as having completed landing and free a runway
        airplane_list[3].complete_landing()

if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()