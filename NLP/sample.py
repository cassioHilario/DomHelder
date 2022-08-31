import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')


frase = 'Hi class, Today I wanna know about NLP'
print(sent_tokenize(frase))