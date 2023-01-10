MORSE_CODE_DICT = { 'A':'.- ', 'B':'-... ',
                    'C':'-.-. ', 'D':'-.. ', 'E':'. ',
                    'F':'..-. ', 'G':'--. ', 'H':'.... ',
                    'I':'.. ', 'J':'.--- ', 'K':'-.- ',
                    'L':'.-.. ', 'M':'-- ', 'N':'-. ',
                    'O':'--- ', 'P':'.--. ', 'Q':'--.- ',
                    'R':'.-. ', 'S':'... ', 'T':'- ',
                    'U':'..- ', 'V':'...- ', 'W':'.-- ',
                    'X':'-..- ', 'Y':'-.-- ', 'Z':'--.. '} 
def to_morse_code(mapping,string1):
    outpustring=""
    for item in range(len(string1)): 
        string1=string1.upper()
        if string1[item] in mapping:
            outpustring+=" "+mapping[string1[item]]              
    print(outpustring)


print(to_morse_code(MORSE_CODE_DICT,"me[rh(aba du)n]ya"))           
        
        
    
    


