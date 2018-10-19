from bottle import get, post, request, route, template, run
import re
import string

def do_tokenize(someString):
   pattern = "[" + string.punctuation + "]"
   allOccurences = re.findall(pattern, someString)
   print("These are the locations of tokenization in this sentence: ", allOccurences) #Just for checking.
   for i in range(0,len(allOccurences)):
       someString = someString.replace(allOccurences[i], " " +
                                       allOccurences[i] +" ")
       someString = re.sub(r"\s+","\n",someString)
   return someString

@route('/')
@get('/tokenize')
def ask_tokenize():
    return '''
        <textarea form ="formid" name="taname" id="taid" cols="35" wrap="soft"></textarea>
        <form action="/tokenize" method="post" id="formid">
            <input value="Tokenize" type="submit" />
        </form>
    '''

@post('/tokenize')
def post_tokenize():
    someString = request.forms.get('taname')
    return "<b>Your tokenized string is:</b> <br />" + \
           "<textarea rows=\"20\" cols=\"40\" wrap=\"soft\" readonly>" \
            + do_tokenize(someString) \
           + "</textarea>"


run()
