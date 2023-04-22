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

datasetpath = "trainingdata/evangeligaudium"

# Datasetpath is wrong
if (not os.path.exists(datasetpath)):
    logging.error('Dataset path does not exist. Please check the path.')
    sys.exit(-1)

# Data set load and create if not exists
db_index = None
if (not os.path.exists(f'{datasetpath}.json')):
    logging.info('Creating database...')
    db_documents = SimpleDirectoryReader(datasetpath).load_data()
    db_index = GPTSimpleVectorIndex.from_documents(db_documents)
    db_index.save_to_disk(f"{datasetpath}.json")

if (db_index is None):
    logging.info('Loading database...')
    db_index = GPTSimpleVectorIndex.load_from_disk(f"{datasetpath}.json")

prompt = input("Podaj zapytanie:")
response = db_index.query(prompt)

print("Odpowiedź: " + str(response))
print("Źródła : "+ response.get_formatted_sources())