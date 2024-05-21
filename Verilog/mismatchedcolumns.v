module mismatchedcolumns (
    input wire [7:0] decoded_top_column_parities,
    input wire [7:0] decoded_bottom_column_parities,
    input wire [15:0] decoded_row_parities,
    input wire [7:0] received_top_column_parities,
    input wire [7:0] received_bottom_column_parities,
    input wire [15:0] received_row_parities,
    output reg [7:0] top_errors,
    output reg [7:0] bottom_errors,
    output reg [15:0] row_errors
);

integer i;

always @(decoded_top_column_parities or received_top_column_parities) begin
    top_errors = 8'b00000000;
    for (i = 0; i < 8; i = i + 1) begin
        if (decoded_top_column_parities[i] != received_top_column_parities[i]) begin
            top_errors[i] = 1;
        end
    end
end

always @(decoded_bottom_column_parities or received_bottom_column_parities) begin
    bottom_errors = 8'b00000000;
    for (i = 0; i < 8; i = i + 1) begin
        if (decoded_bottom_column_parities[i] != received_bottom_column_parities[i]) begin
            bottom_errors[i] = 1;
        end
    end
end

always @(decoded_row_parities or received_row_parities) begin
    row_errors = 16'b0000000000000000;
    for (i = 0; i < 16; i = i + 1) begin
        if (decoded_row_parities[i] != received_row_parities[i]) begin
            row_errors[i] = 1;
        end
    end
end

endmodule
