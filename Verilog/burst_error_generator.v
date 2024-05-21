module burst_error_generator(
    input clk,
    input [63:0] message,
    output reg [63:0] error_message,
    output reg [6:0] burst_start,
    output reg [2:0] burst_length
);
    reg [6:0] burst_end;
    integer i;
    always @(posedge clk) begin
        burst_start = $urandom % 64;
        burst_length = (64 - burst_start < 8) ? ($urandom % (64 - burst_start)) : ($urandom % 6 + 2);
        burst_end = burst_start + burst_length;

        error_message = message;
        for (i = burst_start; i <= burst_end; i = i + 1) begin
            if ($urandom % 2 == 1 || i == burst_start || i == burst_end) begin
                error_message[i] = ~message[i];
            end
        end
    end
endmodule