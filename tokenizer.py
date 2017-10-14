import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download("all")

example_text = """The fifth round of monthly Brexit talks between the UK and the EU has taken place, with a decision due to be taken by the EU later in October on
whether or not enough progress has been made on "separation issues" to be able to start talks about the future relationship between the UK and the EU after Brexit.
Theresa May tried to speed up progress with a speech in Florence, Italy, in which she called for trade with the EU to continues as it is for two years after Britain
leaves, but EU figures say not enough progress has been made yet. EU negotiator Michel Barnier has said it could be \"weeks or months\" before the talks move on to
the next stage."""

stop_words = set(stopwords.words("english"))
words = word_tokenize(example_text)

filtered_text = []

for word in words:
    if word not in stop_words:
        filtered_text.append(word)

print("Sentences:")
print(sent_tokenize(example_text))
print("\n")
print("Words:")
print(word_tokenize(example_text))
print(len(word_tokenize(example_text)))
print("\n")
print("Stop words removed")
print(filtered_text)
print(len(filtered_text))
