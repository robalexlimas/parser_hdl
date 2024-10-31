-- Sumador completo de 1 bit
library IEEE;
  use IEEE.STD_LOGIC_1164.all;

entity adder_bit is
  port (
    A    : in  STD_LOGIC;
    B    : in  STD_LOGIC;
    Cin  : in  STD_LOGIC;
    Sum  : out STD_LOGIC;
    Cout : out STD_LOGIC
  );
end entity;

architecture behavioral of adder_bit is
begin
  Sum  <= A xor B xor Cin;
  Cout <= (A and B) or (Cin and (A xor B));
end architecture;
