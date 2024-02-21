# -*- coding: utf-8 -*-
# Authors: Elizaveta Sineva, Sara Chilson
"""
The main file for running the code for gathering
the frequency information from the data.

The data used for collecting the frequencies is taken 
from the OpenSubtitles database:
https://opus.nlpl.eu/OpenSubtitles-v2018.php

P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: 
Extracting Large Parallel Corpora from Movie and TV Subtitles. 
In Proceedings of the 10th International Conference on Language 
Resources and Evaluation (LREC 2016)
"""

import argparse
import time

from extract_data import extract_data
from count_freq import count_freq
from order_data import order_data
from export_data import export_data


ABBR2FULL = {'af': 'afrikaans', 
             'sq': 'albanian', 
             'ar': 'arabic', 
             'hy': 'armenian', 
             'bn': 'bengali',
             'bg': 'bulgarian', 
             'eu': 'basque', 
             'br': 'breton', 
             'ca': 'catalan', 
             'hr': 'croatian', 
             'cs': 'czech', 
             'da': 'danish', 
             'nl': 'dutch', 
             'en': 'english', 
             'eo': 'esperanto', 
             'et': 'estonian', 
             'fi': 'finnish', 
             'fr': 'french', 
             'gl': 'galician', 
             'ka': 'georgian', 
             'de': 'german', 
             'el': 'greek', 
             'he': 'hebrew', 
             'hi': 'hindi', 
             'hu': 'hungarian', 
             'is': 'icelandic', 
             'id': 'indonesian', 
             'it': 'italian', 
             'kk': 'kazakh', 
             'lv': 'latvian', 
             'lt': 'lithuanian', 
             'mk': 'macedonian', 
             'ms': 'malay', 
             'ml': 'malayalam', 
             'no': 'norwegian', 
             'fa': 'persian', 
             'pl': 'polish', 
             'pt_br': 'portuguese_brazil', 
             'pt': 'portuguese_portugal', 
             'ro': 'romanian', 
             'ru': 'russian', 
             'sr': 'serbian', 
             'sk': 'slovak', 
             'sl': 'slovenian', 
             'es': 'spanish', 
             'sv': 'swedish', 
             'tl': 'tagalog', 
             'ta': 'tamil', 
             'te': 'telugu', 
             'tr': 'turkish', 
             'uk': 'ukrainian', 
             'ur': 'urdu'}                                                                                           



def main(gz_data_file, file_types="txt|xlsx", ipa_dir="",
         count_character=False, count_bigram=False, stats=False):
    """
    Collects frequencies from the OpenSubtitles data in a given language.

    Parameters
    ----------
    gz_data_file : str
        The path to the data file with the gz extension.
    file_types : str, optional
        The extension of the file to export the data into.
        The available extensions: "txt","csv", "xlsx".
        To export data into more than one file type, use | to separate
           extensions.
         The default is "txt|xlsx".
    ipa_dir : str, optional
        Provide path to the directory with the IPA information 
            if the information is to be added. The default is "" (= no IPA).
    count_character : bool, optional
        Set to True if the information about word character frequency is to 
        be added. The default is False.
    count_bigram : bool, optional
        Set to True if the information about bigram frequency within a word
            is to be added. The default is False.
    stats : bool, optional
        Set to True to have some statistical information about the corpus 
            printed out. The default is False.

    Returns
    -------
    None.

    """
    # Extract the language of the data
    split_path = gz_data_file.split("/")
    lang_abbr = split_path[-1].split(".")[0]
    lang = ABBR2FULL[lang_abbr]
    
    print(f"Language: {lang.capitalize()}\n")
    
    # Extract the raw data from the file
    data_lines = extract_data(gz_data_file)

    # Extract the frequencies for each word in the data
    word_freq, character_freq, bigram_freq = count_freq(data_lines, 
                                                count_character=count_character,
                                                count_bigram=count_bigram,
                                                stats=stats)
    
    data_types = {"word": word_freq}
    
    if count_character:
        data_types["character"] = character_freq
        
    if count_bigram:
        data_types["bigram"] = bigram_freq
    
    if ipa_dir:
        data_types["ipa"] = word_freq
    
    for data_type in data_types:
        ipa_info = ipa_dir if data_type == "ipa" else ""
        data_type = "word" if data_type == "ipa" else data_type
        
        # Organize the data
        ordered_freq = order_data(data_types[data_type], ipa_dir=ipa_info, 
                                  lang=lang, unit_name=data_type.capitalize(),
                                  stats=stats)
                
        # Export word frequency data in a file
        folder_name = f"data/{data_type}_freq/"
        file_name = folder_name + lang + f".{data_type}.freq"
        if ipa_info:
            file_name += ".ipa"        
        export_data(ordered_freq, file_name, file_types=file_types)
        
        

if __name__ == "__main__":
    ### Run the code using arguments
    argdesc = "The script for extracting word frequencies from the OpenSubtitles corpus."
    argparser = argparse.ArgumentParser(description=argdesc)

    argparser.add_argument("-f", "--file", type=str, required=True,
                            help="the path to the data file with the gz extension (required)")
    argparser.add_argument("-x", "--extension", type=str, default="txt|xlsx",
                            help="the extension of the file to export the data into (txt/xlsx/csv); use | for several data types; default: txt|xlsx")    
    argparser.add_argument("-i", "--ipa", type=str, default="",
                            help="the path to the directory containing the files with the IPA information if the information is to be added")
    argparser.add_argument("-c", "--character", default=False,
                            action=argparse.BooleanOptionalAction,
                            help="use to extract word character frequency information")
    argparser.add_argument("-b", "--bigram", default=False,
                            action=argparse.BooleanOptionalAction,
                            help="use to extract bigram frequency information (bigrams within a word)")
    argparser.add_argument("-s", "--stats", default=False,
                            action=argparse.BooleanOptionalAction,
                            help="use to print out statistics about the data")
    
    args = argparser.parse_args()

    
    ### Run the script with the given arguments
    time_start = time.time()  # keep track of the time to report on the runtime
    
    gz_data_file = args.file
    main(gz_data_file, ipa_dir=args.ipa, count_character=args.character,
          count_bigram=args.bigram, stats=args.stats)


    ### Run the script without using arguments
    # gz_data_file = "opensubs/br.txt.gz"
    # main(gz_data_file, count_character=False, count_bigram=False, 
    #      ipa_dir="IPA/", stats=True)
    
    ### Calculate the runtime
    time_end = time.time()
    
    total_time = time_end - time_start
    
    time_hrs = int(total_time/60//60)
    time_min = int(total_time//60 - time_hrs*60)
    time_sec = "{:02d}".format(int(total_time - time_min*60 - time_hrs*60*60))
    
    time_min = "{:02d}".format(time_min)
    
    print(f"The total runtime is {time_hrs}:{time_min}:{time_sec}.")
    
    