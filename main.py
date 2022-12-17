from amazon import amazon
from canez import canez
from casami import casami
from digicel import digicel
from ebay import ebay
import os, csv
from flask import Flask, render_template
from utilities import listing_by_price


col1, col2, col3, col4 = "image", "product_name", "price", "web_site"

def main():

    user = os.getlogin()
    directory = "ScrappingResults"
    path = f"C:/Users/{user}/Downloads/{directory}"
    try:
        os.makedirs(path)
    except:
        print()

    input_key = input("Enter the key search : ")

    headers = f"{col1},{col2},{col3},{col4}\n"
    file_name = f"{path}/{input_key}.csv"
    with open(file_name, "w", encoding="UTF-8") as file:
        file.write(headers)
    
    print("Collecting infos from Amazon web site...")
    amazon(input_key, file_name)

    print("Collecting infos from Casami web site...")
    casami(input_key, file_name)    

    print("Collecting infos from Valerio Canez web site...")
    canez(input_key, file_name)

    
    print("Collecting infos from Digicel web site...")
    digicel(input_key, file_name)

    print("Collecting infos from Ebay web site...")
    ebay(input_key, file_name)

    print("Sorting results by price...")
    listing_by_price(input_key, file_name, col1, col2, col3, col4, path)

app = Flask(__name__)

@app.route('/')
def result():
    with open("C:\\Users\\Mydleyka\\Downloads\\ScrappingResults\\samsung_by_prices.csv", encoding="UTF-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return render_template('index.html', result = reader)


if __name__ == '__main__':
    # main()
    app.run(debug = True)