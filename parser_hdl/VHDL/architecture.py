from pyparsing import Group, Suppress, Optional, OneOrMore, Dict, delimitedList

from .constants import *


# Ports
port_definition = Group(
    identifier("port_name")
    + Suppress(":")
    + identifier("direction")
    + identifier("type")
)

# Entity
entity_definition = Dict(
    Group(
        entity_kw.suppress()
        + identifier("entity_name")
        + is_kw.suppress()
        + Optional(
            port_kw.suppress()
            + Suppress("(")
            + Group(OneOrMore(port_definition + Optional(Suppress(";"))))("ports")
            + Suppress(");")
        )
        + end_kw.suppress()
        + Optional(entity_kw)
        + Optional(identifier)("entity_name_end")
        + Suppress(";")
    )
)

# Signals
signal_definition = Group(
    signal_kw.suppress()
    + identifier("signal_name")
    + Suppress(":")
    + identifier("signal_type")
    + Suppress(";")
)

# Instances
instance_definition = Group(
    identifier("instance_name")
    + Suppress(":")
    + Optional(component_kw.suppress())
    + identifier("component_name")
    + port_map_kw.suppress()
    + Suppress("(")
    + Group(
        delimitedList(
            Group(identifier("port") + Suppress("=>") + identifier("connection"))
        )
    )("port_connections")
    + Suppress(");")
)

# Architecture
architecture_definition = Dict(
    Group(
        architecture_kw.suppress()
        + identifier("architecture_name")
        + of_kw.suppress()
        + identifier("entity_name")
        + is_kw.suppress()
        + Optional(OneOrMore(signal_definition))("signals")
        + begin_kw.suppress()
        + OneOrMore(instance_definition)("instances")
        + end_kw.suppress()
        + architecture_kw.suppress()
        + Optional(identifier("architecture_name_end"))
        + Suppress(";")
    )
)

vhdl_module_definition = entity_definition("entity") + architecture_definition(
    "architecture"
)
