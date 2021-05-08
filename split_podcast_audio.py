from audioclipextractor import AudioClipExtractor, SpecsParser

# Inicialize the extractor
ext = AudioClipExtractor('/Users/p/code/scrap/scripts/src/data/28_vacunas.mp3', '/Users/p/code/scrap/scripts/src/data/')

# Define the clips to extract
# It's possible to pass a file instead of a string
specs = '''
    3.5     17      Winter is coming.
    26      32.4    Summer child.
    40      58.9    Hodor. Hodor. Hodor.
'''

# Extract the clips according to the specs and save them as a zip archive
ext.extract_clips(specs, '/Users/p/code/scrap/scripts/src/data/', zip_output=True)


