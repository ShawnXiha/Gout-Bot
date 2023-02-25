import csv

domain_file = open('data/domain.yml', 'w')
nlu_file = open('data/nlu.yml', 'w')

domain_file.write("intents:\n")
nlu_file.write("version: '2.0'\n\nnlu:\n")

with open('data/tsv/痛风问答_excel编辑结果.txt') as tsv_file:
    tsv_reader = csv.reader(tsv_file, delimiter='\t')
    next(tsv_reader)  # skip header row

    intents = {}
    responses = {}
    for row in tsv_reader:
        intent_name = row[0].replace(" ", "_").lower()
        question = row[1]
        answer = row[2]
        responses[intent_name] = answer
        if intent_name not in intents:
            intents[intent_name] = []

        intents[intent_name].append(question)

        domain_file.write(f"  - {intent_name}\n")

        nlu_file.write(f"- intent: {intent_name}\n  examples: |\n")
        nlu_file.write(f"    - {question}\n\n")

    domain_file.write("\nresponses:\n")

    for intent_name, questions in intents.items():
        intent_name = intent_name.replace("_", " ")
        domain_file.write(f"  {intent_name}:\n    - text: {responses[intent_name]}\n\n")

domain_file.close()
nlu_file.close()
