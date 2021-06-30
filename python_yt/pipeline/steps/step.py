from abc import ABC
from abc import abstractmethod


class Steps(ABC):  # 抽象物件(abstract base class)至少需要一個或以一個以上的abstract method
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):
        pass


# 繼承python內部的Exception的物件
class StepException(Exception):  # 程式中任何錯誤停止時，讓他觸發這個物件，讓我們可以用TryException來捕捉錯誤
    pass
