from beamngpy import BeamNGpy
import time
import os

beamng_tech_home = os.getenv('BEAMNG_TECH_HOME')
if beamng_tech_home is None:
    raise EnvironmentError("BEAMNG_TECH_HOME environment variable is not defined")

beamng = BeamNGpy('localhost', 64256, home = beamng_tech_home, quit_on_close=False, crash_lua_on_error=False)
beamng.open(launch=True, listen_ip="*")
while True:
    time.sleep(10)