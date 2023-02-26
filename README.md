# Gout-Bot
使用Rasa建立痛风相关问答系统


《痛风大全》 pdf-- 痛风病友群房哥和痛风快好整理提供

step1 把pdf中的问答，抽取出来

python pdf_extract.py

step2 在excel 修正抽取的结构保存 为[手动编辑结果](data/tsv/痛风问答_excel编辑结果.txt)

step3:

rasa_data_gather.py 从编辑的问答表格生成，nlu.yml 和domain.yml
或者 excel_to_rasa_data.py 把数据excel 转换为nlu.yml 和 domain.yml
    
