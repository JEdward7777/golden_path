 #!/usr/bin/env python3

#  Similar to [5] the published data Tokenizer, this data abstractor provides a common
# API to the AI solution for accessing the data so that the AI solution is dataformat agnostic. It also tokenizes the
# data so that the AI solution is language agnostic. There can be a different data abstraction written for each language
# and data format source.
import os
from ... import common_data_tools

datafile = "../f11_Language_data/German.xml"
 


def getVerse_tokenized( reference: str ) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    abs_datafile = os.path.join(dir_path,datafile )

    #where to place intermediate files.
    work_folder = os.path.dirname(os.path.abspath(__file__))

    reference_str = common_data_tools.translate_reference( reference )
    verses_tokenized_str = common_data_tools.get_or_train_tokenization( abs_datafile, work_folder )
    return verses_tokenized_str[reference_str]

def getVerseReferences() -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    abs_datafile = os.path.join(dir_path,datafile )

    #where to place intermediate files.
    work_folder = os.path.dirname(os.path.abspath(__file__))

    verses_tokenized_str = common_data_tools.get_or_train_tokenization( abs_datafile, work_folder )
    return list(verses_tokenized_str.keys())


if __name__ == '__main__': print( getVerse_tokenized( "John 3:16") )