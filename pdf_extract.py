
import re


import fitz  # PyMuPDF library
import csv

def question_clean(question):
    return re.sub("^[0-9一二三四]+[，,.、] *",  '', question)

def extract_qa_from_pdf(pdf_path, tsv_path):
    # Open the PDF file
    with fitz.open(pdf_path) as doc:

        # Define a list to store the questions and answers
        qa_list = []
        paragraphs = []
        question_index = []
        # Loop through each page in the PDF
        for page in doc:

            # Extract the text from the page
            text = page.get_text()

            # Split the text into paragraphs
            paragraphs_page = text.split('\n')
            paragraphs += [p.strip() for p in paragraphs_page if p.strip()]
        for i, p in enumerate(paragraphs):
            if "？" == p[-1]:
                question_index.append(i)
        for i, j in zip(question_index, question_index[1:]):
            question = paragraphs[i]
            answer = paragraphs[i+1:j]
            qa_list.append((question, "".join(answer)))
        question = paragraphs[j]
        answer = paragraphs[j+1:]
        qa_list.append((question, "".join(answer)))
        print(qa_list)
    # Save the questions and answers to a TSV file
    with open(tsv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['Question', 'Answer'])
        writer.writerows(qa_list)

def extract_qa_from_pdfs(pdf_paths, tsv_path):
    # Open the PDF file

    # Save the questions and answers to a TSV file
    with open(tsv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['Question', 'Answer'])
        for pdf_path in pdf_paths:
            with fitz.open(pdf_path) as doc:

                # Define a list to store the questions and answers
                qa_list = []
                paragraphs = []
                question_index = []
                # Loop through each page in the PDF
                for page in doc:
                    # Extract the text from the page
                    text = page.get_text()

                    # Split the text into paragraphs
                    paragraphs_page = text.split('\n')
                    paragraphs += [p.strip() for p in paragraphs_page if p.strip()]
                for i, p in enumerate(paragraphs):
                    if '?' in p[-2:] or "？" in p[-2:]:
                        question_index.append(i)
                for i, j in zip(question_index, question_index[1:]):
                    question = paragraphs[i]
                    answer = paragraphs[i + 1:j]
                    qa_list.append((question_clean(question), "".join(answer)))
                question = paragraphs[j]
                answer = paragraphs[j + 1:]
                qa_list.append((question_clean(question), "".join(answer)))
                print(qa_list)
                writer.writerows(qa_list)
if __name__ == '__main__':
    # example_pdf = "data/pdfs/《痛风大全》1，体检篇.pdf"
    # example_tsv = "data/tsv/体检qa.tsv"
    # extract_qa_from_pdf(example_pdf, example_tsv)
    from glob import glob
    pdfs = glob("data/pdfs/《痛风大全》*.pdf")
    all_tsv = "data/tsv/all_qa.tsv"
    extract_qa_from_pdfs(pdfs, all_tsv)