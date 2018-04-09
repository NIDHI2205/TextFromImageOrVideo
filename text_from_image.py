from PIL import Image
import pytesseract

<<<<<<< HEAD
im = Image.open("test_data/test_image_4.jpg")
text = pytesseract.image_to_string(im, lang = 'eng')
#text = pytesseract.image_to_string(im)

=======
im = Image.open("test_data/test_image_1.png")
text = pytesseract.image_to_string(im, lang = 'eng')
#text = pytesseract.image_to_string(im)
>>>>>>> parent of 0a13601... Revert "TextFromImageOrVideoCommit"
print(text)
