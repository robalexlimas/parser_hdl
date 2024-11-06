entity alu is
  port (
    A : in  std_logic;
    B : in  std_logic;
    Y : out std_logic
  );
end entity;

architecture behavioral of alu is
  signal temp : std_logic;
begin
  U1: component Adder
    port map (
      A => A,
      B => B,
      S => temp
    );
end architecture;
