module mix_128_bits (
    input wire [127:0] data_in,
    output wire [127:0] data_out
);

    genvar i;
    generate
        for (i = 0; i < 128; i = i + 1) begin : mix_bits
            assign data_out[i] = data_in[(i % 16) * 8 + i / 16];
        end
    endgenerate

endmodule