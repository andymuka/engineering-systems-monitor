from sensor import sensor

def main():

    TestSensor: sensor = sensor()

    TestSensor.turn_on()
    TestSensor.run()

main()