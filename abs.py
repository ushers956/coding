from abc import ABC, abstractmethod

class absclass(ABC):


    def print(self,x):
        print("passed value:", x)

    @abstractmethod
    def task(self):
        print("we are inside absclass task")

class test_task(absclass):
    def task(self):
        print("we are inside test_class task")

test_obj = test_task()
test_obj.task()
test_obj.print(100)