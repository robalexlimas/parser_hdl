from pyparsing import ParseException

from parser_hdl.abstracts import HDLParser
from parser_hdl.verilog.architecture import module_definition


# Verilog parser
class VerilogParser(HDLParser):
    def __init__(self, file_path):
        HDLParser.__init__(self, file_path)

    def to_dict(self, parsed_data):
        parsed_dict = {
            "module_name": parsed_data["module_name"],
            "ports": [
                {"direction": p["direction"], "port_name": p["port_name"]}
                for p in parsed_data.get("ports", [])
            ],
            "wires": [{"wire_name": w} for w in parsed_data.get("wires", [])],
            "instances": [
                {
                    "instance_type": inst["instance_type"],
                    "instance_name": inst["instance_name"],
                    "port_connections": [
                        {"port": conn["port"], "connection": conn["connection"]}
                        for conn in inst["port_connections"]
                    ],
                }
                for inst in parsed_data.get("instances", [])
            ],
        }
        return parsed_dict

    def parse(self, file_content):
        try:
            modules = module_definition.parseString(file_content)
            parsed_data = {"modules": [self.to_dict(m) for m in modules]}
            return parsed_data
        except ParseException as pe:
            print(f"Error parsing Verilog file\n{pe}")
            return None
