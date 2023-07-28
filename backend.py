# importing googletrans library to do language translation     |          to print elements with key
import googletrans                                            #|         a = {'police':'A person who protect crimes' }  
                                                              #|            for element(any name as var) in a.items():
#  lets see what is inside googletrans                         |            print(element)
# print(dir(googletrans))  

# let's do the translation now
language_translator = googletrans.Translator() # global function


# let's create a function to extract the list of language    
def get_languages():                                     

    # lets see what all languages can our translator work with  
    language_info = googletrans.LANGUAGES 


    # empty language list  
    language_list = []  

    # iterating over the dictionary  
    for language in language_info.items():
     
       # extracting the languages and adding it to the language list 
       language_list.append(language[1])
    
    # let's return the list
    return language_list

# let's create a function to get the list of abbreviations 
def get_abbreviation():

    # lets see what all languages can our translator work with
    language_info = googletrans.LANGUAGES 


    # empty language list
    abbreviation_list = [] 

    # iterating over the dictionary  
    for language in language_info.items():
     
      # extracting the languages and adding it to the language list 
      abbreviation_list.append(language[0])
    
    # let's return the list
    return abbreviation_list
    
# let's define a function to do translations
def do_translation(text_to_be_translated, source_language, target_language):

    #  To use anything global from inside of a function, use the keyword global
    global language_translator

    #  let's call the translate function
    output=language_translator.translate(text=text_to_be_translated , dest = target_language, src=source_language)


    # extracting the text from the output
    translated_text = output.text
    
    #  return it
    return translated_text

#  let's call this function
result = do_translation('I love myself', 'en', 'hi' )
print(result)