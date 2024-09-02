from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Input text for summarization
text = """
Audio signal processing is a subfield of signal processing that is concerned with 
the electronic manipulation of audio signals. Audio signals are electronic representations 
of sound waves—longitudinal waves which travel through air, consisting of compressions and 
rarefactions. The energy contained in audio signals or sound power level is typically measured 
in decibels. As audio signals may be represented in either digital or analog format, processing 
may occur in either domain. Analog processors operate directly on the electrical signal, while 
digital processors operate mathematically on its digital representation."""

# Summarize the text
summary = summarizer(text, max_length=30, min_length=20, do_sample=False)

# Output the summary
print("Summary:", summary[0]['summary_text'])

print(f"\n\n{len(text)}\n{len(summary[0]['summary_text'])}")
