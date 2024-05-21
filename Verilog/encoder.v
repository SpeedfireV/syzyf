module encoder (
    input wire [63:0] data,
    input wire debug_mode,
    output reg [127:0] whole_message
);

wire [7:0] slided_message [15:0];
wire [7:0] additional_bits [15:0];

integer i;

always @(*) begin
    if (debug_mode) begin
        $display("#ENCODER#");
        $display("ORIGINAL MESSAGE:");
        for (i = 0; i < 8; i = i + 1) begin
            $display("%b", data[i*8 +: 8]);
        end
    end

    // Call slide_lines function
    // Assign output to slided_message

    if (debug_mode) begin
        $display("SLIDED MESSAGE WITH PARITY CHECKS!:");
    end

    // Call get_table_parities function
    // Assign output to additional_bits

    // Concatenate data and additional_bits to form whole_message
    whole_message = data;
    for (i = 0; i < 16; i = i + 1) begin
        whole_message = {whole_message, additional_bits[i]};
    end
end

endmodule
