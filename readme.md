# DAW Session Creator

A tool for automatic creation of DAW sessions, based on the list of files supplied in .txt or Excel format. Designed with audio post-production studios in mind.

## Installation

Does not require installation. Uses only Python 3.6 internal library.

## Usage

session_creator.py [-h] [--dist [DIST]] [--range [RANGE]] input_file_path output_file_path audio_directory



Positional arguments:

  input_file_path:      Path to a file with the list of required files: txt or xls/xlsx.

  output_file_path:      Path to an output file: suported filetypes: RPP
                        (Reaper).

  audio_directory:       Path to a directory with the audio files.

Optional arguments:

  -h, --help:            show this help message and exit

  --dist [DIST], -d [DIST]: Distance between regions as multiple of the previous
                        file's length.

  --range [RANGE], -r [RANGE]: Location of filenames in the spreadsheet, e.g. "A2:A20". Required if an Excel spreadsheet is specified as input file.


## License
[MIT](https://choosealicense.com/licenses/mit/)
