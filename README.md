# PyUploadGram

An API wrapper for UploadGram

# Installation
not on pyPi soo..
    
    git clone https://github.com/scrubjay55/PyUploadGram
    pip3 install ./PyUploadGram


# Usage

```python
import PyUploadGram

pyuploadgram_sesh = PyUploadGram.Session()

b_somephoto = open(r"./somephoto.jpeg", 'rb').read()
uploaded_file = pyuploadgram_sesh.upload_file(filename="some photo.jpeg",
                                              file=b_somephoto
                                              )
# OR
uploaded_file2 = pyuploadgram_sesh.upload_file(filename="some photo2.jpeg",
                                               file=r"./somephoto.jpeg"
                                               )
print(uploaded_file)
# (UploadedFile: url=https://dl.uploadgram.me/********?raw, delete=******)

# DIRECTLY FROM THE INTERNET
some_media_u = pyuploadgram_sesh.upload_file(filename="some media.jpg",
                                             file="https://i.redd.it/xxxxxxx.jpg"
                                             )
# OR
b_some_media = requests.get("https://i.redd.it/xxxxxxx.jpg").content
some_media_u2 = pyuploadgram_sesh.upload_file(filename="some media.jpg",
                                              file=b_some_media
                                              )

is_succesfully_deleted = pyuploadgram_sesh.delete_file(uploaded_file)
print(is_succesfully_deleted)
# True
print(pyuploadgram_sesh.uploaded_files)

# ALSO POSSIBLE WITHOUT A SESSION
PyUploadGram.upload_file(filename="some file.o",
                         file=r"./someobj.o"
                         )

```
