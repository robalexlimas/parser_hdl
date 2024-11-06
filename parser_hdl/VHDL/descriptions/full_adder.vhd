-- Sumador completo de n bits
library IEEE;
  use IEEE.STD_LOGIC_1164.all;

entity full_adder is
  generic (
    N : integer := 4
  );
  port (
    A    : in  STD_LOGIC_VECTOR(N - 1 downto 0);
    B    : in  STD_LOGIC_VECTOR(N - 1 downto 0);
    Cin  : in  STD_LOGIC;
    Sum  : out STD_LOGIC_VECTOR(N - 1 downto 0);
    Cout : out STD_LOGIC
  );
end entity;

architecture behavioral of full_adder is
  signal carry : STD_LOGIC_VECTOR(N downto 0);
begin
  carry(0) <= Cin;

  gen_adders: for i in 0 to N - 1 generate
    FA_inst: entity work.adder_bit
      port map (
        A    => A(i),
        B    => B(i),
        Cin  => carry(i),
        Sum  => Sum(i),
        Cout => carry(i + 1)
      );
  end generate;

  Cout <= carry(N);
end architecture;
