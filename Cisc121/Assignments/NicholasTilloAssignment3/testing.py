import tkinter as tk
import glob
from tkinter.filedialog import askdirectory
import os

window = tk.Tk()
#print(list_of_files)

def create_list_of_files(directory_list):
    '''Takes a list of the directory names and returns a list of them'''
    directory_set = []
    for value in directory_list:
        directory_set.append(open(value,"r", encoding = "utf8"))
    return directory_set


def create_stop_words():
    '''Opens the file stop words and creates a set of useable words'''
    stop_words = open("Assignments/NicholasTilloAssignment3/stop_words.txt", "r")
    stop_words_set = set()
    for line in stop_words:
        stop_words_set.add(line[:-1])
    return stop_words_set


def get_letters(s):
    '''Inputs a word(string), and removes all non letters and makes it lowercase'''
    word = ""
    for char in s:
        if char.isalpha():
            word += char.lower()
    return word


def create_set_book(cfile):
    '''Inputs a file, iterates through the lines, and words, taking out all
    stop words, all words that occur less than 5 times, and words with less
    than 3 letters.'''
    #print(file)
    returning_set = set()
    temp2_dictionary = {}
    for clines in cfile:
        cline_words = clines.split()
        for cwords in cline_words:
            cword = get_letters(cwords)
            set_word = set()
            set_word.add(cwords)
            if len(cword) > 3 and not set_word.issubset(set_stopwords):
                if cword in temp2_dictionary:
                    temp2_dictionary[cword] += 1
                    if temp2_dictionary[cword] >= 5:
                        returning_set.add(cword)
                else:
                    temp2_dictionary[cword] = 1
    returning_set.discard("")
    return returning_set

#Set Intersection

#print(set_stopwords.intersection(set_book_file))
#print(len(set_stopwords.intersection(set_book_file)))

def find_set_comparibility(book1, book2):
    '''Takes two files and uses the Jaccard equation to return the value'''
    intersection = book1.intersection(book2)
    union = book1.union(book2)
    value = len(intersection) / len(union)
    return value


def create_set_dictonary(list_of_files):
    '''Takes a set of files and gets a set of words for each one, putting it 
    into a dictionary'''
    returning_dict = {}
    for values in range(len(list_of_files)):
        returning_dict[values] = create_set_book(list_of_files[values])
    return returning_dict


def create_dictionary(list_files):
    '''Takes a list of files and creates a dictionary, the value being a 
    tuple, the first value being the most similar book, the second value being
    the Jaccard value'''
    dictionary_files = {}
    temp_dictonary = create_set_dictonary(list_files)
    for i in range(len(list_files)):
        bestnumber = 0
        for j in range(len(list_files)):
            if j != i:
                value2 = find_set_comparibility(temp_dictonary[i], temp_dictonary[j])
                text1 = str(list_files[i]) + str(list_files[j])
                if bestnumber < value2:
                    bestnumber = value2
                    bestbook = str(list_files[j])
            
        dictionary_files[list_files[i]] = (bestbook, bestnumber)
    return dictionary_files
    

set_stopwords = create_stop_words()

def compare_button():
    '''The main function, creates a secondary window, uses the selected 
    directory to gathter the text files within it. Then compared them to
    each other and outputs the book, recommendation, and the jaccard number
    in a table on the secondary window.'''
    second_window = tk.Tk()
    second_window.title("Comparing Window")
    second_window.geometry("1200x800")
    column_1_head = tk.Label(second_window, text="Book 1", pady = 20)
    column_1_head.grid(row = 0, column = 1, padx = 175)
    column_2_head = tk.Label(second_window,text = "Book 2", pady = 20)
    column_2_head.grid(row = 0, column = 2, padx = 175)
    column_3_head = tk.Label(second_window,text = "Jaccard Simularity Result", pady = 20)
    column_3_head.grid(row=0, column = 3, padx = 175)


    files = askdirectory()
    list_of_files = glob.glob((files)+"/"+"*.txt")
    yup = create_dictionary(create_list_of_files(list_of_files))

    counter = 0
    for poop in yup:
        x = tk.Label(second_window, text = os.path.basename(list_of_files[counter]))
        x.grid(row = counter + 1, column = 1)
        y = tk.Label(second_window, text = os.path.basename(yup[poop][0]).split("'")[0])

        #https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format

        y.grid(row = counter + 1, column = 2)
        z = tk.Label(second_window, text = yup[poop][1])
        z.grid(row = counter + 1, column = 3)
        counter += 1
    second_window.mainloop()


compare_button_1 = tk.Button(window, text="Compare", command = compare_button)
compare_button_1.grid(row= 3, column = 2)
window.mainloop()