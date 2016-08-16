# -*- coding: utf-8 -*-
import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        temp_dict={}
        strings = string.ascii_lowercase + string.ascii_uppercase
#        str1 = strings[:shift]
#        str2 = strings[shift:]
#        str_shift = str2 + str1
        
        if len(string.ascii_lowercase) > shift >= 0 :
            str1 = strings[:shift]
            str2 = strings[shift:]
            str_shift = str2 + str1
            
            
            for i in range(len(string.ascii_lowercase + string.ascii_uppercase)):
                temp_dict[i]= str_shift[i]
#            for i in temp_dict:
#                if i + shift < temp_dict :
#                    print temp_dict[i],
#                print len(temp_dict)
#                print i +shift ,
        return temp_dict  
        #pass #delete this line and replace with your code here

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        temp_dict = self.build_shift_dict(shift)
        default_dict = {}
        temp_text = self.message_text
        empty_text = ""
        strings = string.ascii_lowercase + string.ascii_uppercase

        for i in range(len(string.ascii_lowercase + string.ascii_uppercase)):
                default_dict[i]= strings[i]
        
        for i in temp_text:
            if i in default_dict.values():
                #print default_dict.values().index(i) , temp_dict.values().index(i) ,i
                #print temp_dict[default_dict.values().index(i)]
                #print default_dict.keys()[default_dict.values().index(i)]
            
                empty_text +=  temp_dict[default_dict.values().index(i)] ## Ayto einai super
            if i in  string.punctuation or i == " ":
                empty_text+=i
            
#        print string.punctuation + " "
#        print temp_text
        return empty_text
##        print Message(self.message_text).build_shift_dict(5)
#        print temp_dict.values()


word = 'samurai are cool dudes!'
wordlist = load_words("words.txt")
msg = Message(word)
#print msg
#print is_word(wordlist, word)
#print msg.build_shift_dict(4)
print msg.apply_shift(5)