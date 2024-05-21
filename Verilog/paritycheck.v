module paritycheck (
    input wire [7:0] cloumn_or_row,
    output reg value_check
);

integer i;

always @(cloumn_or_row) begin
    value_check = 0;  // initialize count variable.
    for (i = 0; i < 8; i = i + 1) begin
        if (cloumn_or_row[i] == 1'b1) begin // check if the bit is '1'
            value_check = value_check + 1;  // if its one, increment the count.
        end
    end
    value_check = value_check % 2;
end

endmodule
