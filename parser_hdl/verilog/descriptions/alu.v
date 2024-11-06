module alu (
    input A,
    input B,
    output Y
);
    wire temp;
    
    adder U1 (
        .A(A),
        .B(B),
        .S(temp)
    );

endmodule