`timescale 1ns / 1ps

module testbench;
    // Inputs
    reg [63:0] message;
    reg [7:0] error_0;
    reg [7:0] error_1;
    reg [7:0] error_2;
    reg [7:0] error_3;
    reg [7:0] error_4;
    reg [7:0] error_5;
    reg [7:0] error_6;
    reg [7:0] error_7;
    reg [7:0] error_8;
    reg [7:0] error_9;
    reg [7:0] error_10;
    reg [7:0] error_11;
    reg [7:0] error_12;
    reg [7:0] error_13;
    reg [7:0] error_14;
    reg [7:0] error_15;

    // Outputs
    wire [63:0] decoded_message;
    wire [7:0] error_positions;

    // Clock
    reg clk;

    // Instantiate the Unit Under Test (UUT)
    main uut (
        .message(message),
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
        .decoded_message(decoded_message),
        .error_positions(error_positions)
    );

    // Clock generation
    initial begin
        clk = 0;
        forever #5 clk = ~clk; // 10ns period
    end

    initial begin
        // Initialize Inputs
        message = 64'h0123456789ABCDEF;
        error_0 = 8'b00000000;
        error_1 = 8'b00000001;
        error_2 = 8'b00000010;
        error_3 = 8'b00000011;
        error_4 = 8'b00000100;
        error_5 = 8'b00000101;
        error_6 = 8'b00000110;
        error_7 = 8'b00000111;
        error_8 = 8'b00001000;
        error_9 = 8'b00001001;
        error_10 = 8'b00001010;
        error_11 = 8'b00001011;
        error_12 = 8'b00001100;
        error_13 = 8'b00001101;
        error_14 = 8'b00001110;
        error_15 = 8'b00001111;

        // Wait for global reset to finish
        #100;

        // Add stimulus here
        $display("Message: %h", message);
        $display("Decoded Message: %h", decoded_message);
        $display("Error Positions: %h", error_positions);

        // Test Case 1: No errors
        #10;
        error_0 = 8'b10000000;
        error_1 = 8'b10000000;
        error_2 = 8'b10000000;
        error_3 = 8'b10000000;
        error_4 = 8'b10000000;
        error_5 = 8'b10000000;
        error_6 = 8'b10000000;
        error_7 = 8'b10000000;
        error_8 = 8'b10000000;
        error_9 = 8'b10000000;
        error_10 = 8'b10000000;
        error_11 = 8'b10000000;
        error_12 = 8'b10000000;
        error_13 = 8'b10000000;
        error_14 = 8'b10000000;
        error_15 = 8'b10000000;
        #10;
        $display("Test Case 1");
        $display("Decoded Message: %h", decoded_message);
        $display("Error Positions: %h", error_positions);

        // Test Case 2: Single error
        error_0 = 8'b00000001;
        #10;
        $display("Test Case 2");
        $display("Decoded Message: %h", decoded_message);
        $display("Error Positions: %h", error_positions);

        // Test Case 3: Multiple errors
        error_1 = 8'b00000110;
        error_2 = 8'b00001001;
        #10;
        $display("Test Case 3");
        $display("Decoded Message: %h", decoded_message);
        $display("Error Positions: %h", error_positions);

        // End simulation
        #50;
        $finish;
    end

endmodule