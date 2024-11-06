from pyparsing import Word, alphas, alphanums, CaselessKeyword

module_kw = CaselessKeyword("module")
endmodule_kw = CaselessKeyword("endmodule")
input_kw = CaselessKeyword("input")
output_kw = CaselessKeyword("output")
wire_kw = CaselessKeyword("wire")

identifier = Word(alphas, alphanums + "_")
