import plistlib
import os

def convert_txt_to_nrset(input_file, output_file):
    """
    Reads a space/tab-separated text file and converts it to an
    Apple Property List (.nrset/plist) XML file.
    """
    mapping_data = {}

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    print(f"Reading from {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Split by whitespace (handles tabs or spaces automatically)
            parts = line.split()
            
            # Ensure we have at least a Key and a Value
            if len(parts) >= 2:
                key = parts[0]
                value = parts[1]
                mapping_data[key] = value

    # Write the dictionary to an XML plist file
    print(f"Writing {len(mapping_data)} entries to {output_file}...")
    
    with open(output_file, 'wb') as f:
        # fmt=plistlib.FMT_XML ensures the output is readable XML text
        plistlib.dump(mapping_data, f, fmt=plistlib.FMT_XML, sort_keys=True)

    print("Conversion complete.")

if __name__ == "__main__":
    # Define file names
    input_filename = 'roman.t-code.txt'
    output_filename = 'roman.t-code.nrset'

    convert_txt_to_nrset(input_filename, output_filename)
