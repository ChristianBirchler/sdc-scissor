import abc


class SegmentationStrategy(abc.ABC):
    @abc.abstractmethod
    def extract_segments(self, road_points) -> list[tuple[int, int]]:
        pass
