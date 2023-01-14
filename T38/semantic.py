import spacy # Used for NLP capabilities
from tabulate import tabulate # For printing results in user readable format

# Loads the medium-sized English language model used for NLP capabilities
nlp = spacy.load('en_core_web_md')

# Code Example 1 - From Lecture
'''
This snippet of code may include original or modified versions of code taken from the lecture material for Task 38 of 
the HyperionDev Software Engineering course, as the task requires running this code. 

This code explores the capability of semantic similarity between three words: 'cat', 'monkey', and 'banana'.

Interesting points to note:
- 'cat' and 'monkey' bear immediate similarity in multiple ways. Firstly, they are both members of the animal kingdom and
even more specifically they are both mammals. Cats and monkeys are both living beings that are capable of displaying the
same range of emotions, behaviours and responses to external stimuli. They have also both been used as symbols in sports,
deified in various religions, revered as national animals and have featured in artwork.
- 'banana' and 'monkey' bear greater similarity because monkeys typically eat bananas in the wild and both monkeys and 
bananas are capable of 'living' as organisms composed of cells. Hence whilst they are not immediately physically similar, 
the association between the two that would increase their similarity score compared to say 'cat' and 'banana'. The common
 image of monkeys eating bananas is frequently noted in popular culture, further strengthening their association.
- 'banana' and 'cat' bear the lowest similarity score due to the lack of identifiable links or themes that associate
the two themes compared to the other two words. However, there is an argument to say that there is some similarity between
 the two in that both cats and bananas are 'living' or capable of living, both are also consumed as prey, and biologically
 they are both organic and composed of cells. Additionally, both cats and bananas will have been depicted in artwork or
 examples of popular culture, hence they do bear some subtle similarity but not in the most obvious way.
'''
print("—"*80) # Prints border for UI and user readability purposes
print("CODE EXAMPLE 1 - SEMANTIC SIMILARITY BETWEEN \'CAT\', \'MONKEY\' AND \'BANANA\':\n")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Declares data and header lists for the Tabulate table, note use of .similarity() function to calculate similarity score
headers = ["Word:", "Word:", "Similarity:"]
data = [[word1, word2, word1.similarity(word2)],
        [word3, word2, word3.similarity(word2)],
        [word3, word1, word3.similarity(word1)]
        ]

# Prints results in user readable table
print(tabulate(data, headers=headers, tablefmt="simple_outline"))

# Code Example 2 - My Example
'''
This snippet of code may include original or modified versions of code taken from the lecture material for Task 38 of 
the HyperionDev Software Engineering course, as the task requires running this code. 

This code explores the capability of semantic similarity between three words: 'blue', 'sky', and 'plane'.

- The association between "blue" and "sky" is strongest as the colour blue is often used to commonly describe the colour 
of the sky during a clear day. The two words often feature together in association, even in idioms (e.g. "blue sky 
thinking"). However as 'blue' is distinctly a colour and 'sky' is a feature of the natural world, the two are not 
necessarily immediately conceptually or semantically similar.
- The association between 'plane' and 'sky' is somewhat strong as planes of course fly through the sky, hence the
 association between these two is that planes are commonly found or seen flying in the sky.
- The link between "plane" and "blue" is not very strong. Both can be seen in the sky, but they do not have a direct 
connection. The sky is often blue, but this is because of the way that light from the sun is scattered in the air. As 
planes can be any color, not just blue, so the two are not closely linked.
'''
print("—"*80) # Prints border for UI and user readability purposes
print("CODE EXAMPLE 2 - WORD SIMILARITIES BETWEEN \'BLUE\', \'SKY\' AND \'PLANE\':\n")
word1 = nlp("blue")
word2 = nlp("sky")
word3 = nlp("plane")

# Declares data and header lists for the Tabulate table, note use of .similarity() function to calculate similarity score
headers = ["Word:", "Word:", "Similarity:"]
data = [[word1, word2, word1.similarity(word2)],
        [word3, word2, word3.similarity(word2)],
        [word3, word1, word3.similarity(word1)]
        ]

# Prints results in user readable table
print(tabulate(data, headers=headers, tablefmt="simple_outline"))


# Code Example 3 - From Lecture
'''
This snippet of code may include original or modified versions of code taken from the lecture material for Task 38 of 
the HyperionDev Software Engineering course, as the task requires running this code. 

This code explores the capability of semantic similarity between multiple words [tokens] by employing the use of for loops.
'''
print("—"*80) # Prints border for UI and user readability purposes
print("CODE EXAMPLE 3 - WORD SIMILARITY FOR MULTIPLE WORDS:\n")
tokens = nlp('cat monkey apple banana')

# Declares data and header lists for the Tabulate table
headers = ["Word:", "Word:", "Similarity:"]
data = []

# Loops through the tokens and calculates their similarity score
for token1 in tokens:
    for token2 in tokens:
        # Updates the data list, note use of .similarity() function to calculate similarity score
        data.append([token1.text, token2.text, token1.similarity(token2)])

# Prints results in user readable table
print(tabulate(data, headers=headers, tablefmt="simple_outline"))

# Code Example 4 - From Lecture
'''
This snippet of code may include original or modified versions of code taken from the lecture material for Task 38 of 
the HyperionDev Software Engineering course, as the task requires running this code. 

This code explores the capability of semantic similarity between multiple sentences by employing the use of foor loops.
'''
print("\n" + "—"*80) # Prints border for UI and user readability purposes
print("CODE EXAMPLE 4 - SENTENCE SIMILARITY:\n")
sentence_to_compare = "Why is my cat on the car"

# Declare a list of sentences
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

# Create comparison sentence token
model_sentence = nlp(sentence_to_compare)

# Declares data and header lists for the Tabulate table
headers = ["Sentence:", "Model Sentence:", "Similarity:"]
data = []

# Loops through the tokens and calculates their similarity score
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    # Updates the data list, note use of .similarity() function to calculate similarity score
    data.append([sentence, model_sentence, similarity])

# Prints results in user readable table
print(tabulate(data, headers=headers, tablefmt="simple_outline"))


# Note on difference between 'en_core_web_sm' vs. 'en_core_web_md':
'''
FINAL NOTES:

The difference between 'en_core_web_md' and 'en_core_web_sm' when run on the file 'example.py' is noticeable. The primary
difference between the two is that 'en_core_web_sm' returns significantly lower similarity scores with a varying margin. 

This is likely due to the size and complexity of the two models, as 'en_core_web_md' is the medium-sized version of the 
English language model whereas 'en_core_web_sm' is the small-sized version. 

'en_core_web_md' includes all the capabilities of the 'en_core_web_sm' and additional features which enhance its word 
vector and similarity analysis capabilities, as this model is trained on a much larger dataset. Therefore, 'en_core_web_md'
has been trained on more information and resources than 'en_core_web_sm'.
'''
