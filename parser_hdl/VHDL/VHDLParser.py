from pyparsing import ParseException

from parser_hdl.abstracts import HDLParser
from parser_hdl.VHDL.architecture import vhdl_module_definition


# VHDL parser
class VHDLParser(HDLParser):
    def __init__(self, file_path):
        HDLParser.__init__(self, file_path)

    def to_dict(self, parsed_data):
        print(parsed_data)
        parsed_dict = {
            "entity_name": parsed_data["entity"]["entity_name"],
            "ports": [
                {
                    "port_name": p["port_name"],
                    "direction": p["direction"],
                    "type": p["type"],
                }
                for p in parsed_data["entity"].get("ports", [])
            ],
            "architecture_name": parsed_data["architecture"]["architecture_name"],
            "signals": [
                {"signal_name": s["signal_name"], "signal_type": s["signal_type"]}
                for s in parsed_data["architecture"].get("signals", [])
            ],
            "instances": [
                {
                    "instance_name": inst["instance_name"],
                    "component_name": inst["component_name"],
                    "port_connections": [
                        {"port": conn["port"], "connection": conn["connection"]}
                        for conn in inst["port_connections"]
                    ],
                }
                for inst in parsed_data["architecture"].get("instances", [])
            ],
        }
        return parsed_dict

    def parse(self, file_content):
        try:
            module_result = vhdl_module_definition.parseString(file_content)
            parsed_data = self.to_dict(module_result[0])
            return parsed_data
        except ParseException as pe:
            print(f"Error parsing VHDL file\n{pe}")
            return None
