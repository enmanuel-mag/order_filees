# File Organizer

This little script of python move your file in dosnload folder to a another folder that you specific.

# Usage

## How set custom folder destination?

You only need create a file called paths.csv in the same directory where is the file **order_downloads.py**. Some like this:

```
.
└── you_folder
    ├── order_downloads.py
    └── paths.csv
```

Inside og **paths.csv** you must specific where move the type of each type file, to do this jsut put the path where you and that move the file.

Initial content of paths.csv
````
img,<your path>
doc,<your path>
prog,<your path>
.
.
.
````

Next I create a way to specific what format fo file is a type. For now the format and type is configured like this:

- img  -> ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
       
- prog -> ('.exe', '.msi', '.jar')
      
- doc  -> ('.pdf', '.docx', '.xlsx', '.zip', '.rar', '.txt'))
        
- musc -> ('.mp3', '.wav')
    
- vid  -> ('.mp4', '.vlc')

Now you run the python file or set a scheduled in you task scheduler to run it when you whant.