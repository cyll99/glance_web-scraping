from amazon import amazon
from canez import canez
from casami import casami
from digicel import digicel
from ebay import ebay
import csv


def main():
    input_key = input("Enter the key search : ")
    col1, col2, col3 = "product_name", "price", "web_site"

    headers = f"{col1},{col2},{col3}\n"
    file_name = str(input_key) +".csv"
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
    listing_by_price(input_key, file_name, col1, col2, col3)

def listing_by_price(input_key, file, col1, col2, col3):
    name, price, web_site, new_prices = list(), list(), list(), list()
    item_and_index = {} #dictionary that associates each value to its index
    with open(file, encoding="UTF-8") as csv_file:
        reader = csv.DictReader(csv_file)

        #Put each row in a list
        for row in reader:
            name.append(row[col1])
            price.append(row[col2])
            web_site.append(row[col3])


        # Cleans the price list
        for i in range(len(price)):
            
            price[i] = price[i].strip().replace(" ", "").replace(",", "").replace("$", "")
            try:
                new_prices.append(float(price[i]))
                item_and_index[i] = float(price[i])
            except:
                continue


    with open(input_key+"_by_prices.csv", "w", encoding="UTF-8") as file:
        file.write(f"{col1},{col2},{col3}\n")

        for item in sorted(new_prices):
            item_index = list(item_and_index.keys())[list(item_and_index.values()).index(item)] #retrieving the index of each item

            file.write(f"{name[item_index]}, ${item}, {web_site[item_index]}\n") # write results

    print("Done")



if __name__ == '__main__':
    main()