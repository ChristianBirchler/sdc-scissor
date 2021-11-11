from typing import List

from deeper.Deeper_test_generator.config import Config
from deeper.Deeper_test_generator.archive import Archive
from deeper.Deeper_test_generator.individual import Individual
from deeper.Deeper_test_generator.member import Member


class Problem:
    def __init__(self, config: Config, archive: Archive):
        self.config: Config = config
        self.archive = archive

    def deap_generate_individual(self) -> Individual:
        raise NotImplementedError()

    def deap_mutate_individual(self, individual: Individual):
        individual.mutate()

    def deap_evaluate_individual(self, individual: Individual):
        raise NotImplementedError()

    def deap_individual_class(self):
        raise NotImplementedError()

    def on_iteration(self, idx, pop: List[Individual], logbook):
        raise NotImplementedError()

    def member_class(self):
        raise NotImplementedError()

    def reseed(self, population, offspring):
        raise NotImplementedError()

    def generate_random_member(self) -> Member:
        raise NotImplementedError()

    def pre_evaluate_members(self, individuals: List[Individual]):
        pass
