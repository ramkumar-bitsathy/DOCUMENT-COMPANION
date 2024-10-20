import streamlit as st
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
import re

# Load model and tokenizer
model_name = "google/pegasus-xsum"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)



# Function to clean text (remove references and select relevant sections)
def clean_text(input_text):
    # Remove anything in square brackets (e.g., references like [1], [2], etc.)
    cleaned_text = re.sub(r'\[[^\]]*\]', '', input_text)

    # Extract the text between "Introduction/Abstract" and "Conclusion/References"
    start_pos = re.search(r'(Introduction|Abstract)', cleaned_text, re.IGNORECASE)
    end_pos = re.search(r'(References)', cleaned_text, re.IGNORECASE)

    if start_pos and end_pos:
        cleaned_text = cleaned_text[start_pos.end():end_pos.start()]
    elif start_pos:
        cleaned_text = cleaned_text[start_pos.end():]
    elif end_pos:
        cleaned_text = cleaned_text[:end_pos.start()]

    return cleaned_text.strip()

# Function to summarize the cleaned text
def summarize_file(input):
    if type(input)==str:
        input_text = clean_text(input)

        if input_text:
            # Tokenize and generate summary
            tokenized_text = tokenizer.encode("summarize: " + input_text, return_tensors='pt', max_length=512, truncation=True).to(device)
            summary_ = model.generate(tokenized_text, min_length=100, max_length=600)
            summary = tokenizer.decode(summary_[0], skip_special_tokens=True)
            return summary
        else:
            return "No valid content to summarize."
    if type(input)==dict:
        summary_dict = dict()
        for key in input.keys():
            input_text = clean_text(input[key])

            if input_text:
                # Tokenize and generate summary
                tokenized_text = tokenizer.encode("summarize: " + input_text, return_tensors='pt', max_length=512, truncation=True).to(device)
                summary_ = model.generate(tokenized_text, min_length=100, max_length=600)
                summary = tokenizer.decode(summary_[0], skip_special_tokens=True)
                summary_dict[key] = summary
            else:
                summary_dict[key] = "Not Enough Content to Summarise."
        return summary_dict


    

