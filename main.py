import sys
import os
from json_to_dataframe import read_json, json_to_dataframe
from dataframe_to_pdf import dataframe_to_pdf

def convert_sbom_to_pdf(json_path, pdf_path):
    json_data = read_json(json_path)
    df = json_to_dataframe(json_data)
    dataframe_to_pdf(json_data, df, pdf_path, json_path)

def process_files_in_directory(directory):
    output_dir = "pdf_conversions"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_path = os.path.join(root, file)
                pdf_path = os.path.join(output_dir, os.path.splitext(file)[0] + ".pdf")
                convert_sbom_to_pdf(json_path, pdf_path)
                print(f"Converted {json_path} to {pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_json_file_or_directory>")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.isfile(input_path) and input_path.endswith(".json"):
        output_dir = "pdf_conversions"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        pdf_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_path))[0] + ".pdf")
        convert_sbom_to_pdf(input_path, pdf_path)
    elif os.path.isdir(input_path):
        process_files_in_directory(input_path)
    else:
        print("Invalid input. Please provide a .json file or a directory containing .json files.")
        sys.exit(1)