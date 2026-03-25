# FILMS v1 Dataset (ARCHIVE ONLY)

This repository contains scripts used for FILMS v1. It is kept here for reference only and is not the maintained codebase.

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

### FILMS v1 Quick Links

[![FILMS v1 CODE](https://img.shields.io/badge/FILMS%20v1-CODE-orange?style=for-the-badge)](https://github.com/sarachilson/FILMS-Corpus/tree/main-os2018/)
[![FILMS v1 DATA](https://img.shields.io/badge/FILMS%20v1-DATA-blue?style=for-the-badge)](https://osf.io/2xps5/)

Use the code from the `main-os2018` branch and the FILMS v1 dataset on OSF. The general OSF link above stays relevant because it hosts all versions.

### Data (FILMS v1)

The dataset contains frequency data for 52 languages in `txt` and Excel (`xlsx`) formats. For languages with more than 100k unique words, the Excel version is reduced to the top 100k entries. The full version is available in the corresponding `txt` file. All `txt` files are tab-separated.

The data is organized into three main directories:

- [`data/word_freq`](https://github.com/sarachilson/FILMS-Corpus/tree/main-os2018/data/word_freq): contains four files for each language in the corpus.

	- `txt` file of the full-length unfiltered version (`[language name].word.freq.txt`)
	- `txt` file of the IPA-filtered version (`[language name].word.freq.ipa.txt`)
	- Excel file of the full-length unfiltered version (`[language name].word.freq.xlsx`)
	- Excel file of the IPA-filtered version (`[language name].word.freq.ipa.xlsx`)

- [`data/character_freq`](https://github.com/sarachilson/FILMS-Corpus/tree/main-os2018/data/character_freq): word character frequencies for all languages (`[language name].character.freq`) as both `txt` and `xlsx` files.
- [`data/bigram_freq`](https://github.com/sarachilson/FILMS-Corpus/tree/main-os2018/data/bigram_freq): bigram frequencies for all languages (`[language name].bigram.freq`). Note that bigrams were extracted within words, not across sentence boundaries.

The files contain frequency rank, raw frequency, frequency per million, and Zipf value for each word, plus IPA transcription in the IPA files.
Different IPA transcriptions for the same word are separated by `  |  ` (double-space, pipe, double-space) for readability.

You can also find statistics for each language in [`stats`](https://github.com/sarachilson/FILMS-Corpus/tree/main-os2018/stats).

Statistics include:
- the average word length within the text of the corpus
- the average word length of unique words in the corpus
- the total number of words (word characters, bigrams) in the text
- the total number of unique words (word characters, bigrams)
- a set of characters removed during dataset pre-processing


## Code (FILMS v1)

Run [`main.py`](https://github.com/sarachilson/FILMS-Corpus/blob/main-os2018/main.py) from the `main-os2018` branch to produce frequency files.

`main.py` accepts the following arguments:

| Argument | Full argument name | Description |
| --- | --- | --- |
| `-h` | `--help` | Show available arguments. |
| `-f FILE` | `--file FILE` | The path to the data file with the `gz` extension (required). |
| `-x EXTENSION` | `--extension EXTENSION` | The extension(s) to export (`txt`/`xlsx`/`csv`). Use `\|` for multiple types (default: `txt\|xlsx`). |
| `-i IPA` | `--ipa IPA` | The path to the directory containing the files with the IPA information from the Wikipron corpus. The IPA information will only be added to the data if the directory is provided. |
| `-c` | `--character` | Use to extract word character frequency information. |
| `-b` | `--bigram` | Use to extract bigram frequency information. |
| `-a` | `--aspell` | Use to filter the words via the [Aspell](http://aspell.net/) spell checker. |
| `-s` | `--stats` | Use to print out statistics about the data. |

_Usage example_:  
To generate German frequency data with IPA in Excel format and print statistics:

```
python main.py -f OpenSubtitlesDirectoryName/de.txt.gz -x xlsx --ipa WikipronDirectoryName/ --stats
```