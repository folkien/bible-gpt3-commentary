'''
This script creates a vector database from texts with
llama_index.
'''
import logging
import sys
import os 
from llama_index import (
    GPTSimpleVectorIndex, 
    GPTSimpleKeywordTableIndex, 
    GPTListIndex, 
    SimpleDirectoryReader
)

# Setup logging and configure basics
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))



# Data set load and create if not exists
db_index = None
if (not os.path.exists('trainingdata/sesa.json')):
    logging.info('Creating database...')
    db_documents = SimpleDirectoryReader('trainingdata/sesa').load_data()
    db_index = GPTSimpleVectorIndex.from_documents(db_documents)
    db_index.save_to_disk('trainingdata/sesa.json')

if (db_index is None):
    logging.info('Loading database...')
    db_index = GPTSimpleVectorIndex.load_from_disk('trainingdata/sesa.json')

prompt = input("Podaje zapytanie do ewangelizatora:")
response = db_index.query(prompt)

print("Odpowiedź: " + str(response))
print("Źródła : "+ response.get_formatted_sources())