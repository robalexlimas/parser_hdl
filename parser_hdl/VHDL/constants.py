from pyparsing import (
    Word,
    alphas,
    alphanums,
    CaselessKeyword,
)

entity_kw = CaselessKeyword("entity")
architecture_kw = CaselessKeyword("architecture")
of_kw = CaselessKeyword("of")
is_kw = CaselessKeyword("is")
port_kw = CaselessKeyword("port")
end_kw = CaselessKeyword("end")
signal_kw = CaselessKeyword("signal")
component_kw = CaselessKeyword("component")
begin_kw = CaselessKeyword("begin")
port_map_kw = CaselessKeyword("port map")

identifier = Word(alphas, alphanums + "_")
