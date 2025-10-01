from pade.acl.aid import AID
from pade.misc.utility import start_loop

from central_agent import CentralAgent
from sensor_agent import SensorAgent


def create_agents():
	central_aid = AID(name='central@localhost:2000')
	central_agent = CentralAgent(central_aid)

	sensor_agents = []
	base_port = 2001
	for index in range(4):
		sensor_aid = AID(name=f'sensor{index + 1}@localhost:{base_port + index}')
		sensor_agents.append(SensorAgent(sensor_aid, central_aid))

	return [central_agent, *sensor_agents]


def main():
	agents = create_agents()
	start_loop(agents)


if __name__ == '__main__':
	main()
