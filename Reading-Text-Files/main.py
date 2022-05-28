def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        txt = f.read()
        return txt

def count_words(str):
    # [assignment] Add your code here
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print (count_words(read_file_content("./story.txt")))




   