from pade.acl.messages import ACLMessage
from pade.behaviours.protocols import TimedBehaviour
import random

class TemperatureSensorBehavior(TimedBehaviour):
    def __init__(self, agent, interval):
        super().__init__(agent, interval)

    def on_time(self):
        temperature = round(random.uniform(30.0, 40.0), 1)  # Simula uma leitura de temperatura
        msg = ACLMessage(ACLMessage.INFORM)
        msg.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        msg.add_receiver(self.agent.central_aid)
        msg.set_content(str(temperature))
        self.agent.send(msg)
        print(f"Sensor {self.agent.aid.name} enviou temperatura: {temperature}")
        super().on_time()