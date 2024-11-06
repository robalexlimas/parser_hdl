from abc import ABC, abstractmethod


# HDL parser based on abstract class
class HDLParser(ABC):
    def __init__(self, file_content):
        self.file_content = file_content

    @abstractmethod
    def parse(self):
        """Abstract method for parsing HDL codes"""
        pass

    @abstractmethod
    def to_dict(self, parsed_data):
        """Abstract method for parsing HDL codes"""
        pass
