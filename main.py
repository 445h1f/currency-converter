import json

# setting base currency variables
BASE_CURRENCY_NAME = "U.S. Dollar"
BASE_CURRENCY_CODE = 'USD'

# list of supported search modes
MODES = ["number", "name", "code"]

# loading the currency data in data.json as a dict
# data credit: http://www.floatrates.com/daily/usd.json
currencyData =  json.load(open('data.json', encoding='utf8'))


# ascii art for greeting
welcomeArt = '''

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

░█████╗░██╗░░░██╗██████╗░██████╗░███████╗███╗░░██╗░█████╗░██╗░░░██╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝████╗░██║██╔══██╗╚██╗░██╔╝
██║░░╚═╝██║░░░██║██████╔╝██████╔╝█████╗░░██╔██╗██║██║░░╚═╝░╚████╔╝░
██║░░██╗██║░░░██║██╔══██╗██╔══██╗██╔══╝░░██║╚████║██║░░██╗░░╚██╔╝░░
╚█████╔╝╚██████╔╝██║░░██║██║░░██║███████╗██║░╚███║╚█████╔╝░░░██║░░░
░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░

░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░██╗
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝██║
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗╚═╝
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║██╗
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝\n\n'''

thanksArt = '''

▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █▀ █ █▄░█ █▀▀ █
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   █▄█ ▄█ █ █░▀█ █▄█ ▄'''

print(welcomeArt)
input(f'>>> Enter any key to get started...')


print(f'\n\n[*] You can enter name or number or code listed below of currencies to convert in {BASE_CURRENCY_NAME} ({BASE_CURRENCY_CODE}). \n\n')


# variable for currency number
num = 1

currencyNamesToCode = {} # dict for storing currencyName:currencyCode for name search mode
currencyDataKeys = [key for key in currencyData.keys()] # currency codes list for code search mode

# printing all the currency available for conversion

for currency in currencyData:
    currencyName = currencyData[currency]["name"].strip() # name of currency
    print(f'{num}: {currencyName} ({currency.upper()})')
    currencyNamesToCode[currencyName.lower()] = currency # adding name:code in currencyNamesToCode dict

    # asking user to display more currencies if multiple of 10 is already displayed
    if num % 10 == 0:
        morePromptText = f'>>> Showing {num} out of {len(currencyData)}... Enter "y" for more: '
        moreOutput = input(morePromptText).lower()
        print('\033[1A' + '\033[K', end='') # clearing input text ‘[1A’ says go up one line and the ‘[K’ says erase to the end of this line.

        if moreOutput != 'y': # breaking loop as user chosen not to display more data
            break

    num += 1 # incrementing the number by 1 for next currency number


print('\n\n')

# asking user to enter search mode
searchMode = input(f'>>> How would you like to search (number, name or code): ').lower().strip()

# validating search mode
if searchMode in MODES: # if mode is valid
    query = input(f'>>> Enter currency {searchMode}: ').lower().strip() # asking user for search query

    # flag to be set true when search is found otherwise diplay not founc
    searchFound = False

    if searchMode == "name": # for name search mode

        # checking if currency query name is in currencyNamesToCode dict
        if query in currencyNamesToCode:
            targetCurrencyCode = currencyNamesToCode[query] # getting currency code from currency name

            # setting search found to true as found in data
            searchFound = True
    elif searchMode == "code": # for code search mode
        # checking if query code is in currencyData dict
        if query in currencyData:
            targetCurrencyCode = query # setting targetCurrencyCode to search query as search mode is code
            searchFound = True
    else: # for number search mode
        # checking if query is number by converting into int
        try:
            index = int(query) - 1 # index of currency code is number - 1 as 0 based indexing
            targetCurrencyCode = currencyDataKeys[index] # getting targetCurrencyCode by index (if index range out of list exception part will be caught)
            searchFound = True
        except:
            pass

    # performing the conversion if search is found
    if searchFound:
        targetCurrencyName = currencyData[targetCurrencyCode.lower()]["name"].strip() # getting currecnyName from currency code
        conversionRate = currencyData[targetCurrencyCode.lower()]["inverseRate"] # getting conversion rate in usd for target currency
        targetCurrencyCode = targetCurrencyCode.upper()

        preciseRate = round(conversionRate, 5) # rounding off the conversion rate upto 5 decimal places

        # displaying conversion rate
        print(f'\n\n[*] 1 {targetCurrencyName} ({targetCurrencyCode}) = {preciseRate} {BASE_CURRENCY_NAME} ({BASE_CURRENCY_CODE})\n\n')


        # asking user for amount to convert in usd.
        # for invalid input except block will be executed.
        try:
            amount = float(input(f'>>> Enter how many {targetCurrencyCode} you want to convert: '))
        except:
            print(f'Invalid Amount!') # displaying invalid amount for invalid input
        else:
            # performing conversion if amount is greater than 0
            if amount > 0:
                convertedAmount = amount * preciseRate # converting the amount to usd

                # displaying the converted result
                print(f'\n\n[*] {amount} {targetCurrencyName} ({targetCurrencyCode}) = {round(convertedAmount, 5)} {BASE_CURRENCY_NAME} ({BASE_CURRENCY_CODE})\n')
                print(thanksArt)
            else:
                print('Amount must be greater than 0!') # displaying error for amount less than 0.
    else:
        print(f'Invalid search query.') # search query is not found or invalid
else:
    print(f'Invalid search mode!') # search mode is not in the defined search modes