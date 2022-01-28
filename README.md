# Wordle Solver

Currently, the dictionary/trie is not generated correctly for some reason.
 - OSPD5 words do not appear as leaves
 - I suspect weights for branches are also incorrect, but not sure

Need to write the solver code based on the json/pickle file of the generated trie.

⚠ Runtime for charfreq.py is maybe on the order of 10 minutes.

### Update
Created charFreq2.py that calculates char frequencies from list of possible answers found in Wordle source code. Also allows user to pass words as params and get back a score of how common that word's letters are.