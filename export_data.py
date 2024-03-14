# -*- coding: utf-8 -*-
# Authors: Elizaveta Sineva, Sara Chilson
"""
Export data into a certain format.
"""

import os


def export_data(df, file_name, file_types="txt"):
    """
    Exports the data into a file with a given format(s).

    Parameters
    ----------
    df : pandas DataFrame
        A dataframe containing the necessary data to export.
    file_name : str
        The name of the file / path to the file to which the data
            will be exported.
    file_types : str, optional
        The extension of the file to export the data into.
        The available extensions: "txt","csv", "xlsx". 
        The default is "txt".
        To export data into more than one file type, use | to separate
           extensions.
        Example: "txt|xlsx".

    Raises
    ------
    Exception
        If the requested file type is not supported by the function.

    Returns
    -------
    None.

    """
    # Create the folder for the data if it does not exist yet
    directory = "/".join(file_name.split("/")[:-1])
    if not os.path.exists(directory):
        os.mkdir(directory)
    
    # Create the file(s) with the required extension
    for file_type in file_types.split("|"):
        curr_file_name = f"{file_name}.{file_type}"
        
        if file_type == "txt":
            df.to_csv(curr_file_name, sep='\t', index=False,
                      encoding="utf-8")
        
        elif file_type == "csv":
            df.to_csv(curr_file_name, sep=',', index=False,
                      encoding="utf-8")
        
        elif file_type == "xlsx":
            # Maximum size possible for excel: 1048576, 16384
            # Restrict data size to 100,000 entries
            max_entries = 100000
            df[:max_entries].to_excel(curr_file_name, index=False)
        
        else:
            raise Exception(f"Unsupported file type {file_type}.")
    
