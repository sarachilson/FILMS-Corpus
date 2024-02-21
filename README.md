# LMU Subtitles Word Frequency Corpus (LSWFC)

LSWFC is a frequency corpus based on the movie subtitles data.
The basis for LSWFC is [OpenSubtitles corpus](https://opus.nlpl.eu/OpenSubtitles-v2018.php).
LSWFC also provides a shortened version of the data containing the IPA information from the [Wikipron corpus](https://github.com/CUNY-CL/wikipron/tree/master/data/scrape/tsv).

If you use the LSWFC corpus in your research, please cite the following article:
Sara Chilson, Xenia Schmalz, Elizaveta Sineva (2023). _[Some article name](link)_. Behavior Research Methods, 56(7), pages.


## Data

The corpus contain frequency data for 52 languages in `txt` and Excel (`xlsx`) formats. Note that for languages that have more than 100k unique words, the Excel version is reduced to the top 100k. You can see the full version in the corresponding `txt` file.

The data is organised in the following way:
* `data/word_freq`: the word frequencies for all languages, the full corpus version (named `[language name].word.freq`) as well as the version with the IPA information (named `[language name].word.freq.ipa`)
* `data/character_freq`: the word character frequencies for all languages (named `[language name].character.freq`)
* `data/bigram_freq`: the bigram frequencies for all languages (named `[language name].bigram.freq`). Note that the bigrams were extracted from within the word and not from within the sentence.

The files contain the frequency rank, the raw frequency, the frequency per million and the Zipf value of each word, as well as their IPA transcription in the IPA files. 
Note that different IPA transcriptions for the same word are separated by double-space | double-space rather than a single space for the sake of improving readability.

You can also find statistics information about the data in the directory `stats`.

The statistics information includes:
- the average word length within the text of the corpus
- the average word length of unique words in the corpus
- the total number of words (word characters, bigrams) in the text
- the total number of unique words (word characters, bigrams)
- A set of characters that were removed after the dataset pre-processing.


## Code

Run `main.py` to produce frequency files.
`main.py` takes the following arguments that allow you to modify the frequency data output:

| Argument | Full argument name | Description |
| --- | --- | --- |
| `-h` | `--help` | List available arguments. |
| `-f FILE` | `--file FILE` | The path to the data file with the `gz` extension (required). |
| `-x EXTENSION` | `--extension EXTENSION` | The extension of the file to export the data into (`txt`/`xlsx`/`csv`). Use \| for several data types (default: `txt|xlsx`) |
| `-i IPA` | `--ipa IPA` | The path to the directory containing the files with the IPA information from the Wikipron corpus. The IPA information will only be added to the data if the directory is provided. |
| `-c` | `--character` | Use to extract word character frequency information. |
| `-b` | `--bigram` | Use to extract bigram frequency information. |
| `-s` | `--stats` | Use to print out statistics about the data. |

_Usage_ _example_: 
If you would like to get the frequency data for German with IPA only in Excel format, and have the statistics information printed out, you can run the following in the command line:

```
python main.py -f OpenSubtitlesDirectoryName/de.txt.gz -x xlsx --ipa WikipronDirectoryName/ --stats
```
