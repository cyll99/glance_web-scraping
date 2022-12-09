from ss import amazon
from casami import casami
from digicel import digicel
from ebay import ebay


def main():
    input_key = input("Enter the key search : ")
    headers = "product_name,price \n\n"
    file_name = str(input_key) +".csv"
    with open(file_name, "w", encoding="UTF-8") as file:
        file.write(headers)
    
    print("Collecting infos from Amazon web site...")
    amazon(input_key, file_name)

    print("Collecting infos from Casami web site...")
    casami(input_key, file_name)

    print("Collecting infos from Digicel web site...")
    digicel(input_key, file_name)

    print("Collecting infos from Ebay web site...")
    ebay(input_key, file_name)

if __name__ == '__main__':
    main()