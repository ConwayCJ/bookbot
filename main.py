
def main():
    path = './books/frankenstein.txt'

    with open(path) as f:
        text = f.read()
         
        def get_num_words(text = text):
             
            words = text.split()
            word_count = len(words)
            return word_count

        # return dict: {"a": 1, "b": 2}
        def get_num_letters():

            letter_dict = {}
            for word in text.split():
                for letter in word:
                    let = letter.lower().strip()            

                    if let in letter_dict:
                        letter_dict[let] += 1
                    else:
                        letter_dict[let] = 1
            return letter_dict

        def sort_on(dict):
            return dict["num"]
        
        def sort_dict(num_chars_dict):
            newL = []
            for ch in num_chars_dict:
                newL.append({"char": ch, "num": num_chars_dict[ch]})
            newL.sort(reverse=True, key=sort_on)
            return newL
        
        

        print(f"""--- Begin report of {path} ---
              {get_num_words()} found in the document              
              """)
        letter_dict = sort_dict(get_num_letters())

        for key in letter_dict:
            print(f"The '{key['char']}' character was found {key['num']} times")
        print("--- End report ---")
    

main()