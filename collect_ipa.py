# -*- coding: utf-8 -*-
# Authors: Elizaveta Sineva, Sara Chilson
"""
Collect IPA information.

The files with the IPA information are taken from the WikiPron database:
https://github.com/CUNY-CL/wikipron/tree/master/data/scrape/tsv

Jackson L. Lee, Lucas F.E. Ashby, M. Elizabeth Garza, Yeonju Lee-Sikka, 
Sean Miller, Alan Wong, Arya D. McCarthy, and Kyle Gorman (2020). 
Massively multilingual pronunciation mining with WikiPron. 
In Proceedings of the 12th Language Resources and Evaluation 
Conference, pages 4223-4228.
"""

import pandas as pd


LANG2FILE = {'afrikaans': 'afr_latn_broad.tsv', 
             'albanian': 'sqi_latn_broad.tsv', 
             'arabic': 'ara_arab_broad.tsv', 
             'armenian': 'hye_armn_w_narrow.tsv', 
             'bengali': 'ben_beng_broad.tsv', 
             'basque': 'eus_latn_broad.tsv', 
             'breton': 'bre_latn_broad.tsv', 
             'bulgarian': 'bul_cyrl_broad.tsv', 
             'catalan': 'cat_latn_broad.tsv', 
             'croatian': 'hbs_latn_broad.tsv', 
             'czech': 'ces_latn_broad.tsv', 
             'danish': 'dan_latn_broad.tsv', 
             'dutch': 'nld_latn_broad.tsv', 
             'english': 'eng_latn_us_broad.tsv', 
             'esperanto': 'epo_latn_broad.tsv', 
             'estonian': 'est_latn_broad.tsv', 
             'finnish': 'fin_latn_broad.tsv', 
             'french': 'fra_latn_broad.tsv', 
             'galician': 'glg_latn_broad.tsv', 
             'georgian': 'kat_geor_broad.tsv', 
             'german': 'deu_latn_broad.tsv', 
             'greek': 'ell_grek_broad.tsv', 
             'hebrew': 'heb_hebr_broad.tsv', 
             'hindi': 'hin_deva_broad.tsv', 
             'hungarian': 'hun_latn_narrow.tsv', 
             'icelandic': 'isl_latn_broad.tsv', 
             'indonesian': 'ind_latn_broad.tsv', 
             'italian': 'ita_latn_broad.tsv', 
             'kazakh': 'kaz_cyrl_broad.tsv', 
             'latvian': 'lav_latn_narrow.tsv', 
             'lithuanian': 'lit_latn_broad.tsv', 
             'macedonian': 'mkd_cyrl_narrow.tsv', 
             'malay': 'msa_latn_broad.tsv', 
             'malayalam': 'mal_mlym_broad.tsv', 
             'norwegian': 'nob_latn_broad.tsv', 
             'persian': 'fas_arab_broad.tsv', 
             'polish': 'pol_latn_broad.tsv', 
             'portuguese_brazil': 'por_latn_bz_broad.tsv', 
             'portuguese_portugal': 'por_latn_po_broad.tsv', 
             'romanian': 'ron_latn_broad.tsv', 
             'russian': 'rus_cyrl_narrow.tsv', 
             'serbian': 'hbs_cyrl_broad.tsv|hbs_latn_broad.tsv', 
             'slovak': 'slk_latn_broad.tsv', 
             'slovenian': 'slv_latn_broad.tsv', 
             'spanish': 'spa_latn_ca_broad.tsv', 
             'swedish': 'swe_latn_broad.tsv', 
             'tagalog': 'tgl_latn_broad.tsv', 
             'tamil': 'tam_taml_broad.tsv', 
             'telugu': 'tel_telu_broad.tsv', 
             'turkish': 'tur_latn_broad.tsv', 
             'ukrainian': 'ukr_cyrl_narrow.tsv', 
             'urdu': 'urd_arab_broad.tsv'}



def collect_ipa(lang, data_dir):
    """
    Collect the IPA information for a given language.

    Parameters
    ----------
    lang : str
        The name of the language to extract the IPA information for.
        For an appropriate language name and available languages
            check the LANG2FILE dictionary above.
    data_dir : str
        The path to the directory that contains Wikipron IPA files.

    Raises
    ------
    Exception
        If the requested language does not have a corresponding IPA file.

    Returns
    -------
    ipa_dict : dict
        A dictionary that provides an IPA transkription for available words.

    """
    # Make sure the data folder name is in an appropriate format
    if data_dir[-1] != "/":
        data_dir = data_dir + "/"
    
    # Raise exception if the IPA file for the requested language
    # does not exist
    if lang not in LANG2FILE:
        excep_msg = f"The IPA information is not supported for language {lang}."
        raise Exception(excep_msg)
    
    ipa_dict = {}
    
    # Go through every IPA file that exists for the given language
    for lang_file in LANG2FILE[lang].split("|"):
        # Extract the IPA data
        data = pd.read_csv(data_dir+lang_file, sep='\t',
                            names=["Word", "IPA"], header=None)

        for index, row in data.iterrows():
            word, ipa = row["Word"], row["IPA"]
            
            # Add the new word to the dictionary
            if word not in ipa_dict:
                ipa_dict[word] = ipa
            
            # Add the new IPA to the word if it is already in the dictionary
            else:
                ipa_dict[word] = ipa_dict[word] + "  |  " + ipa
    
    return ipa_dict

