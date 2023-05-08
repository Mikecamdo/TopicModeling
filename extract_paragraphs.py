def extract_paragraphs():
    file1 = "1969-70.txt"
    file2 = "1996-97.txt"
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    text= f1.readlines()
    text.append(f2.readlines())
    hold = ""
    paragraphs = []
    for line in text:
        hold += line
        if len(line) < 70:
            if len(hold) > 70:
                paragraphs.append(hold)
                hold = ""
    return paragraphs