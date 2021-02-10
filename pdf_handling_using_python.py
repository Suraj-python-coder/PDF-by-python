# work with pdf files using python
# install PyPDF2
# read pdf file
# write to pdf files


# ## first we have to install PyPDF2 in  the python: pip install PyPDF2

import PyPDF2    

#  here we take one sample pdf file and open it using following instruction. in this pdf file , it very simple file only text presents.
my_file = open('sample.pdf','rb')    # in this we open pdf file in read binary mode (rb)

# read operation:
pdf_reader = PyPDF2.PdfFileReader(my_file)  # here we create an object to read the our opened pdf file.
# print(pdf_reader.numPages)     # here we count no.of pages avalable in our pdf.
# page_one = pdf_reader.getPage(0)  # here we read the data of page no.0 means in our language page no.1
# print(page_one.extractText())    # here we extract it and print it.

# for i in range(pdf_reader.numPages):    # here we extract full pdf file, read it and print it.
#     page = pdf_reader.getPage(i)
#     print(page.extractText())

#################### write to pdf #######################
# write operation: unfortunatly we cant write directly in any pdf file,
# [NOTE: WE APPEND SOME PAGES OF ONE PDF FILE TO ANOTHER PDF FILE.]

print(pdf_reader.numPages) 
page_one = pdf_reader.getPage(0)

output_file = open('new.pdf','wb')

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)
pdf_writer.write(output_file)


my_file.close()
output_file.close()

