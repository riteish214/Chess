import nltk
from nltk import CFG
from nltk.parse.chart import ChartParser

# Define a basic grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
PP -> P NP
Det -> 'a' | 'the' | 'my'
N -> 'dog' | 'cat' | 'park' | 'telescope'
V -> 'saw' | 'walked'
P -> 'in' | 'with'
""")

# Create a ChartParser
parser = ChartParser(grammar)

# Simple syntax checking function
def check_syntax(sentence):
    tokens = nltk.word_tokenize(sentence)
    trees = list(parser.parse(tokens))
    if trees:
        print("✔️ Sentence is syntactically correct!")
    else:
        print("❌ Sentence is NOT syntactically correct.")

# Example usage
sentence = "I saw a dog in the park"
check_syntax(sentence)
