module main (
    input wire clk,
    input wire rst,
    input wire [63:0] data_in,
    output reg [127:0] whole_message_out,
    output reg [7:0] error_position_0_out,
    output reg [7:0] error_position_1_out,
    output reg [7:0] error_position_2_out,
    output reg [7:0] error_position_3_out,
    output reg [7:0] error_position_4_out,
    output reg [7:0] error_position_5_out,
    output reg [7:0] error_position_6_out,
    output reg [7:0] error_position_7_out,
    output reg [7:0] error_position_8_out,
    output reg [7:0] error_position_9_out,
    output reg [7:0] error_position_10_out,
    output reg [7:0] error_position_11_out,
    output reg [7:0] error_position_12_out,
    output reg [7:0] error_position_13_out,
    output reg [7:0] error_position_14_out,
    output reg [7:0] error_position_15_out
);

wire [15:0] data_formatted_column0;
wire [15:0] data_formatted_column1;
wire [15:0] data_formatted_column2;
wire [15:0] data_formatted_column3;
wire [15:0] data_formatted_column4;
wire [15:0] data_formatted_column5;
wire [15:0] data_formatted_column6;
wire [15:0] data_formatted_column7;

line_slider line_slider_inst(
    .column0(data_formatted_column0),
    .column1(data_formatted_column1),
    .column2(data_formatted_column2),
    .column3(data_formatted_column3),
    .column4(data_formatted_column4),
    .column5(data_formatted_column5),
    .column6(data_formatted_column6),
    .column7(data_formatted_column7),
    .final_column0(final_column0),
    .final_column1(final_column1),
    .final_column2(final_column2),
    .final_column3(final_column3),
    .final_column4(final_column4),
    .final_column5(final_column5),
    .final_column6(final_column6),
    .final_column7(final_column7)
);

data_formatter data_formatter_inst(
    .data(data_in),
    .column0(data_formatted_column0),
    .column1(data_formatted_column1),
    .column2(data_formatted_column2),
    .column3(data_formatted_column3),
    .column4(data_formatted_column4),
    .column5(data_formatted_column5),
    .column6(data_formatted_column6),
    .column7(data_formatted_column7),
    .row0(row0),
    .row1(row1),
    .row2(row2),
    .row3(row3),
    .row4(row4),
    .row5(row5),
    .row6(row6),
    .row7(row7)
);

encoder encoder_inst(
    .data(data_formatter_inst),
    .debug_mode(1'b0), // Change to 1'b1 for debugging
    .whole_message(whole_message)
);

decoder decoder_inst(
    .received_message(whole_message),
    .number_of_rows(16), // Placeholder, provide correct value
    .debug_mode(1'b0), // Change to 1'b1 for debugging
    .error_position_0(error_position_0),
    .error_position_1(error_position_1),
    .error_position_2(error_position_2),
    .error_position_3(error_position_3),
    .error_position_4(error_position_4),
    .error_position_5(error_position_5),
    .error_position_6(error_position_6),
    .error_position_7(error_position_7),
    .error_position_8(error_position_8),
    .error_position_9(error_position_9),
    .error_position_10(error_position_10),
    .error_position_11(error_position_11),
    .error_position_12(error_position_12),
    .error_position_13(error_position_13),
    .error_position_14(error_position_14),
    .error_position_15(error_position_15)
);

transmission transmission_inst(
    .clk(clk),
    .rst(rst),
    .data_in(data_formatter_inst),
    .data_out(data_out)
);

endmodule
