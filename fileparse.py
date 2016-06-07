'''
Reads through files and parses out paragraphs (denoted by newline characters)
'''
def parse():
    f = open('input.txt', 'r')
    
    text = []
    
    line = f.readline()
    
    while(line is not ""):
        if line is not "\n":
            text += [line[:len(line)-1]] #-2 is to remove \n from line end
        line = f.readline()
         
    
    text.remove('')
            
    print(text)
    
    return text
    