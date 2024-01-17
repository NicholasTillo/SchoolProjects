# Name:   <Nicholas Tillo>
# Student Number: <20291255>
# Email:  <20njt4@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

import tkinter as tk
import glob
from tkinter.constants import CENTER
from tkinter.filedialog import askdirectory
import os
import sys


text_1_text ="This is where your chosen directory will show up"
text_2_text ="This is where the files within the chosen directory will show up"
window = tk.Tk()
window.title("Main Window")
window.geometry("975x400")

def browse_button():
    '''Asks the user for a directory and then outputs it into a text box'''
    file_name = askdirectory()
    text_1.delete(1.0, tk.END)
    text_1.insert(tk.END, file_name)
    

def open_button():
    '''Takes the text from the the chosen directory and takes the names 
    outputting in a list to another text box.'''
    files = glob.glob(str(text_1.get("1.0",tk.END))[:-1] + "/" + "*.txt")
    finalstring = ""
    counter = 0
    for x in files:
        counter += 1
        finalstring += str(counter) + ". " + str(os.path.basename(x)) + "\n"

    text_2.delete(1.0,tk.END)
    text_2.insert(tk.END, finalstring)


def create_list_of_files(directory_list):
    '''Takes a list of the directory names and returns a list of the opened 
    files'''
    directory_set = []
    for value in directory_list:
        directory_set.append(open(value,"r", encoding = "utf8"))
    return directory_set


def create_stop_words():
    '''Opens the file stop words and creates a set of useable words'''
    stop_words = open("stop_words.txt","r")
    stop_words_set = set()
    for line in stop_words:
        stop_words_set.add(get_letters(line[:-1]))
    return stop_words_set


def get_letters(s):
    '''Inputs a word(string), and removes all non letters and 
    makes it lowercase'''
    word = ""
    for char in s:
        if char.isalpha():
            word += char.lower()
    return word


def create_set_book(cfile):
    '''Inputs a file, iterates through the lines, and words, taking out all
    stop words, all words that occur less than 5 times, and words with less
    than 3 letters.'''
    returning_set = set()
    temp2_dictionary = {}
    for clines in cfile:
        cline_words = clines.split()
        for cwords in cline_words:
            cword = get_letters(cwords)
            is_in = 0
            for swords in set_stopwords:
                if cword == swords:
                    is_in += 1

            if is_in == 0:
                if cword in temp2_dictionary:
                    temp2_dictionary[cword] += 1
                    if temp2_dictionary[cword] >= 5:
                       returning_set.add(cword)
                else:
                    temp2_dictionary[cword] = 1
             
    returning_set.discard("")
    return returning_set


def find_set_comparibility(set1, set2):
    '''Takes two sets and uses the Jaccard equation to return a value'''
    intersection = set1.intersection(set2)
    union = set1.union(set2)
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
                value2 = find_set_comparibility(temp_dictonary[i], 
                temp_dictonary[j])
                text1 = str(list_files[i]) + str(list_files[j])
                if bestnumber < value2:
                    bestnumber = value2
                    bestbook = str(list_files[j])
            
        dictionary_files[list_files[i]] = (bestbook, bestnumber)
    return dictionary_files
    

def compare_button():
    '''The main function, creates a secondary window, uses the selected 
    directory to gathter the text files within it. Then compared them to
    each other and outputs the book, recommendation, and the Jaccard number
    in a table on the secondary window.'''
    
    second_window = tk.Tk()
    second_window.title("Comparing Window")
    second_window.geometry("1200x800")
    column_1_head = tk.Label(second_window, text="Book 1", pady = 20)
    column_1_head.grid(row = 0, column = 1, padx = 175)
    column_2_head = tk.Label(second_window,text = "Book 2", pady = 20)
    column_2_head.grid(row = 0, column = 2, padx = 175)
    column_3_head = tk.Label(second_window,
    text = "Jaccard Simularity Result", pady = 20)
    column_3_head.grid(row=0, column = 3, padx = 175)
    list_of_files = glob.glob(str(text_1.get("1.0",tk.END))[:-1] 
    + "/" + "*.txt")

    if len(list_of_files) < 2:
        text_3.delete(1.0, tk.END)
        text_3.insert(tk.END, "Please Input a Valid Directory")
        second_window.destroy()
        return None
    
    final_dictionary = create_dictionary(create_list_of_files(list_of_files))
    counter = 0
    for result in final_dictionary:
        x = tk.Label(second_window, text = os.path.basename(list_of_files
        [counter]))
        x.grid(row = counter + 1, column = 1)
        y = tk.Label(second_window, text = os.path.basename(final_dictionary
        [result][0]).split("'")[0])

        #https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
        #The os.path.basename allows me to get the file name from a pathway

        y.grid(row = counter + 1, column = 2)
        z = tk.Label(second_window, text = final_dictionary[result][1])
        z.grid(row = counter + 1, column = 3)
        counter += 1
    second_window.mainloop()


set_stopwords = create_stop_words()
button = tk.Button(window, text ="Choose Directory", command = browse_button)
open_button_1 = tk.Button(window, text ="Open", command = open_button)
compare_button_1 = tk.Button(window,text = "Compare",comman = compare_button)

text_1 = tk.Text(window, width = 40)
text_2= tk.Text(window, width = 40)
text_3 = tk.Text(window, width = 40)
text_1.insert(tk.END, text_1_text)
text_1.grid(row = 2,column = 1)
text_2.insert(tk.END, text_2_text)
text_3.grid(row = 2, column = 3)
button.grid(row = 1,column = 1)
open_button_1.grid(row = 1,column = 2)
compare_button_1.grid(row = 1, column = 3)
text_2.grid(row = 2,column = 2)
window.mainloop()