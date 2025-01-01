from abc import ABC, abstractmethod

class BaseProduct(ABC):


    @abstractmethod
    def __add__(self, other) -> float:
        pass

    # @classmethod
    # @abstractmethod
    # def new_product(cls):
    #     pass



