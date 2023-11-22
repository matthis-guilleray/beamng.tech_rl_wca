from beamngpy import BeamNGpy, Scenario, Vehicle
from beamngpy.misc.quat import angle_to_quat
from beamngpy.sensors import Damage, Electrics, Camera
from beamngpy import BeamNGpy
import numpy as np


class Vehicle_cls :
    def __init__(self, beamng) -> None:
        self.beamng = beamng
        self.vehicle = None
        self.sensors_pool = None
        self.cam1, self.electrics, self.damage = None, None, None


    def create_vehicle(self,name, **args):
        if self.vehicle != None : 
            raise ValueError("The object already have been initialized")
        self.vehicle = Vehicle(name, **args)
        


    def create_sensors(self, cam1_pos = (-0.3, 1, 2), cam1_dir = (0, -1, 0), cam1_fov_y = 70, cam1_resolution = (256, 256)):
        if self.damage  != None : 
            raise ValueError("The object already have been initialized")
        # Creation of the camera N°1
        self.cam1 = Camera('camera1', self.beamng, self.vehicle, is_using_shared_memory=False,
                    pos=cam1_pos, dir=cam1_dir, field_of_view_y=cam1_fov_y, requested_update_time=0.000000001,
                    near_far_planes=(0.1, 100), resolution=cam1_resolution,
                    is_render_annotations=True, is_render_instance=False, is_render_depth=True)
        

        
        self.electrics = Electrics()
        self.damage = Damage()
        self.vehicle.sensors.attach('electrics', self.electrics)
        self.vehicle.sensors.attach('damage', self.damage)
        self.vehicle.sensors.poll()


    def reset_controls(self):
        self.vehicle.control(throttle=0.0, brake=0.0, steering=0.0)
        self.vehicle.set_shift_mode('realistic_automatic')
        self.vehicle.control(gear=2)
        self.vehicle.sensors.poll()

    
    def restart(self, position, rotation):
        # To avoid the vehicule moving after reset
        self.vehicle.control(throttle=0.0, brake=0.0, steering=0.0)
        self.vehicle.teleport(position,rotation,True)
        self.reset_controls()


    def plot_camera(self):
        self.sensors_pool["camera1"]["annotation"]


    def delete(self):
        self.vehicle.close()
        self.vehicle.disconnect()


    def get_sensors_results(self):
        
        # self.vehicle.sensors.poll()
        # self.sensors_pool = self.vehicle.sensors
        cam1_pool = self.cam1.poll()
        # electrics_pool = self.sensors_pool["electrics"]
        
        output_results = list()
        output_results.append(np.asarray(cam1_pool["annotation"].convert("RGB")))
        output_results.append(np.asarray(cam1_pool["depth"].convert("RGB")))
        """
        output_results.append(electrics_pool['rpm'])
        output_results.append(electrics_pool['gear_index'])
        output_results.append(electrics_pool['throttle'])
        output_results.append(electrics_pool['brake'])
        output_results.append(electrics_pool['steering'])
        output_results.append(electrics_pool['wheelspeed'])
        output_results.append(electrics_pool['altitude'])"""

        return output_results


    def get_sensors_output(self):
        if self.sensors_pool == None : 
            raise BufferError("The sensors pool is not filled, put the data in pool before")
        return self.sensors_pool
    

    def get_state(self):
        if self.sensors_pool == None : 
            raise BufferError("The sensors pool is not filled, put the data in pool before")
        return self.vehicle.state
    
    
    def set_ai_script(self, script):
        self.vehicle.ai.set_script(script)

    
    def set_ai_mode(self, mode="span", aggression = 0.3):
        self.vehicle.ai.set_mode(mode)
        self.vehicle.ai.set_aggression(aggression)
    
    

        

        
        

        




        
        




