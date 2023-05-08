import textwrap
message1 = '''today my visit to the jungle was very SPECIAL###
it was like all the life in the jungle was RESPONding to me###
it WAS big AND small animals###ANT; honey-dew; MORMON-butterfly; honey-bees; deers; bear; neelgay###

i sat there listening to the birds when a &&humming-bird&& sang a song
 and &&cuckoo&& was you know cuckooing and the &&koyel&& it gave the most aweSOME music'''
def reformat(message):
    z = ""
    message = message.replace(";", ",")
    message = message.replace("##", ". ")
    message = message.replace("&&", "'")
    message = message.replace(":", "")
    split_message = message.split("#")
    for x in split_message:
        """print("before- ", x)
        a = x.capitalize()
        print("after-", a)"""
        if x.startswith("\n"):
            x = x.replace("\n", "")
        x = x.capitalize()
        z = z + x

    z = textwrap.fill(z)
    return z
print(reformat(message1))

