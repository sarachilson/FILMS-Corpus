# FILMS Dataset (ARCHIVE ONLY)

This repository contains intermediate scripts and exploratory work that were not used for final FILMS data production. It is kept here for reference only and is not the maintained codebase.

## CURRENT REPOSITORY

[![CURRENT REPO: FILMSer](https://img.shields.io/badge/CURRENT%20REPO-FILMSer-red?style=for-the-badge)](https://github.com/elisavetas/FILMSer/)

For the maintained scripts used for FILMS v2 (OpenSubtitles v2024), use [FILMSer](https://github.com/elisavetas/FILMSer/).

## CURRENT DATA

[![DATA FILES: OSF](https://img.shields.io/badge/DATA%20FILES-OSF-blue?style=for-the-badge)](https://osf.io/rd7p6/)

All released dataset files, including different FILMS versions, are available on [OSF](https://osf.io/rd7p6/).

Sara Chilson, Elizaveta Sineva, Xenia Schmalz (2024). 

## What is FILMS?

FILMS stands for Word <ins>F</ins>requency <ins>I</ins>PA <ins>M</ins>ulti<ins>L</ins>ingual <ins>S</ins>ubtitles. It is a frequency dataset derived from movie subtitle data from the [OpenSubtitles corpus](https://opus.nlpl.eu/OpenSubtitles/corpus/version/OpenSubtitles).

## Version Notes

### FILMS v2

- Data source: OpenSubtitles v2024
- Maintained scripts: [FILMSer](https://github.com/elisavetas/FILMSer/)
- Dataset files: [OSF](https://osf.io/rd7p6/)

### FILMS v1

- Data source: [OpenSubtitles v2018](https://opus.nlpl.eu/OpenSubtitles/corpus/version/OpenSubtitles)
- IPA source: [Wikipron corpus](https://github.com/CUNY-CL/wikipron/tree/master/data/scrape/tsv)
- Scripts: [main-os2018 branch](https://github.com/sarachilson/FILMS-Corpus/tree/main-os2018/)
- Dataset files: [OSF](https://osf.io/2xps5/)
- Preprint: https://doi.org/10.31219/osf.io/zy5qf

## Using This Repository

If you still need to run these legacy scripts, use `main.py` as a package. From outside the `src` directory:

```bash
python -m src.filmser.main -f /path/to/file/
```

The script accepts the following arguments:

| Argument | Full argument name | Description |
| --- | --- | --- |
| `-h` | `--help` | Show the available arguments. |
| `-f FILE` | `--file FILE` | Path to the raw data file when creating a new frequency list, or to an existing frequency list when updating one. Required. |
| `-u` | `--update` | Update the provided frequency list with new information. |
| `-n NEW_DATA` | `--new-data NEW_DATA` | Path to a raw data file whose frequency information should be added to an existing frequency list. Only works in update mode. Default: `""`. |
| `-l LANGUAGE` | `--language LANGUAGE` | Language of the data, either as a full name (for example, `English`) or an abbreviation (for example, `en`). This is especially important when using Aspell. Default: `english`. |
| `-x EXTENSION [EXTENSION ...]` | `--extension EXTENSION [EXTENSION ...]` | Output format: `txt` (tab-separated), `xlsx`, `csv`, or `tsv`. You can provide multiple formats. Default: `txt xlsx`. |
|  | `--spacy-size SPACY_SIZE` | Size of the spaCy model used for tokenization, if applicable. Options: `sm`, `md`, `lg`, `trf`. Default: `sm`. |
| `-a` | `--aspell` | Filter words using the [Aspell](http://aspell.net/) spell checker. |
| `-i IPA [IPA ...]` | `--ipa IPA [IPA ...]` | Path to one or more files containing IPA information to add to the dataset. |
| `-c` | `--character` | Extract word character frequency information. |
| `-b` | `--bigram` | Extract bigram frequency information. |
| `-s` | `--stats` | Print summary statistics for the data. |
| `-p` | `--progress-bar` | Display a progress bar using [alive-progress](https://github.com/rsalmei/alive-progress/). |
| `-d OUTPUT_DIRECTORY` | `--output-directory OUTPUT_DIRECTORY` | Directory where the created or updated frequency list should be saved. Default: `data/`. |

## Example

To generate German frequency data with IPA, export it only as Excel, print summary statistics, and show a progress bar:

```bash
python -m src.filmser.main -f PathToFile -x xlsx --ipa PathToIPAFile --stats -p
```
