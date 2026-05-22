import random
import time
from abc import ABC, abstractmethod

class sensor(ABC): 

    def __init__(self, name: str, max: float, min: float) -> None:
        self.value = 0
        self.turned_on = False
        self.name = name
        self.max = max
        self.min = min

    @abstractmethod
    def turn_on(self) -> None:    
        pass

    @abstractmethod
    def run(self) -> None: 
        pass


class VoltageSensor(sensor): 

    def __init__(self, max, min):
        super().__init__("Test Voltage Sensor", max, min)
        self.turned_on = False

    def turn_on(self) -> None:
        if self.turned_on: 
            print(f'{self.name} is already on')
        else: 
            self.turned_on = True
            print(f'{self.name} is now on. ')

    def run(self) -> None: 
        while self.turned_on:
            if self.turned_on: 
                self.value = round(random.uniform(self.max, self.min), 2)
                print(f'Voltage: {self.value}')
                time.sleep(1)
            else: 
                print(f'{self.name} is not turned on. ')

class TemperatureSensor(sensor): 

    def __init__(self, max, min):
        super().__init__("Test Temperature Sensor", max, min)
        self.turned_on = False


    def turn_on(self) -> None:
        if self.turned_on: 
            print(f'{self.name} is already on')
        else: 
            self.turned_on = True
            print(f'{self.name} is now on. ')

    def run(self) -> None: 
        while self.turned_on:
            if self.turned_on: 
                self.value = round(random.uniform(self.max, self.min), 2)
                print(f'Temperature: {self.value}')
                time.sleep(1)
            else: 
                print(f'{self.name} is not turned on. ')

