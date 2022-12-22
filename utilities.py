
import csv

def listing_by_price(input_key, file, col1, col2, col3, col4, col5, path):
    name, price, web_site, new_prices, images, product_link = list(), list(), list(), list(), list(), list()
    item_and_index = {} #dictionary that associates each value to its index
    with open(file, encoding="UTF-8") as csv_file:
        reader = csv.DictReader(csv_file)

        #Put each row in a list
        for row in reader:
            images.append(row[col1])
            name.append(row[col2])
            price.append(row[col3])
            web_site.append(row[col4])
            product_link.append(row[col5])
            


        # Cleans the price list
        for i in range(len(price)):
            
            price[i] = price[i].strip().replace(" ", "").replace(",", "").replace("$", "")
            try:
                new_prices.append(float(price[i]))
                item_and_index[i] = float(price[i])
            except:
                continue

    file_name = f"{path}/{input_key}_by_prices.csv"
    with open(file_name, "w", encoding="UTF-8") as file:
        file.write(f"{col1},{col2},{col3},{col4},{col5}\n")

        for item in sorted(new_prices):
            item_index = list(item_and_index.keys())[list(item_and_index.values()).index(item)] #retrieving the index of each item

            file.write(f"{images[item_index]}, {name[item_index]}, ${item}, {web_site[item_index]}, {product_link[item_index]}\n") # write results

    print("Done")

