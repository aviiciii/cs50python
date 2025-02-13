filename=input ('File: ').lower().strip()

dot=filename.rfind('.')

filetype=filename[dot:]

if filetype == '.jpg' or filetype == '.jpeg':
    print('image/jpeg')
elif filetype == '.gif':
    print('image/gif')
elif filetype == '.png':
    print('image/png')
elif filetype == '.pdf':
    print('application/pdf')
elif filetype == '.txt':
    print('text/plain')
elif filetype == '.zip':
    print('application/zip')
else :
    print('application/octet-stream')



# this method is more easier and allows a broader list instead of if-else everything.
types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
    "mp4": "video/mp4",
    "csv": "text/csv",
}

s = input("File name: ").strip().lower().split(".")[-1]
print(types.get(s, "application/octet-stream"))
