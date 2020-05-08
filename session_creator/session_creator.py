import os
import pandas
import sys

from input_functions import *
from process import *
from reaper_output import *
import settings as st


def main(list_file_path, output_file_path, audio_directory,
         distance_multiplier, column, row_range):

    if list_file_path[-3:] == 'txt':
        files_to_load = import_list_of_files(list_file_path)
        # elif list_file_path[-3:] == 'xls' or 'lsx':
        """ patrz co się dzieje w tym warunku: 
    In [1]: 'xls' == 'xls' or 'lsx'                                                                                                                                                
Out[1]: True

In [2]: 'lsx' == 'xls' or 'lsx'                                                                                                                                                
Out[2]: 'lsx'

In [3]: 'bollocks' == 'xls' or 'lsx'                                                                                                                                           
Out[3]: 'lsx'

In [4]: bool('xls' == 'xls' or 'lsx')                                                                                                                                          
Out[4]: True

In [5]: bool('lsx' == 'xls' or 'lsx')                                                                                                                                          
Out[5]: True

In [6]: bool('bollocks' == 'xls' or 'lsx')                                                                                                                                     
Out[6]: True

    - warunkek ten jest zawsze prawdziwy, bo jeśli pierwsza częśćzawiedzie, to bool('lsx') jest zawsze True

        """
    elif list_file_path[-3:] in ('xls', 'lsx', 'xlsx'):
        # mam problemy z załadowaniem pliku xls zrobionym na OSX...
        # files_to_load = get_filenames_from_excel_column(list_file_path, column, row_range[0], row_range[1])

        # następne 2 linijki załatwiają całe ładowanie excela (i .xls i .xlsx), bez względu na ilość wierszy
        df = pandas.read_excel(list_file_path)
        files_to_load = df['Filename'].values

    # get the filenames from directory
    all_files, wav_files = get_all_and_wave_filenames_from_directory(
                                                            audio_directory)

    """Process and analyze"""

    # compare text list and real files and print results
    good_files, extra_files, files_not_present = \
        compare_list_and_wave_files_in_directory(
            files_to_load, wav_files, audio_directory)

    # create wavefile objects from the good files and create dummies
    wavefiles = create_wavefile_objects(files_to_load, good_files,
                                        audio_directory)

    # inpect wavefiles for inconsistencies and print results
    inspect_files(wavefiles)

    """Write"""
    # generate final string
    project = generate_reaper_project(wavefiles, distance_multiplier)

    # write it to file
    # można by też zapewnić rozszerzenie .RPP, jeśli użytkownikowi zabraknie ( z życia wzięte ;)
    with open(output_file_path, 'w') as f:  # tu było unresolved reference, natomiast output_file_path nie zostało użyte
        f.write(project)


# For CLI use
if __name__ == '__main__':

    arguments = sys.argv[1:]

    """Read files"""
    (list_file_path, output_file_path, directory, distance_multiplier,
     column, row_range) = parse_cli_arguments(arguments)

    errors, row_range, distance_multiplier = validate_input(
        list_file_path, output_file_path, directory, distance_multiplier,
        column, row_range)

    if errors:
        print(f'Input errors: {errors}.')
        print('"python3 session_creator.py -h" for help.')
    else:
        main(list_file_path, output_file_path, directory, distance_multiplier,
             column, row_range)
