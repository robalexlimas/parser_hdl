from parser_hdl.verilog import VerilogParser
from parser_hdl.VHDL import VHDLParser


# Wrapper
class HDLFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        if self.file_path.endswith(".vhd") or self.file_path.endswith(".vhdl"):
            parser = VHDLParser(file_path)
        elif self.file_path.endswith(".v") or self.file_path.endswith(".verilog"):
            parser = VerilogParser(file_path)
        else:
            raise ValueError(
                "Format is not supported. Formats allowed are VHDL (.vhd, .vhdl) or Verilog (.v, .verilog)."
            )
        self.parser = parser

    def _get_file_content(self):
        with open(self.file_path, "r") as file:
            return file.read()

    def parse_file(self):
        file_content = self._get_file_content()
        return self.parser.parse(file_content)
