import os
import csv
import json
import PyPDF2


def parse_pdf(file_path):
    log_data = []
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            log_data.extend(text.split('\n'))
    return log_data

def parse_csv(file_path):
    log_data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            log_data.append(row)
    return log_data

def parse_txt(file_path):
    log_data = []
    with open(file_path, 'r') as txt_file:
        log_data = txt_file.readlines()
    return log_data

def parse_json(file_path):
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
    return json_data
def transpose_data(data):
    return list(map(list, zip(*data)))

def parse(log_file_path, ruleset_file_path):
    log_data = []
    ruleset_data = []

    if os.path.exists(log_file_path):
        log_file_extension = os.path.splitext(log_file_path)[1].lower()

        if log_file_extension == '.pdf':
            log_data = parse_pdf(log_file_path)
        elif log_file_extension == '.csv':
            log_data = parse_csv(log_file_path)
        elif log_file_extension == '.txt':
            log_data = parse_txt(log_file_path)
        else:
            print("Unsupported log file format.")

    if os.path.exists(ruleset_file_path):
        ruleset_file_extension = os.path.splitext(ruleset_file_path)[1].lower()

        if ruleset_file_extension == '.pdf':
            ruleset_data = parse_pdf(ruleset_file_path)
        elif ruleset_file_extension == '.csv':
            ruleset_data = parse_csv(ruleset_file_path)
        elif ruleset_file_extension == '.txt':
            ruleset_data = parse_txt(ruleset_file_path)
        elif ruleset_file_extension == '.json':
            ruleset_data = parse_json(ruleset_file_path)
        else:
            print("Unsupported ruleset file format.")


    return [log_data, ruleset_data]
    # print("Log Data (row wise):")
    # print(log_data)


    # print("\nRuleset Data:")
    # print(ruleset_data)