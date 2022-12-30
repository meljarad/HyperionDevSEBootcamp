# garden.py
This script demonstrates how to use the spaCy library to perform entity recognition on a list of garden path sentences.

## Requirements and Usage
To run this code, you will need the following:

| Requirement                                  | Installation command (Mac)              | Installation command (Windows)          |
|----------------------------------------------|-----------------------------------------|-----------------------------------------|
| Python 3                                     | Already installed on your system        | Already installed on your system        |
| spaCy library                                | pip install spacy                      | python -m pip install spacy             |
| tabulate library                             | pip install tabulate                    | python -m pip install tabulate          |
| Pre-trained English language model for spaCy | python -m spacy download en_core_web_sm | python -m spacy download en_core_web_sm |

See https://spacy.io for more instructions on Spacy.

## Functionality
This script includes 5 pretyped garden path sentences:

- "Without her contributions would be impossible"
- "The complex houses married and single soldiers and their families"
- "When Mr. Everest called his old mother was happy"
- "Jordan announces crude discovery of new oil reserves"
- "After James the young Londoner had visited his parents prepared to celebrate their 30th anniversary"

Garden path sentences are sentences that are initially ambiguous or misleading, causing the reader to initially parse the sentence in a way that is not consistent with its true meaning.

The script has two main functions:

| Function           | Description                                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| tokenizer          | This function takes a list of garden sentences as input and returns a list of tokenized sentences.                                             |
| recognize_entities | This function takes a list of tokenized sentences as input and performs entity recognition on each sentence, printing the results to the user. |

## Output
The script will output a summary table for each sentence, showing the identified entities and their labels/label codes. 

If a sentence does not have any entities, it will print a message saying so.
## Authors

- [@Mo El-Jarad](https://github.com/meljarad/HyperionDevSEBootcamp)


## Acknowledgements
Many thanks to HyperionDev for providing guidance and educational resource material on Natural Language Processing and other aspects of Python coding as part of the Software Engineering Bootcamp, making it possible to produce this code.
 - [HyperionDev](https://www.hyperiondev.com/)