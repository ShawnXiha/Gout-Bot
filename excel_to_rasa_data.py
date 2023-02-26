import pandas as pd

import pandas as pd


def create_rasa_files(nlu_path, domain_path, excel_path):
    # Load data from Excel file
    data = pd.read_excel(excel_path)

    # Create dictionary for intents and responses
    intents = {}
    responses = {}

    domain_file = open(domain_path, 'w', encoding='utf-8')
    nlu_file = open(nlu_path, 'w', encoding='utf-8')

    domain_file.write("versin: '3.1'\n\nintents:\n")
    nlu_file.write("version: '3.1'\n\nnlu:\n")
    # Loop through data and add to dictionary
    for _, row in data.iterrows():
        intent_name = row['Intent']
        question = row['Question']
        answer = row['Answer']

        intents[intent_name] = question.replace("\n", '')

        responses[intent_name] = answer.replace("\n", '')

    for intent_name in intents.keys():
        domain_file.write(f"  - {intent_name}\n")
    domain_file.write(f"\nresponses:\n")
    for intent_name, questions in intents.items():

        domain_file.write(f"  {intent_name}:\n     - text: {responses[intent_name]}\n\n")

        nlu_file.write(f"- intent: {intent_name}\n  examples: |\n")
        nlu_file.write(f"    - {question}\n\n")
    domain_file.close()
    nlu_file.close()
if __name__ == '__main__':
    excel_path = "data/痛风问答.xlsx"
    nlu_path = "data/nlu.yml"
    domain_path = "data/domain.yml"
    create_rasa_files(nlu_path, domain_path, excel_path)
