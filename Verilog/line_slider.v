module line_slider (
    input wire [7:0] column0,
    input wire [7:0] column1,
    input wire [7:0] column2,
    input wire [7:0] column3,
    input wire [7:0] column4,
    input wire [7:0] column5,
    input wire [7:0] column6,
    input wire [7:0] column7,
    output reg [15:0] final_column0,
    output reg [15:0] final_column1,
    output reg [15:0] final_column2,
    output reg [15:0] final_column3,
    output reg [15:0] final_column4,
    output reg [15:0] final_column5,
    output reg [15:0] final_column6,
    output reg [15:0] final_column7
);

initial begin
    final_column0 = {8'b00000000, column0};
    final_column1 = {8'b00000000, column1};
    final_column2 = {8'b00000000, column2};
    final_column3 = {8'b00000000, column3};
    final_column4 = {8'b00000000, column4};
    final_column5 = {8'b00000000, column5};
    final_column6 = {8'b00000000, column6};
    final_column7 = {8'b00000000, column7};

    // Slide bits by number of the columns *2
    final_column0 = {final_column0[15], final_column0[14], final_column0[13], final_column0[12], final_column0[11], final_column0[10], final_column0[9], final_column0[8], final_column0[7], final_column0[6], final_column0[5], final_column0[4], final_column0[3], final_column0[2], final_column0[1], final_column0[0]};
    final_column1 = {final_column1[13], final_column1[12], final_column1[11], final_column1[10], final_column1[9], final_column1[8], final_column1[7], final_column1[6], final_column1[5], final_column1[4], final_column1[3], final_column1[2], final_column1[1], final_column1[0], final_column1[15], final_column1[14]};
    final_column2 = {final_column2[11], final_column2[10], final_column2[9], final_column2[8], final_column2[7], final_column2[6], final_column2[5], final_column2[4], final_column2[3], final_column2[2], final_column2[1], final_column2[0], final_column2[15], final_column2[14], final_column2[13], final_column2[12]};
    final_column3 = {final_column3[9], final_column3[8], final_column3[7], final_column3[6], final_column3[5], final_column3[4], final_column3[3], final_column3[2], final_column3[1], final_column3[0], final_column3[15], final_column3[14], final_column3[13], final_column3[12], final_column3[11], final_column3[10]};
    final_column4 = {final_column4[7], final_column4[6], final_column4[5], final_column4[4], final_column4[3], final_column4[2], final_column4[1], final_column4[0], final_column4[15], final_column4[14], final_column4[13], final_column4[12], final_column4[11], final_column4[10], final_column4[9], final_column4[8]};
    final_column5 = {final_column5[5], final_column5[4], final_column5[3], final_column5[2], final_column5[1], final_column5[0], final_column5[15], final_column5[14], final_column5[13], final_column5[12], final_column5[11], final_column5[10], final_column5[9], final_column5[8], final_column5[7], final_column5[6]};
    final_column6 = {final_column6[3], final_column6[2], final_column6[1], final_column6[0], final_column6[15], final_column6[14], final_column6[13], final_column6[12], final_column6[11], final_column6[10], final_column6[9], final_column6[8], final_column6[7], final_column6[6], final_column6[5], final_column6[4]};
    final_column7 = {final_column7[1], final_column7[0], final_column7[15], final_column7[14], final_column7[13], final_column7[12], final_column7[11], final_column7[10], final_column7[9], final_column7[8], final_column7[7], final_column7[6], final_column7[5], final_column7[4], final_column7[3], final_column7[2]};
end

endmodule
