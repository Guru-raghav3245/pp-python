message = '''today my visit to the jungle was very SPECIAL###
it was like all the life in the jungle was RESPONding to me###
it WAS big AND small animals###ANT; honey-dew; MORMON-butterfly; honey-bees; deers; bear; neelgay###

i sat there listening to the birds when a &&humming-bird&& sang a song
 and &&cuckoo&& was you know cuckooing and the &&koyel&& it gave the most aweSOME music'''
capital = message.split("###")
#print(capital)
#print(capital[0].capitalize())
for x in capital:
    x = x.replace("\n", "")
    print(x.capitalize())

