import logging

from refactored_pipeline.simulator_api.abstract_simulator import AbstractSimulator
from refactored_pipeline.simulator_api.beamng_simulator import BeamNGSimulator


class SimulatorFactory:
    @staticmethod
    def get_beamng_simulator() -> AbstractSimulator:
        beamng_simulator = BeamNGSimulator(
            host='localhost',
            port=64256,
            home=r'C:\Users\birc\Documents\BeamNG.tech.v0.24.0.2\BeamNG.drive-0.24.0.2.13392',
            user=r'C:\Users\birc\Documents\BeamNG.drive'
        )
        return beamng_simulator


if __name__ == '__main__':
    logging.info('* simulator_factory.py')
