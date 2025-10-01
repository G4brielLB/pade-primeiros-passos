from pade.core.agent import Agent
from temperature_sensor_behavior import TemperatureSensorBehavior


class SensorAgent(Agent):
    def __init__(self, aid, central_aid):
        super().__init__(aid)
        self.central_aid = central_aid
        self.behaviours.append(TemperatureSensorBehavior(self, 10))  # Envia temperatura a cada 10 segundos
