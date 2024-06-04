module encoder (
    input wire [63:0] data_in,
    output wire [127:0] data_out
);

    reg [10:0] data_blocks [0:7];
    reg [15:0] encoded_blocks [0:7];
    integer i;

    // Initialize data blocks
    always @* begin
        for (i = 0; i < 8; i = i + 1) begin
            data_blocks[i] = data_in[i*8 +: 8];
        end
    end

    // Hamming encoding for each block
    always @* begin
        for (i = 0; i < 8; i = i + 1) begin : Hamming_calc
  
// Hamming Bits
encoded_blocks[i][15] = ^data_blocks[i];
// 2. & 4. Column
            encoded_blocks[i][14] = data_blocks[i][7] ^ data_blocks[i][6] ^ data_blocks[i][4] ^ data_blocks[i][3] ^ data_blocks[i][1];
// 3. & 4. Column
            encoded_blocks[i][13] = data_blocks[i][7] ^ data_blocks[i][5] ^ data_blocks[i][4] ^ data_blocks[i][2] ^ data_blocks[i][1];
// 2. & 4. Row
            encoded_blocks[i][11] = data_blocks[i][6] ^ data_blocks[i][5] ^ data_blocks[i][4] ^ data_blocks[i][0];
// 3. & 4. Row
            encoded_blocks[i][7] = data_blocks[i][3] ^ data_blocks[i][2] ^ data_blocks[i][1] ^ data_blocks[i][0];

// Data Bits
            encoded_blocks[i][12] = data_blocks[i][7];
            encoded_blocks[i][10] = data_blocks[i][6];
            encoded_blocks[i][9] = data_blocks[i][5];
            encoded_blocks[i][8] = data_blocks[i][4];
            encoded_blocks[i][6] = data_blocks[i][3];
            encoded_blocks[i][5] = data_blocks[i][2];
            encoded_blocks[i][4] = data_blocks[i][1];
            encoded_blocks[i][3] = data_blocks[i][0];

            encoded_blocks[i][2] = 'b0;
            encoded_blocks[i][1] = 'b0;
encoded_blocks[i][0] = 'b0;
        end
    end

    // Concatenate encoded blocks into output
    assign data_out = {encoded_blocks[7], encoded_blocks[6], encoded_blocks[5], encoded_blocks[4], encoded_blocks[3], encoded_blocks[2], encoded_blocks[1], encoded_blocks[0]};

endmodule