# -*- coding: utf-8 -*-
# Authors: Elizaveta Sineva, Sara Chilson
"""
Extract data from gz.
"""

import gzip


def extract_data(gz_file):
    """
    Extract data from a given gz file.

    Parameters
    ----------
    gz_file : string
        The path to the data file of gz type.

    Returns
    -------
    lines: list of strings
        A list of lines from the data.
    """
    lines = []
    
    with gzip.open(gz_file) as f:
        for line in f:
            decoded_line = line.decode()
            lines.append(decoded_line)
    
    return lines

