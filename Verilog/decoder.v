module decoder (
    input wire [127:0] received_message,
    input wire number_of_rows,
    input wire debug_mode,
    output reg [7:0] error_position_0,
    output reg [7:0] error_position_1,
    output reg [7:0] error_position_2,
    output reg [7:0] error_position_3,
    output reg [7:0] error_position_4,
    output reg [7:0] error_position_5,
    output reg [7:0] error_position_6,
    output reg [7:0] error_position_7,
    output reg [7:0] error_position_8,
    output reg [7:0] error_position_9,
    output reg [7:0] error_position_10,
    output reg [7:0] error_position_11,
    output reg [7:0] error_position_12,
    output reg [7:0] error_position_13,
    output reg [7:0] error_position_14,
    output reg [7:0] error_position_15
);

reg [63:0] information_bits;
reg [7:0] slided_message [15:0];
reg [7:0] received_row_parities;
reg [7:0] received_top_column_parities;
reg [7:0] received_bottom_column_parities;
reg [7:0] decoded_row_parities;
reg [7:0] decoded_top_column_parities;
reg [7:0] decoded_bottom_column_parities;
reg [7:0] row_parity_errors;
reg [7:0] top_column_parity_errors;
reg [7:0] bottom_column_parity_errors;

integer i;

always @(*) begin
    if (debug_mode) begin
        $display("#DECODER#");
    end

    // Slice received_message to get information_bits
    information_bits = received_message[127:64];

    // Call slide_lines function
    // Assign output to slided_message

    // Slice received_message to get received_row_parities,
    // received_top_column_parities, and received_bottom_column_parities

    if (debug_mode) begin
        $display("SLIDED RECEIVED MESSAGE WITH PARITY CHECK:");
    end

    // Call get_table_parities function
    // Assign output to decoded_row_parities, decoded_top_column_parities, and decoded_bottom_column_parities

    // Calculate row_parity_errors, top_column_parity_errors, and bottom_column_parity_errors

    // Calculate error_positions based on the errors detected

    // Assign error_positions to output reg signals
end

endmodule
