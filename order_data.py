# -*- coding: utf-8 -*-
# Authors: Elizaveta Sineva, Sara Chilson
"""
Order the given frequencies.
"""

import pandas as pd
import math

from collect_ipa import collect_ipa



def order_data(freq_dict, unit_name="Word", ipa_dir="", lang=None,
               stats=False):
    """
    Organises data into a data frame into columns:
    Rank, Word/Character/Bigram, Frequency, Frequency per million, IPA (optional)
    Sorts the data according to frequency first, aplhabetically second.
    Ranks the data (units with the same frequency are assigned the same rank).
    Calculates frequency per million.
    Adds IPA infomation if necessary.

    Parameters
    ----------
    freq_dict : dict
        A dictionary containing word/character/bigram frequency information.
    unit_name : str, optional
        The name of the unit used for frequency counting. 
        Options: "Word", "Character", "Bigram". The default is "Word".
    ipa_dir : str, optional
        Provide path to the directory with the IPA information 
            if the information is to be added. The default is "" (= no IPA).
    lang : str, optional
        The abbreviation of the language as given in the name of 
            the data file (only necessary for IPA). The default is None.
    stats : bool, optional
        Set to True to have some statistical information about the corpus 
            printed out. The default is False.

    Returns
    -------
    freq_df : pandas DataFrame
        Dataframe containing ordered information about the data.

    """
    # The columns to be added to the data frame
    data_dict = {"Rank": [], unit_name: [], "Frequency": [], 
                 "Frequency per million": [], "Zipf value": []}
    
    if ipa_dir:
        # Add the IPA column
        data_dict["IPA"] = []
        # Extract the IPA information
        ipa_dict = collect_ipa(lang, ipa_dir)
    
    # Sort the data from highest frequency to lowest, alphabetically
    ordered_data = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    
    # Get the total number of units in the data
    total_units = sum(freq_dict.values())
        
    rank = 0
    prev_freq = 0
    
    
    if stats:
        total_types = 0
        
        # Initialize counters for word statistics
        if unit_name == "Word":
            word_len = 0
            type_len = 0
            
            if ipa_dir:
                ipa_units = 0
    
    # Collect all data into one table
    for (unit, freq) in ordered_data:
        
        # Check for IPA if applicable
        if ipa_dir:
            ipa_info = None
            
            if unit in ipa_dict:
                ipa_info = ipa_dict[unit]
            elif "ß" in unit:
                # Rewrite ß as ss to search for IPA
                # to account for German spelling versions
                ssword = unit.replace("ß", "ss")
                if ssword in ipa_dict:
                    ipa_info = ipa_dict[ssword]
            
            # If the ipa info is available, include the word
            if ipa_info:
                data_dict["IPA"].append(ipa_info)
            # If the ipa info isn't available, exclude the word
            else:
                continue
        
        # Determine the true rank
        if freq != prev_freq:
            # If the frequency of the current word is different from the
            # previous, increase its rank
            rank += 1
            prev_freq = freq
        
        # Add all of the information about the unit to the data frame
        data_dict["Rank"].append(rank)
        data_dict[unit_name].append(unit)
        data_dict["Frequency"].append(freq)
        
        # Calculate frequency per million
        freq_mil = round(10**6 * freq / total_units, 4)
        data_dict["Frequency per million"].append(freq_mil)
        
        # Calculate Zipf value
        zipf_val = round(math.log10(freq_mil)+3, 4)
        data_dict["Zipf value"].append(zipf_val)
        
        # Calculate word information for statistics
        if stats:
            total_types += 1
            if unit_name == "Word":
                curr_len = len(unit)
                word_len += curr_len*freq
                type_len += curr_len
                if ipa_dir:
                    ipa_units += freq
        
    freq_df = pd.DataFrame(data_dict)

    # Print out the statistics
    if stats:
        corpus_size = "IPA" if ipa_dir else "full"
        if ipa_dir:
            total_units = ipa_units
        if unit_name == "Word":
            word_len_av = round(word_len/total_units, 2)
            type_len_av = round(type_len/total_types, 2)
            print(f"The average word length within the {corpus_size} corpus text is {word_len_av}.")
            print(f"The average unique word length within the {corpus_size} corpus {type_len_av}.")
            print()
        print(f"The total number of {unit_name.lower()}s in the {corpus_size} corpus is {total_units}.")
        print(f"The total number of {unit_name.lower()} types in the {corpus_size} corpus is {total_types}.")
        print()
    
    return freq_df
