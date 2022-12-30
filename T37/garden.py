# T37 - GARDEN.PY
import spacy # Used to import English language NLP capabilities
from tabulate import tabulate # Allows for outputting data in a user-readable format

# Used to load a pre-trained version of the English language model in the spaCy library.
nlp = spacy.load('en_core_web_sm')

def tokenizer(input_list):
    '''
    This function will iterate through a list of garden sentences and tokenize each one.

    Args:
        input_list (list): The list of garden sentences where each element is a string that represents a sentence.
    '''
    doc_list = []
    for i in input_list:
        doc_list.append(nlp(i))
    return doc_list

def recognize_entities(input_doc_list):
    '''
    This function will iterate through a list of tokenized sentences and perform entity recognition on each token.

    Args:
        input_doc_list (list): The list of tokenized sentences upon which entity recognition is performed.
    '''
    count = 0
    entities_headers = ['PHRASE:', 'ENTITY LABEL:', 'ENTITY LABEL CODE:']
    for i in input_doc_list:
        entities_data = []
        count += 1
        # Print a summary of the output to the user
        print(f"—"*100 + f"\nSENTENCE {count}: \'{i}\'") # Border included for UI and user readability purposes
        if len(i.ents) == 0:
            print("\nThis sentence has no entities!")
        else:
            # If at least one entity is found, loop through it and display the relevant word and its entity type
            print("\nThis sentence has the following entities:")
            for entity in i.ents:
                entities_data.append(['\'' + str(entity.text) + '\'', str(entity.label_).title(), str(entity.label)])
            summary_table = tabulate(entities_data, headers=entities_headers, tablefmt="grid")
            print(summary_table)

# Declares five initial examples of garden path sentences and stores them all in a list
gp_sentence_1 = u"Without her contributions would be impossible"
gp_sentence_2 = u"The complex houses married and single soldiers and their families"
gp_sentence_3 = u"When Mr. Everest called his old mother was happy"
gp_sentence_4 = u"Jordan announces crude discovery of new oil reserves"
gp_sentence_5 = u"After James the young Londoner had visited his parents prepared to celebrate their 30th anniversary"

gp_sentences_list = [gp_sentence_1,
                     gp_sentence_2,
                     gp_sentence_3,
                     gp_sentence_4,
                     gp_sentence_5
                     ]

# Create a list of tokenized sentences
gp_sentence_doc_list = tokenizer(gp_sentences_list)

# Print output
recognize_entities(gp_sentence_doc_list)

'''
ENTITY COMMENTS:
1. The word 'Jordan' is incorrectly identified as a Person when the sentences refers to a discovery of crude oil by
the country of Jordan. This should be of entity type GPE (Geopolitical entity) but due to the similarity in the
name of the country and the common first name, this sentence can be challenging for Spacy to parse. Similarly this 
particular garden sentence starts off as if to imply someone named Jordan was to make a crude announcement, hence
it can be initially misleading in true garden-path sentence style.
2. The word 'Londoner' in sentence 5 is identified as a Person however this is James' demonym that is
referring to the fact he is from London, rather than a separate person who is also a Londoner.
'''
