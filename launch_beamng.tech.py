from beamngpy import BeamNGpy

beamng = BeamNGpy('localhost', 64256, home = "C:/Users/MSI/Desktop/BeamNG.tech.v0.30.6.0", quit_on_close=False, crash_lua_on_error=False)
beamng.open(launch=True, listen_ip="*")