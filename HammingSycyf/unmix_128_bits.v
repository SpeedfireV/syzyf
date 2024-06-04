module unmix_128_bits (
    input wire [127:0] data_in,
    output wire [127:0] data_out
);

    genvar i;
    generate
        for (i = 0; i < 128; i = i + 1) begin : unmix_bits
            assign data_out[(i % 16) * 8 + i / 16] = data_in[i];
        end
    endgenerate

endmodule