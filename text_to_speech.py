import pyttsx3
from PyPDF2 import PdfReader

# open the PDF file in binary mode
with open('typing certificate 1.pdf', 'rb') as pdf_file:
    # create a PDF reader object
    reader = PdfReader(pdf_file)

    # initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # get the available voices
    voices = engine.getProperty('voices')

    # set the voice to a female voice
    engine.setProperty('voice', voices[1].id)

    # get the total number of pages in the PDF file
    total_pages = len(reader.pages)

    # ask the user which page to start reading from
    start_page = int(input(f"Enter the page number to start reading (1 - {total_pages}): "))

    # loop over the pages starting from the user-specified page
    for page_num in range(start_page - 1, total_pages):
        # extract the text from the current page
        page = reader.pages[page_num]
        text = page.extract_text()

        # convert the extracted text to speech
        engine.say(text)
        engine.runAndWait()

        # ask the user if they want to continue reading or stop
        user_input = input("Press 's' to stop reading, or any other key to continue: ")
        if user_input == 's':
            break
