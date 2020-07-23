from flask import Flask, render_template, request
import requests 
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/s_w', methods =['POST'])
def search():
    word=request.form['word_to_search']
    url='https://yourdictionary.com/%s'%word
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    meaning=soup.find('ol', class_='sense')
    result=meaning.find_all('div' , 'custom_entry')
    output="."
    for result in result:{
        output=+ result.text + "\n\n"
        #temp=output;
        }
    return render_template('meaning.html', mean=output)

    #return redirect(url_for)output 

    #meaning=meaning.text.strip()
    #return meaning
    #return redirect('meaning.html', meaning)

   
   
   
   
    #mean='Taher'
   # return        mean
    #return render_template('meaning.html', meaning=meaning)


    #return redirect("https://www.merriam-webster.com/dictionary/%s"%word)
    
    
    
    #return render_template('index.html')
    #return 'Word= %s'%word 
    #return "https://www.merriam-webster.com/dictionary/%s"%word

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")