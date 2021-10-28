 #!/usr/bin/env python3

 
#  Similar to [5] the published data Tokenizer, this data abstractor provides a common
# API to the AI solution for accessing the data so that the AI solution is dataformat agnostic. It also tokenizes the
# data so that the AI solution is language agnostic. There can be a different data abstraction written for each language
# and data format source.

import xml.etree.ElementTree as ET
import functools
import os,re

datafile = "../11_Language_data/Hebrew.xml"
 

reference_regex = re.compile("(?P<book>([0-9] ?)?[^0-9]*\\S)\\s*(?P<chapter>[0-9]+):(?P<verse>[0-9]+)")

book_name_lookup = {
    "Genesis":"GEN",
    "Exodus":"EXO",
    "Leviticus":"LEV",
    "Numbers":"NUM",
    "Deuteronomy":"DEU",
    "Joshua":"JOS",
    "Judges":"JDG",
    "Ruth":"RUT",
    "1 Samuel":"1SA",
    "2 Samuel":"2SA",
    "1 Kings":"1KI",
    "2 Kings":"2KI",
    "1 Chronicles":"1CH",
    "2 Chronicles":"2CH",
    "Ezra":"EZR",
    "Nehemiah":"NEH",
    "Esther":"EST",
    "Job":"JOB",
    "Psalms":"PSA",
    "Proverbs":"PRO",
    "Ecclesiastes":"ECC",
    "Song of Songs":"SON",
    "Song of Solomon":"SON",
    "Isaiah":"ISA",
    "Jeremiah":"JER",
    "Lamentations":"LAM",
    "Ezekiel":"EZE",
    "Daniel":"DAN",
    "Hosea":"HOS",
    "Joel":"JOE",
    "Amos":"AMO",
    "Obadiah":"OBA",
    "Jonah":"JON",
    "Micah":"MIC",
    "Nahum":"NAH",
    "Habakkuk":"HAB",
    "Zephaniah":"ZEP",
    "Haggai":"HAG",
    "Zechariah":"ZEC",
    "Malachi":"MAL",
    "Matthew":"MAT",
    "Mark":"MAR",
    "Luke":"LUK",
    "John":"JOH",
    "Acts":"ACT",
    "Romans":"ROM",
    "1 Corinthians":"1CO",
    "2 Corinthians":"2CO",
    "Galatians":"GAL",
    "Ephesians":"EPH",
    "Philippians":"PHI",
    "Colossians":"COL",
    "1 Thessalonians":"1TH",
    "2 Thessalonians":"2TH",
    "1 Timothy":"1TI",
    "2 Timothy":"2TI",
    "Titus":"TIT",
    "Philemon":"PHM",
    "Hebrews":"HEB",
    "James":"JAM",
    "1 Peter":"1PE",
    "2 Peter":"2PE",
    "1 John":"1JO",
    "2 John":"2JO",
    "3 John":"3JO",
    "Jude":"JUD",
    "Revelation":"REV"
}

"""
This gets the verse from this data source.  It returns untokenized scripture reference for the tokenizer to tokenize.
"""
def getVerse( reference: str ) -> str:
    reference_match = reference_regex.match( reference )
    if not reference_match: return None
    book = reference_match["book"]
    if book not in book_name_lookup: return None
    chapter = reference_match["chapter"]
    verse = reference_match["verse"]
    book = book_name_lookup[book]
    reference_str = "b." + book + "." + chapter + "." + verse
    verses = load_verses()
    return verses[ reference_str ] if reference_str in verses else None

def load_xml():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    #https://docs.python.org/3/library/xml.etree.elementtree.html
    tree = ET.parse( os.path.join(dir_path,datafile ) )
    root = tree.getroot()
    return root

@functools.lru_cache(maxsize=None)
def load_verses():
    verses = {}
    root = load_xml()
    for seg in root.iter( "seg"):
        concat = []
        for section in seg.findall( "./s" ):
            concat.append( section.text )
        verses[ seg.get( 'id' ) ] = " ".join( concat )

    return verses


if __name__ == '__main__': print( getVerse( "John 3:16") )