from pade.core.agent import Agent
from pade.acl.messages import ACLMessage


class CentralAgent(Agent):
    def __init__(self, aid):
        super().__init__(aid)
        self.temperature_readings = {}

    def react(self, message):
        super().react(message)
        
        if message.performative == ACLMessage.INFORM:
            temperature = float(message.content)
            sensor_id = message.sender.name
            self.temperature_readings[sensor_id] = temperature
            print(f"Temperatura recebida {temperature} de {sensor_id}")
            print(f"Média atual: {self.get_average_temperature()}")

    def get_average_temperature(self):
        if not self.temperature_readings:
            return None
        return sum(self.temperature_readings.values()) / len(self.temperature_readings)
