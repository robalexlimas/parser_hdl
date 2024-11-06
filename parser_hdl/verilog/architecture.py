from pyparsing import Group, Suppress, Optional, OneOrMore, Literal, delimitedList, Dict

from parser_hdl.verilog.constants import *


# Ports
port_definition = Group((input_kw | output_kw)("direction") + identifier("port_name"))

port_map = Group(
    Literal(".")
    + identifier("port")
    + Suppress("(")
    + identifier("connection")
    + Suppress(")")
)


instance_definition = Group(
    identifier("instance_type")("instance_type")
    + identifier("instance_name")("instance_name")
    + Suppress("(")
    + Group(delimitedList(port_map))("port_connections")
    + Suppress(");")
)

# Module
module_definition = Group(
    module_kw.suppress()
    + identifier("module_name")("module_name")
    + Suppress("(")
    + Optional(Group(delimitedList(port_definition))("ports"))
    + Suppress(");")
    + Optional(OneOrMore(wire_kw.suppress() + identifier("wire_name") + Suppress(";")))(
        "wires"
    )
    + OneOrMore(instance_definition)("instances")
    + endmodule_kw.suppress()
)
