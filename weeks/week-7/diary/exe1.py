import os

with open("diary.txt","w", encoding="utf-8") as f:
    f.write("15-1-2020: woolcom\n")
    f.write("15-2-2022: aharon\n")
    f.write("15-3-2022: weber\n")
    print("the diary was created successfully")

with open("diary.txt", "r", encoding="utf-8") as f:
    all = f.read()
    print (all)    


def add_entry(filename, date, content):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{date}: {content}\n")

def search_diary(filename, keyword):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if keyword in line:
                return line
            
def safe_read_diary(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()        
    except: FileNotFoundError




