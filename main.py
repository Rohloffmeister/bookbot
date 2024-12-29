


def count_words(text):
    return len(text.split())

def count_characters(text):
    character_dic = {}
    converted_text = "".join(text.split()).lower()
    characters = "a b c d e f g h i j k l m n o p q r s t u v w x y z ä ö ü".split(" ")
    
    for character in converted_text:
        
        if character in characters:
            if character not in character_dic:
                character_dic[character] = 1
            else:
                character_dic[character] += 1
   
    return dict(sorted(character_dic.items(),reverse=True,key=lambda  item: item[1]))
  

def main():
    book_path="books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    
    character_dic = count_characters(file_contents)
    word_count = count_words(file_contents)
    
    print("--- Begin report of " + book_path + "---")
    print(str(word_count) + " words found in the document")
    print()
    
    for key in character_dic:
        print(f"The '{key}' character was found {character_dic[key]} times")
        
    
    
    
    
    
    
    
main()