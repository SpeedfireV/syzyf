module main (
    input wire [63:0] message,
 input wire [7:0] error_0,
input wire [7:0] error_1,
input wire [7:0] error_2,
input wire [7:0] error_3,
input wire [7:0] error_4,
input wire [7:0] error_5,
input wire [7:0] error_6,
input wire [7:0] error_7,
input wire [7:0] error_8,
input wire [7:0] error_9,
input wire [7:0] error_10,
input wire [7:0] error_11,
input wire [7:0] error_12,
input wire [7:0] error_13,
input wire [7:0] error_14,
input wire [7:0] error_15,
 
    output wire [63:0] decoded_message,
    output wire [7:0] error_positions
);

    wire [127:0] encoded_message;
    wire [127:0] mixed_message;
 wire [127:0] error_message;
    wire [127:0] unmixed_message;

    encoder enc (
        .data_in(message),
        .data_out(encoded_message)
    );

    mix_128_bits mix (
        .data_in(encoded_message),
        .data_out(mixed_message)
    );
 
 burst_error_generator beg (
        .data_in(mixed_message),
  .error_0(error_0),
  .error_1(error_1),
  .error_2(error_2),
  .error_3(error_3),
  .error_4(error_4),
  .error_5(error_5),
  .error_6(error_6),
  .error_7(error_7),
  .error_8(error_8),
  .error_9(error_9),
  .error_10(error_10),
  .error_11(error_11),
  .error_12(error_12),
  .error_13(error_13),
  .error_14(error_14),
  .error_15(error_15),
        .data_out(error_message)
    );

    unmix_128_bits unmix (
        .data_in(error_message),
        .data_out(unmixed_message)
    );

    decoder dec (
        .data_in(unmixed_message),
        .data_out(decoded_message),
        .error_positions(error_positions)
    );

endmodule