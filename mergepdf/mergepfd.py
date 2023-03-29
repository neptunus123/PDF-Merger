# Python Code created by Cemhan Baykal.
# A simple pdf merging application that merges multiple pdf files into a single pdf output file.

from PyPDF2 import PdfMerger

# creating a pdf file merger object
birlestirici = PdfMerger(strict=False)

# append pdf one by one with their path names. (Do not forget to include the path names such as: birlestirici.append('c:/user/user/pdf1.pdf, 'rb')
birlestirici.append('pdf1.pdf', 'rb')
birlestirici.append('pdf1.pdf', 'rb')
birlestirici.append('pdf1.pdf', 'rb')
birlestirici.append('pdf1.pdf', 'rb')

# writing combined pdf to output pdf file
# with open('Merged.pdf', 'wb') as fout:
#     birlestirici.write(fout)

birlestirici.write('merged.pdf')
birlestirici.close()

# NOTE: The output file goes to the same location as the python file's directory.
