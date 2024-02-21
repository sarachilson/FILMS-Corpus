# -*- coding: utf-8 -*-
# Authors: Elizaveta Sineva, Sara Chilson
"""
Counting different types of frequencies.
"""

from process_sent import process_sent



def count_freq(data_lines, count_character=False, count_bigram=False,
               stats=False):
    """
    Counts the frequency of every word in the data.
    Optionally counts the frequency of every character in the data.

    Parameters
    ----------
    data_lines : list of strings
        A list of lines (sentences) from the data file.
    count_character : bool, optional
        Set to True if the information about word character frequency is to be added. 
        The default is False.
    count_bigram : bool, optional
        Set to True if the information about bigram frequency within a word
            is to be added. The default is False.
    stats : bool, optional
        Set to True to have some statistical information about the corpus 
            printed out. The default is False.

    Returns
    -------
    word_freq : dictionary
        Dictionary containing word to its frequency.
    character_freq : dictionary
        Dictionary containing word character to its frequency 
            if count_character is True.
    bigram_freq : dictionary
        Dictionary containing bigram to its frequency if count_bigram is True.

    """
    word_freq = {}
    character_freq = {}
    bigram_freq = {}
    
    # Keep track of deleted characters
    deleted = set()
    
    # Go through every sentence in the data
    for sent in data_lines:
        processed_sent, del_set = process_sent(sent, stats)
        
        deleted.update(del_set)
        
        # Go through every word in the given sentence
        for word in processed_sent:
            
            # Remove empty strings
            if not word:
                continue
            
            # Create an entry for the word in the frequency dictionary
            # if it doesn't exist yet
            word_freq.setdefault(word, 0)
            # Count the word
            word_freq[word] += 1
            
            if count_character:
                # Go through every character in the given word
                for character in word:
                    # Skip spaces and punctuation
                    if character in " -'":
                        continue
                    # Create an entry for the character in the frequency
                    # dictionary if it doesn't exist yet
                    character_freq.setdefault(character, 0)
                    # Count the character
                    character_freq[character] += 1
            
            if count_bigram:
                bi_word = f"^{word}$"
                
                for idx in range(len(bi_word)-1):
                    bigram = bi_word[idx:idx+2]
                    # Create an entry for the bigram in the frequency
                    # dictionary if it doesn't exist yet
                    bigram_freq.setdefault(bigram, 0)
                    # Count the bigram
                    bigram_freq[bigram] += 1
    
    if stats:
        print("Removed characters:\n", deleted, "\n")
    
    return word_freq, character_freq, bigram_freq

