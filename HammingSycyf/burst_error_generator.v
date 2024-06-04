module burst_error_generator (
    input [127:0] data_in,
    output reg [127:0] data_out,
    input [7:0] error_0,
input [7:0] error_1,
input [7:0] error_2,
input [7:0] error_3,
input [7:0] error_4,
input [7:0] error_5,
input [7:0] error_6,
input [7:0] error_7,
input [7:0] error_8,
input [7:0] error_9,
input [7:0] error_10,
input [7:0] error_11,
input [7:0] error_12,
input [7:0] error_13,
input [7:0] error_14,
input [7:0] error_15
 
);


always @(*) begin
    data_out = data_in;
 if (!(error_0 == 'b10000000))
data_out[error_0] = ~ data_out[error_0];
if (!(error_0 == 'b10000000)) begin
data_out[error_0] = ~ data_out[error_0];
end
if (!(error_1 == 'b10000000)) begin
data_out[error_1] = ~ data_out[error_1];
end
if (!(error_2 == 'b10000000)) begin
data_out[error_2] = ~ data_out[error_2];
end
if (!(error_3 == 'b10000000)) begin
data_out[error_3] = ~ data_out[error_3];
end
if (!(error_4 == 'b10000000)) begin
data_out[error_4] = ~ data_out[error_4];
end
if (!(error_5 == 'b10000000)) begin
data_out[error_5] = ~ data_out[error_5];
end
if (!(error_6 == 'b10000000)) begin
data_out[error_6] = ~ data_out[error_6];
end
if (!(error_7 == 'b10000000)) begin
data_out[error_7] = ~ data_out[error_7];
end
if (!(error_8 == 'b10000000)) begin
data_out[error_8] = ~ data_out[error_8];
end
if (!(error_9 == 'b10000000)) begin
data_out[error_9] = ~ data_out[error_9];
end
if (!(error_10 == 'b10000000)) begin
data_out[error_10] = ~ data_out[error_10];
end
if (!(error_11 == 'b10000000)) begin
data_out[error_11] = ~ data_out[error_11];
end
if (!(error_12 == 'b10000000)) begin
data_out[error_12] = ~ data_out[error_12];
end
if (!(error_13 == 'b10000000)) begin
data_out[error_13] = ~ data_out[error_13];
end
if (!(error_14 == 'b10000000)) begin
data_out[error_14] = ~ data_out[error_14];
end
if (!(error_15 == 'b10000000)) begin
data_out[error_15] = ~ data_out[error_15];
end


    
end

endmodule