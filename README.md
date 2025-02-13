# Word <ins>F</ins>requency <ins>I</ins>PA <ins>M</ins>ulti<ins>L</ins>ingual <ins>S</ins>ubtitles Corpus (FILMS Corpus)

Word <ins>F</ins>requency <ins>I</ins>PA <ins>M</ins>ulti<ins>L</ins>ingual <ins>S</ins>ubtitles Corpus (FILMS Corpus) is a frequency corpus based on the movie subtitles data taken from [OpenSubtitles corpus](https://opus.nlpl.eu/OpenSubtitles/corpus/version/OpenSubtitles) (v2018).
FILMS includes a full length version of all frequency count, as well as a smaller subset of the data contianing only words for which IPA transcriptions were avaliabe in Wikipedia [Wikipron corpus](https://github.com/CUNY-CL/wikipron/tree/master/data/scrape/tsv).

Sara Chilson, Elizaveta Sineva, Xenia Schmalz (2024). 

## Data

The corpus contain frequency data for 52 languages in `txt` and Excel (`xlsx`) formats. Note that for languages that have more than 100k unique words, the Excel version is reduced to the top 100k. You can see the full version in the corresponding `txt` file. All `txt` files are tab separated.  

The data is organised into three main directories in the following way:

* [`data/word_freq`](https://github.com/sarachilson/FILMS-Corpus/tree/main/data/word_freq): contians four files for each language in the corpus. 

1) txt file of the full-length unfiltered version (named `[language name].word.freq.txt`)
2) txt file of the IPA filtered data (named `[language name].word.freq.ipa.txt`)
3) excel file of the full-length unfiltered version (named `[language name].word.freq.xlsx`)
4) excel file of the IPA filtered data  (named `[language name].word.freq.ipa.xlsx`)

* [`data/character_freq`](https://github.com/sarachilson/FILMS-Corpus/tree/main/data/character_freq): the word character frequencies for all languages (named `[language name].character.freq`) both as a `txt` file and as a `xlsx` file
* [`data/bigram_freq`](https://github.com/sarachilson/FILMS-Corpus/tree/main/data/bigram_freq): the bigram frequencies for all languages (named `[language name].bigram.freq`). Note that the bigrams were extracted from within the word and not from within the sentence.

The files contain the frequency rank, the raw frequency, the frequency per million and the Zipf value of each word, as well as their IPA transcription in the IPA files. 
Note that different IPA transcriptions for the same word are separated by double-space | double-space rather than a single space for the sake of improving readability.

You can also find statistics information about each language in the directory [`stats`](https://github.com/sarachilson/FILMS-Corpus/tree/main/stats).

The statistics information includes:
- the average word length within the text of the corpus
- the average word length of unique words in the corpus
- the total number of words (word characters, bigrams) in the text
- the total number of unique words (word characters, bigrams)
- A set of characters that were removed after the dataset pre-processing.


## Code

Run [`main.py`](https://github.com/sarachilson/FILMS-Corpus/blob/main/main.py) to produce frequency files.
`main.py` takes the following arguments that allow you to modify the frequency data output:

| Argument | Full argument name | Description |
| --- | --- | --- |
| `-h` | `--help` | List available arguments. |
| `-f FILE` | `--file FILE` | The path to the data file with the `gz` extension (required). |
| `-x EXTENSION` | `--extension EXTENSION` | The extension of the file to export the data into (`txt`/`xlsx`/`csv`). Use \| for several data types (default: `txt|xlsx`) |
| `-i IPA` | `--ipa IPA` | The path to the directory containing the files with the IPA information from the Wikipron corpus. The IPA information will only be added to the data if the directory is provided. |
| `-c` | `--character` | Use to extract word character frequency information. |
| `-b` | `--bigram` | Use to extract bigram frequency information. |
| `-a` | `--aspell` | Use to filter the words via the [Aspell](http://aspell.net/) spell checker. |
| `-s` | `--stats` | Use to print out statistics about the data. |

_Usage_ _example_: 
If you would like to get the frequency data for German with IPA only in Excel format, and have the statistics information printed out, you can run the following in the command line:

```
python main.py -f OpenSubtitlesDirectoryName/de.txt.gz -x xlsx --ipa WikipronDirectoryName/ --stats
```