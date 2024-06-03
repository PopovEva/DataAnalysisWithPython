import csv
from enum import Enum
from rich import print 
from statistics import median
from collections import defaultdict

class Operations(Enum):
    MAX_PRICE = 1
    AVRG_PRICE = 2
    IDEAL_DIAMONDS = 3
    COLORS = 4
    MEDIAN_CARAT_PREMIUM = 5
    AVRG_CARAT_CUT = 6
    AVRG_PRICE_COLOR = 7
    EXIT = 8
    
def menu():
    for oper in Operations: print(f'{oper.value} - {oper.name}')   
    return Operations(int(input("Choose your action:")))

def read_csv(csv_filename):
    with open(csv_filename, mode='r') as file:
        return list(csv.DictReader(file))

def find_max_price(data):
    max_price = 0
    for row in data:
        price = int(row['price'])
        if price > max_price:
            max_price = price
    return max_price    

def find_average_price(data):
    total_price = 0
    count = 0
    for row in data:
        total_price += int(row['price'])
        count += 1
    return total_price / count if count else 0

def count_ideal_diamonds(data):
    return sum(1 for row in data if row['cut'] == 'Ideal')

def count_unique_colors(data):
    colors = set(row['color'] for row in data)
    return len(colors), colors

def find_median_carat_premium(csv_filename):
    with open(csv_filename, mode='r') as file:
        return median(float(row['carat']) for row in csv.DictReader(file) if row['cut'] == 'Premium')

def find_average_carat_by_cut(data):
    carat_by_cut = defaultdict(list)
    for row in data:
        carat_by_cut[row['cut']].append(float(row['carat']))
    average_carat_by_cut = {cut: sum(carats)/len(carats) for cut, carats in carat_by_cut.items()}
    return average_carat_by_cut        

def calculate_average_price_by_color(data):
    price_sum_by_color = defaultdict(float)
    count_by_color = defaultdict(int)
    for row in data:
        color_type = row['color']
        price_sum_by_color[color_type] += int(row['price'])
        count_by_color[color_type] += 1
    average_price_by_color = {color: price_sum_by_color[color] / count_by_color[color] for color in price_sum_by_color}
    return average_price_by_color

if __name__ == "__main__":  
        filename = 'data.csv'
        data = read_csv(filename)
        num_colors, unique_colors = count_unique_colors(data)
        while True:
            try:
                user_selection = menu()
                if user_selection== Operations.EXIT: exit() 
                elif user_selection== Operations.MAX_PRICE: 
                    print(f"[green]The highest price of a diamond:[/] {find_max_price(data)}") 
                elif user_selection== Operations.AVRG_PRICE:
                    average_price = find_average_price(data)
                    print(f"[green]Average arithmetic price of a diamond:[/] {average_price:.2f}") 
                elif user_selection== Operations.IDEAL_DIAMONDS:
                    ideal_count = count_ideal_diamonds(data)
                    print(f"Number of 'Ideal' cut diamonds: {ideal_count}")  
                elif user_selection== Operations.COLORS: 
                    print(f"[bold magenta]Number of different diamond colors:[/] {num_colors}")
                    print(f"[bold magenta]Unique diamond colors:[/] {', '.join(unique_colors)}")  
                elif user_selection== Operations.MEDIAN_CARAT_PREMIUM:
                    print(f"The median carat size for 'Premium' diamonds is: {find_median_carat_premium(filename)}") 
                elif user_selection == Operations.AVRG_CARAT_CUT:
                    print('[green]Whait for answer..[/]' )
                    average_carat_by_cut = find_average_carat_by_cut(data)
                    for cut, avg_carat in average_carat_by_cut.items():
                        print(f"Average carat weight for '{cut}' cut diamonds: {avg_carat:.2f}")    
                elif user_selection == Operations.AVRG_PRICE_COLOR:
                    average_price_color = calculate_average_price_by_color(data)
                    for color, avg_price in average_price_color.items():
                        print(f"Average price for color '{color}': {avg_price:.2f}")                 
            except Exception as e:
                print("[red]Incorrect syntax, try again:[/] ")   
                print("[red]Choose a action number:[/] ")     
                