#!/bin/bash

# Directory containing .in files
input_directory="x3dna_sec_struct_pt2"
output_directory="sequence_designs_x3dna"

# Iterate through all .in files in the directory
for file in "$input_directory"/*.in
do
  # Check if the file exists to avoid errors in case the directory is empty
  if [ -f "$file" ]; then
    # Extract the base filename without extension (e.g., id from id.in)
    base_filename=$(basename "$file" .in)

    # Run the RNAinverse command with -R16 option and redirect output to a .txt file
    RNAinverse -R16 < "$file" > "$output_directory/$base_filename.txt"

    echo "Processed: $file -> $base_filename.txt"
  fi
done
