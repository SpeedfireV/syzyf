module decoder (
    input wire [127:0] data_in,
    output wire [63:0] data_out,
    output wire [7:0] error_positions
);

    reg [15:0] data_blocks [0:7];
	 reg [7:0] output_message [0:7];
    reg [7:0] decoded_blocks [0:7];
    reg [3:0] error_positions_internal [0:7];
    integer i;

    // Initialize data blocks
    always @* begin
        for (i = 0; i < 8; i = i + 1) begin: block_divider
            data_blocks[i] = data_in[i*16 +: 16];
        end
    end

    // Hamming decoding for each block
    always @* begin
        for (i = 0; i < 8; i = i + 1) begin: parity_calculation
            // Check parity bits
            reg [3:0] parity_bits;
            reg overall_parity;
            reg [3:0] error_position;
				// 2. & 4. Columns
            parity_bits[0] = data_blocks[i][14] ^ data_blocks[i][12] ^ data_blocks[i][10] ^ data_blocks[i][8] ^ data_blocks[i][6] ^ data_blocks[i][4];
            // 3. & 4. Columns
				parity_bits[1] = data_blocks[i][13] ^ data_blocks[i][12] ^ data_blocks[i][9] ^ data_blocks[i][8] ^ data_blocks[i][5] ^ data_blocks[i][4];
            // 2. & 4. Rows
				parity_bits[2] = data_blocks[i][11] ^ data_blocks[i][10] ^ data_blocks[i][9] ^ data_blocks[i][8] ^ data_blocks[i][3];
            // 3. & 4. Rows
				parity_bits[3] = data_blocks[i][7] ^ data_blocks[i][6] ^ data_blocks[i][5] ^ data_blocks[i][4] ^ data_blocks[i][3];
            // Whole Block Parity
				overall_parity = ^data_blocks[i];

            // Calculate error position
            error_position = {parity_bits[3], parity_bits[2], parity_bits[1], parity_bits[0]};

            
				$display(error_position);
				case (error_position)
					4'b0011: begin
								output_message[i][7] = ~data_blocks[i][12];
								output_message[i][6] = data_blocks[i][10];
								output_message[i][5] = data_blocks[i][9];
								output_message[i][4] = data_blocks[i][8];
								output_message[i][3] = data_blocks[i][6];
								output_message[i][2] = data_blocks[i][5];  
								output_message[i][1] = data_blocks[i][4];
								output_message[i][0] = data_blocks[i][3]; 
								end
					4'b0101: begin
								$display(data_blocks[i][0]);
								$display(data_blocks[i][1]);
								$display(data_blocks[i][2]);
								$display(data_blocks[i][3]);
								$display(data_blocks[i][4]);
								$display(data_blocks[i][5]);
								$display(data_blocks[i][6]);
								$display(data_blocks[i][7]);
								$display(data_blocks[i][8]);
								$display(data_blocks[i][9]);
								$display(data_blocks[i][10]);
								$display(data_blocks[i][11]);
								$display(data_blocks[i][12]);
								$display(data_blocks[i][13]);
								$display(data_blocks[i][14]);
								$display(data_blocks[i][15]);
								output_message[i][7] = data_blocks[i][12];
								output_message[i][6] = ~data_blocks[i][10];
								output_message[i][5] = data_blocks[i][9];
								output_message[i][4] = data_blocks[i][8];
								output_message[i][3] = data_blocks[i][6];
								output_message[i][2] = data_blocks[i][5];  
								output_message[i][1] = data_blocks[i][4];
								output_message[i][0] = data_blocks[i][3]; 
								end
					4'b0110: begin
								output_message[i][7] = data_blocks[i][12];
								output_message[i][6] = data_blocks[i][10];
								output_message[i][5] = ~data_blocks[i][9];
								output_message[i][4] = data_blocks[i][8];
								output_message[i][3] = data_blocks[i][6];
								output_message[i][2] = data_blocks[i][5];  
								output_message[i][1] = data_blocks[i][4];
								output_message[i][0] = data_blocks[i][3]; 
								end
					4'b0111: begin
								output_message[i][7] = data_blocks[i][12];
								output_message[i][6] = data_blocks[i][10];
								output_message[i][5] = data_blocks[i][9];
								output_message[i][4] = ~data_blocks[i][8];
								output_message[i][3] = data_blocks[i][6];
								output_message[i][2] = data_blocks[i][5];  
								output_message[i][1] = data_blocks[i][4];
								output_message[i][0] = data_blocks[i][3]; 
								end
					4'b1001: begin
								output_message[i][7] = data_blocks[i][12];
								output_message[i][6] = data_blocks[i][10];
								output_message[i][5] = data_blocks[i][9];
								output_message[i][4] = data_blocks[i][8];
								output_message[i][3] = ~data_blocks[i][6];
								output_message[i][2] = data_blocks[i][5];  
								output_message[i][1] = data_blocks[i][4];
								output_message[i][0] = data_blocks[i][3]; 
								end
					4'b1010: begin
								output_message[i][7] = data_blocks[i][12];
								output_message[i][6] = data_blocks[i][10];
								output_message[i][5] = data_blocks[i][9];
								output_message[i][4] = data_blocks[i][8];
								output_message[i][3] = data_blocks[i][6];
								output_message[i][2] = ~data_blocks[i][5];  
								output_message[i][1] = data_blocks[i][4];
								output_message[i][0] = data_blocks[i][3]; 
								end
					4'b1011: begin
								output_message[i][7] = data_blocks[i][12];
								output_message[i][6] = data_blocks[i][10];
								output_message[i][5] = data_blocks[i][9];
								output_message[i][4] = data_blocks[i][8];
								output_message[i][3] = data_blocks[i][6];
								output_message[i][2] = data_blocks[i][5];  
								output_message[i][1] = ~data_blocks[i][4];
								output_message[i][0] = data_blocks[i][3]; 
								end
					4'b1100: begin
								output_message[i][7] = data_blocks[i][12];
								output_message[i][6] = data_blocks[i][10];
								output_message[i][5] = data_blocks[i][9];
								output_message[i][4] = data_blocks[i][8];
								output_message[i][3] = data_blocks[i][6];
								output_message[i][2] = data_blocks[i][5];  
								output_message[i][1] = data_blocks[i][4];
								output_message[i][0] = ~data_blocks[i][3]; 
								end
					default: begin
								$display(data_blocks[i][0]);
								$display(data_blocks[i][1]);
								$display(data_blocks[i][2]);
								$display(data_blocks[i][3]);
								$display(data_blocks[i][4]);
								$display(data_blocks[i][5]);
								$display(data_blocks[i][6]);
								$display(data_blocks[i][7]);
								$display(data_blocks[i][8]);
								$display(data_blocks[i][9]);
								$display(data_blocks[i][10]);
								$display(data_blocks[i][11]);
								$display(data_blocks[i][12]);
								$display(data_blocks[i][13]);
								$display(data_blocks[i][14]);
								$display(data_blocks[i][15]);
								
								output_message[i][7] = data_blocks[i][12];
								output_message[i][6] = data_blocks[i][10];
								output_message[i][5] = data_blocks[i][9];
								output_message[i][4] = data_blocks[i][8];
								output_message[i][3] = data_blocks[i][6];
								output_message[i][2] = data_blocks[i][5];
								output_message[i][1] = data_blocks[i][4];
								output_message[i][0] = data_blocks[i][3];
								end
				endcase
					
						
					
            // Extract the original 8-bit data
            decoded_blocks[i] = output_message[i];
            error_positions_internal[i] = error_position;
        end
    end

    // Concatenate decoded blocks into output
    assign data_out = {decoded_blocks[7], decoded_blocks[6], decoded_blocks[5], decoded_blocks[4], decoded_blocks[3], decoded_blocks[2], decoded_blocks[1], decoded_blocks[0]};
    assign error_positions = {error_positions_internal[0], error_positions_internal[1], error_positions_internal[2], error_positions_internal[3], error_positions_internal[4], error_positions_internal[5], error_positions_internal[6], error_positions_internal[7]};

endmodule
