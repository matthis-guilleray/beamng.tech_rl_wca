from beamngpy import BeamNGpy, Scenario, Vehicle, set_up_simple_logging
import matplotlib.pyplot as plt
import time
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
print(sys.path)
from object.Vehicule import Vehicle_cls # This file need to be in the same folder


def main():
    set_up_simple_logging()

    beamng = BeamNGpy('localhost', 64256, quit_on_close=False)
    beamng.open(launch=False)

    scenario = Scenario('west_coast_usa', 'ai_sine')
    vehicle = Vehicle_cls(beamng)
    vehicle.create_vehicle("ego", model = 'etk800', license="AI")
    scenario.add_vehicle(vehicle.vehicle, pos=(-769.1, 400.8, 142.8), rot_quat=(0, 0, 1, 0))
    scenario.make(beamng)

    beamng.settings.set_deterministic(60)

    try:
        beamng.scenario.load(scenario)
        vehicle.create_sensors()
        beamng.ui.hide_hud()
        beamng.scenario.start()
        vehicle.set_ai_mode('span', 0.1)
        time.sleep(1)
        plt.ion()
        while True:
            print("Step	: ")
            step_time = time.time()

            beamng.control.step(1)
            print("time 1 : ", time.time()-step_time)
            step_time = time.time()
            
            sensors = vehicle.get_sensors_results()
            print("time 2 : ", time.time()-step_time)
            step_time = time.time()

            plt.imshow(sensors[0])
            print("time 3 : ", time.time()-step_time)
            step_time = time.time()

            plt.show()
            print("time 4 : ", time.time()-step_time)
            step_time = time.time()

            plt.pause(0.000000001)
    finally:
        beamng.close()


if __name__ == '__main__':
    main()