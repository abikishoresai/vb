file_to_load = "raw_data/paragraph_1.txt"

with open(file_to_load, 'r') as reader:
    num_line = 0
    num_word = 0
    num_letter = 0        
    for row in reader:
        print(row)
        wordsList = row.split()
        num_line += 1
        num_word += len(wordsList)
        num_letter += len(row)
        print(num_line)
        print(num_word)
        print(num_letter)
