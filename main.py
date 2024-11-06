from parser_hdl import HDLFileParser

file_path_vhdl = "parser_hdl/VHDL/descriptions/alu.vhd"
file_path_verilog = "parser_hdl/verilog/descriptions/alu.v"

hdl_parser_vhdl = HDLFileParser(file_path_vhdl)
result_vhdl = hdl_parser_vhdl.parse_file()
print("VHDL:", result_vhdl)

# hdl_parser_verilog = HDLFileParser(file_path_verilog)
# result_verilog = hdl_parser_verilog.parse_file()
# print("Verilog:", result_verilog)
