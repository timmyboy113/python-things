plaintext    = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
encrytedtext = list('DEFGHIJKLMNOPQRSTUVWXYZABC')

def message(text, plain, encryp):
    dictionary = dict(zip(plain, encryp))
    newmessage = ''
    for char in text:
        try:
            newmessage += dictionary[char]
        except:
            newmessage += ' '
    print text, '\nhas been encrypted to:'
    print newmessage
	
text = raw_input("Test:")	
message(text,plaintext,encrytedtext)
input()
