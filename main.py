import telegram.ext

with open('token.txt', 'r') as f:
   Token = f.read()

def start(update, context):
     
updater= telegram.ext.updater(Token, use_context=True)
disp= updater.dispatcher