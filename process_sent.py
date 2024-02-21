# -*- coding: utf-8 -*-
# Authors: Elizaveta Sineva, Sara Chilson
"""
Sentence processing.
"""

import unicodedata



def process_sent(sent, stats=False):
    """
    Removes non-alphabetic characters from the sentence.
    Keeps combining characters (marks) that aren't musical or signwriting.
    Keeps mid-word hyphens and apostrophes, as well as
    apostrophes that do not seem to be used as quotation marks.
    Lower-cases the sentence.
    Extracts words from the sentence.

    Parameters
    ----------
    sent : string
        A sentence from the raw data.
    stats : bool, optional
        Set to True to have some statistical information about the corpus 
            printed out. The default is False.

    Returns
    -------
    words: list of strings
        A list of words from the sentence.

    """    
    sent_len = len(sent)
    clean_sent = ""
    
    # Manage apostrophes as quot. marks
    apostrophe_start = False
    apostrophe_indices = []
    
    # Keep track of deleted characters
    deleted = set()
    
    for char_idx in range(sent_len):
        char = sent[char_idx]
        
        # Remove unnecessary characters
        if not char.isalpha() and char not in "-' ":
            
            # Check for combining non-alphabetic characters
            uni_cat = unicodedata.category(char)
            uni_hex = hex(ord(char))
            
            # Remove if the character isn't combining
            if uni_cat != "Mn" and uni_cat != "Mc":
                
                # Keep track of removed characters for statistics
                if stats:
                    deleted.add(char)
                continue
            
            # Remove if the combining character is...
            elif (uni_hex.startswith("0x1d1") or  # musical
                  uni_hex.startswith("0x1d2") or  # Greek musical
                  uni_hex.startswith("0x1da")     # sign writing
                  ):
                    # Keep track of removed characters for statistics
                    if stats:
                        deleted.add(char)
                    continue

            # Keep the rest of combining characters
            else:
                clean_sent += char
        
        # Remove multiple spaces
        elif (char == ' ' and ((clean_sent and clean_sent[-1] == ' ') or 
                               not clean_sent)):
            continue
        
        # Keep the hyphens between words, else remove
        elif (char == '-' and (
            not clean_sent or   # It's the start of the sentence
            not clean_sent[-1].isalpha() or   # The previous character isn't a letter
            char_idx+1 >= sent_len or   # It's the end of the sentence
            not sent[char_idx+1].isalpha())):   # The next character isn't a letter
            continue
        
        # Manage apostrophes as quot. marks
        elif char == "'":
            # If the start of the supposed quotation mark isn't found yet
            if (not apostrophe_start and 
                # It's the start of the sent or not mid-word
               (not clean_sent or clean_sent[-1] == ' ')):
                # Assume the start of quotation
                  apostrophe_start = True
                  
                  # Keep the apostrophe if it's attached to a word
                  # Track its index t remove later if it is part
                  # of a quotation
                  if (char_idx+1 < sent_len and sent[char_idx+1].isalpha()):                      
                      apostrophe_indices.append(len(clean_sent))
                      # Keep the apostrophe in the sentence for now
                      clean_sent += char
            
            # If the start of the supposed quotation mark has been found
            elif (apostrophe_start and 
                # It's the end of the sent or not mid-word
               (char_idx+1 >= sent_len or not sent[char_idx+1].isalpha())):
                apostrophe_start = False
            
            # If it is mid-word or seems to be part of the word
            else:
                clean_sent += char
        
        # Keep everything else in the sentence
        else:
            clean_sent += char
            
    # If the end of supposed quotation was never found,
    # don't remove the apostrophe
    if apostrophe_start and apostrophe_indices:
        apostrophe_indices.pop(-1)
    
    # Remove the apostrophes that start the quotations
    # Move backwards to avoid shifting indices after apostrophe removal
    for idx in apostrophe_indices[::-1]:
        clean_sent = clean_sent[:idx] + clean_sent[idx+1:]
    
    # Lowercase the sentence
    clean_sent = clean_sent.lower().strip()
    
    # Split the sentence into words
    words = clean_sent.split(" ")

    return words, deleted

