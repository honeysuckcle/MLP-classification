import torch
from transformers import BertTokenizer, BertModel
import pandas as pd
# import matplotlib.pyplot as plt

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

train_words = pd.read_csv('../data/train_description_en.csv')
test_words = pd.read_csv('../data/test_description_en.csv')

en_text = "Here is the sentence I want embeddings for."
ch_text = "这是我们需要进行向量化的句子。"
marked_text = "[CLS] " + en_text +  ch_text + "[SEP]"

# Tokenize our sentence with the BERT tokenizer.
tokenized_text = tokenizer.tokenize(marked_text)

# Print out the tokens.
print (tokenized_text)