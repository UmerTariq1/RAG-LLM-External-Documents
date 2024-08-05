# python script_name.py data/output/hackmd_processed.txt data/output/splitted

import os
import argparse

def split_into_files(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_heading1 = ''
    current_heading2 = ''
    current_body = []
    file_index = 1

    for line in lines:
        line = line.strip()

        if line.startswith('Heading 1:'):
            current_heading1 = line[11:].strip()
        elif line.startswith('Heading 2:'):
            # Write the previous section to a file
            if current_heading2:
                output_path = os.path.join(output_dir, f'section_{file_index}.txt')
                with open(output_path, 'w', encoding='utf-8') as out_file:
                    out_file.write(f'Heading 1: {current_heading1}\n')
                    out_file.write(f'Heading 2: {current_heading2}\n')
                    out_file.write('Body:\n')
                    out_file.write('\n'.join(current_body))
                file_index += 1
                current_body = []

            current_heading2 = line[11:].strip()
        elif line.startswith('Body:'):
            current_body = []
        else:
            if line:
                current_body.append(line)

    # Write the last section to a file
    if current_heading2:
        output_path = os.path.join(output_dir, f'section_{file_index}.txt')
        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(f'Heading 1: {current_heading1}\n')
            out_file.write(f'Heading 2: {current_heading2}\n')
            out_file.write('Body:\n')
            out_file.write('\n'.join(current_body))

def main():
    parser = argparse.ArgumentParser(description='Split processed Markdown file into multiple files based on Heading 2')
    parser.add_argument('input_file', type=str, help='Path to the input processed Markdown file')
    parser.add_argument('output_dir', type=str, help='Directory to save the split files')

    args = parser.parse_args()
    split_into_files(args.input_file, args.output_dir)
    print(f'Splitting complete. The files have been saved to {args.output_dir}')

if __name__ == '__main__':
    main()
