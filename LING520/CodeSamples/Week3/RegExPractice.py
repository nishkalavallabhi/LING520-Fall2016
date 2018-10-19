import re
from urllib.request import urlopen

def get_input_url():
    link = input("Enter the wikipedia url: ")
    pattern = re.compile("<li class=\"interlanguage-link.*?>.*?</a></li>") #why the question mark after .*?
    #How to get this pattern above? Look at the source of HTML from browser.
    try:
        html = urlopen(link).read().decode(encoding="utf8").strip()
        temp_list = re.findall(pattern, html)
        for item in temp_list:
           #print(item) #printing this told me what should I split at in the next line.
           necessary_link = item.split("a href=\"")[1].split(" ")[0] #What is this???
           print(necessary_link)
    except:
        print("something is wrong with processing the url you gave. Quitting the program")
        exit()

def main():
    get_input_url()

if __name__ == "__main__":
    main()
