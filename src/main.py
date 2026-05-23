from sensor import VoltageSensor, TemperatureSensor

def main():

    t: TemperatureSensor = TemperatureSensor(75, 70)
    v: VoltageSensor = VoltageSensor(15, 12)

    t.turn_on()
    t.run()
main()