import random
import time

class sensor: 

    def __init__(self) -> None:
        self.value = 0
        self.turned_on = False


    def turn_on(self) -> None:
        if self.turned_on: 
            print('Sensor is already on')
        else: 
            self.turned_on = True
            print(f'Sensor is now on. ')

    def run(self) -> None: 
        while True:
            if self.turned_on: 
                self.value = round(random.uniform(70.0, 75.0), 2)
                print(f'{self.value}')
                time.sleep(1)
        else: 
            print(f'Sensor is not turned on. ')

