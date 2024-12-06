from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url= f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    print(url)
    content = requests.get(url).text
    soup = BeautifulSoup(content,"html.parser")
    rate = soup.find("span",class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])

    
    return rate

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('test.html')



@app.route('/api/v1/<in_curr>-<out_cur>')
def api(in_curr, out_cur):
    rate = get_currency(in_curr,out_cur)
    result_dic = {'input_currency: ': in_curr, 'output_currency: ': out_cur, 'rate: ':rate}
    return jsonify(result_dic)


if __name__ == '__main__':
    app.run()