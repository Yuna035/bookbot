def get_word_count(book_text):
    words = book_text.split() 
    return len(words)
 

def get_char_counts(book_text):
    counts = {} 
    for c in book_text:
        string = c.lower()
        if string in counts:
            counts[string] +=1
        else:
            counts[string] = 1
    return counts 
 

def sort_on(d):
    return d["num"]


def list_letters(chars_count_dict):
    char_list = [] 
    for char in chars_count_dict:            
        if char.isalpha():
            char_list.append({"char":char,"num":chars_count_dict[char]})  
    char_list.sort(reverse=True, key=sort_on)   
    return char_list                       
        
     
   
    