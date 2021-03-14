import math, requests, re, collections, copy, os.path
import easygui as gui
from bs4 import BeautifulSoup

def input_exists(): #Kontrollib kas sisendfail nimega ASI.txt eksisteerib
    if not os.path.exists('ASI.txt'):
        print('!!! Provide an input file \'ASI.txt\'')
        quit()

def find_rate_EUR(): #Tagastab sõnastiku kurssidest
    input_exists()

    try:
        print('Fetching data...')
        req = requests.get('https://www.eestipank.ee/valuutakursid').text
    except:
        print('Failed to fetch exchange data')
        quit()

    all_rates = BeautifulSoup(req, 'html.parser').find_all('td', class_='views-field-field-currency-rate')
    currency = ['USD', 'GBP', 'NOK', 'SEK', 'RUB']
    num = [30, 8, 4, 26, 25]
    rates = {}

    for x, y in zip(currency, num):
        rates[x] = float(re.sub(r'[\n\t\s]*', '', all_rates[y].text).replace(',', '.'))

    rates['EUR'] = float(1)

    return rates

def all_notes(rates): #Tagastab pangaautomaadis olevad kupüürid sõnastikuna
    file = open('ASI.txt','r').read().split('\n')
    available_notes = {}

    for i in file:
        i = i.replace(' ','')
        notes = {}

        if i != '':
            for x in i[4:].split(';'):

                x = x.split('-')
                note = int(x[0])
                amount = int(x[1].replace('tk',''))
                notes[note] = amount

            available_notes[i[:3]] = notes

    return available_notes

def values(): #Raha koguse, valuuta ja soovitava valuuta valimine
    amount = gui.enterbox('Enter the amount to exchange',title)

    while not amount.isdecimal() or amount == None:
        gui.msgbox('Invalid amount!')
        amount = gui.enterbox('Enter the amount to exchange',title)

    amount = float(amount)
    og_note = gui.enterbox('Enter the currency',title)

    while og_note.upper() not in ['GBP','NOK','RUB','SEK','USD','EUR']:
        gui.msgbox('Invalid currency!',title)
        og_note = gui.enterbox('Enter the currency',title)

    og_note = og_note.upper()
    new_note = gui.enterbox('Enter the desirable currency',title)

    while new_note.upper() not in ['GBP','NOK','RUB','SEK','USD','EUR']:
        gui.msgbox('Invalid currency!',title)
        new_note = gui.enterbox('Enter the desirable currency',title)

    new_note = new_note.upper()

    return (amount, og_note, new_note)

def min_notes(banknotes, new_note): #Kui valitakse, et soovitakse väikseim arv kupüüre tagasi
    global all_notes, exchange_amount, wallet
    notes = copy.copy(banknotes[new_note])
    first = True

    while True:
        for x in sorted(notes):

            if all_notes[new_note][x] <= 0:
                notes.remove(x)

        if all_notes[new_note][min(all_notes[new_note].keys())] <= 0 or notes == []:
            gui.msgbox('Sorry, but we are out of banknotes',title)
            break

        if exchange_amount - min(notes) < 0:
            if first:
                gui.msgbox('Insufficient funds or out of banknotes!',title)
            break

        else:
            for x in notes:
                for _ in range(all_notes[new_note][x]):
                    
                    if exchange_amount - x > 0 and all_notes[new_note][x] > 0:
                        all_notes[new_note][x] -= 1
                        exchange_amount -= x
                        wallet.append(x)

                    else:
                        break
        first = False

def max_notes(banknotes, new_note): #Kui valitakse, et soovitakse suurim arv kupüüre tagasi
    global all_notes, exchange_amount, wallet
    notes = copy.copy(banknotes[new_note])
    first = True

    while True:
        for x in sorted(notes):

            if all_notes[new_note][x] <= 0:
                notes.remove(x)

        if all_notes[new_note][max(all_notes[new_note].keys())] <= 0 or notes == []:
            gui.msgbox('Sorry, but we are out of banknotes',title)
            break

        if exchange_amount - min(notes) < 0:
            if first:
                gui.msgbox('Insufficient funds or out of banknotes!',title)
            break

        else:
            for x in notes[::-1]:
                for _ in range(all_notes[new_note][x]):

                    if exchange_amount - x > 0 and all_notes[new_note][x] > 0:
                        all_notes[new_note][x] -= 1
                        exchange_amount -= x
                        wallet.append(x)

                    else:
                        break
        first = False

def only_small(banknotes, new_note): #Kui soovitakse raha tagasi saada vaid väikestes kupüürides
    global all_notes, exchange_amount, wallet
    notes = copy.copy(banknotes[new_note])
    notes = notes[len(notes)//2:]
    first = True

    while True:
        for x in notes:
            for _ in range(all_notes[new_note][x]):

                    if exchange_amount - x > 0 and all_notes[new_note][x] > 0:
                        all_notes[new_note][x] -= 1
                        exchange_amount -= x
                        wallet.append(x)

                    else:
                        break
        if all_notes[new_note][min(all_notes[new_note].keys())] <= 0 or notes == []:
            gui.msgbox('Sorry, but we are out of banknotes',title)
            break

        for x in sorted(notes):
            if all_notes[new_note][x] <= 0:
                notes.remove(x)

        if exchange_amount - min(notes) < 0:
            if first:
                gui.msgbox('Insufficient funds or out of banknotes!',title)
            break
        first = False

def only_big(banknotes, new_note): #Kui soovitakse raha tagasi saada vaid suurtes kupüürides
    global all_notes, exchange_amount, wallet
    notes = copy.copy(banknotes[new_note])
    notes = notes[:len(notes)//2]
    first = True

    while True:
        for x in notes:
            for _ in range(all_notes[new_note][x]):

                    if exchange_amount - x > 0 and all_notes[new_note][x] > 0:
                        all_notes[new_note][x] -= 1
                        exchange_amount -= x
                        wallet.append(x)

                    else:
                        break

        if all_notes[new_note][min(list(all_notes[new_note].keys())[:len(notes)])] <= 0 or notes == []:
            gui.msgbox('Sorry, but we are out of banknotes',title)
            break

        for x in notes[:len(notes)//2]:
            if all_notes[new_note][x] <= 0:
                notes.remove(x)

        if exchange_amount - min(notes) < 0:
            if first:
                gui.msgbox('Insufficient funds or we are out of banknotes!',title)
            break
        first = False

def custom(banknotes, new_note): #Kui soovitakse kindlaid kupüüre
    global all_notes, exchange_amount, wallet
    notes = copy.copy(banknotes[new_note])
    custom = {i : int(gui.enterbox(f'Enter the number of {i} {new_note} notes, 0 if You want none',title)) for i in notes}

    for i in custom.values():
        if i == None:
            return None

    if sum([i*custom[i] for i in custom]) < exchange_amount:
        for i in custom:

            if all_notes[new_note][i] < custom[i]:
                gui.msgbox(f"Sorry, we don't have enough {i} {new_note} banknotes, will give all available notes")
                custom[i] = all_notes[new_note][i]

        exchange_amount -= sum([i*custom[i] for i in custom])
        wallet = [i for i in custom for x in range(custom[i])]

    else:
        gui.msgbox('Insufficient funds!', title)

def all_sum(banknotes, new_note): #Kontrollib et raha ei antaks rohkem tagasi kui vahetada sooviti
    global all_notes, exchange_amount, wallet
    _quit = False
    cont = True
    notes = copy.copy(banknotes[new_note])

    if sum(notes) < exchange_amount:

        for i in range(int(exchange_amount // sum(notes))):
            for x in notes:
                for _ in range(all_notes[new_note][x]):

                    if exchange_amount - x > 0 and all_notes[new_note][x] > 0:
                        all_notes[new_note][x] -= 1
                        exchange_amount -= x
                        wallet.append(x)

                    else:
                        break
                else:
                    cont = False
                    break

            if not cont:
                break
    else:
        gui.msgbox('Insufficient funds!',title)
        _quit = True

    while not _quit:
        for x in sorted(notes):

            if all_notes[new_note][x] <= 0:
                notes.remove(x)

        if notes == [] or exchange_amount - min(notes) < 0:
            break

        else:
            for x in notes:
                for _ in range(all_notes[new_note][x]):

                    if exchange_amount - x > 0 and all_notes[new_note][x] > 0:
                        all_notes[new_note][x] -= 1
                        exchange_amount -= x
                        wallet.append(x)

                    else:
                        break

def final_string(wallet, unexchangeable, new_note, og_note): #Lõpu teksti koostaja
    wallet = dict(collections.Counter(wallet))
    string = ''

    for i in wallet:
        string += f'You got {wallet[i]} {i} {new_note} banknotes\n'

    string += f'\n{unexchangeable} {og_note} was not exchanged'
    return string

 
exchange = True
title = 'Money exchange'
rate = find_rate_EUR()
all_notes = all_notes(rate)
banknotes = {i : sorted(all_notes[i].keys(), reverse=True) for i in rate if i in all_notes.keys()}

gui.msgbox('EUR, RUB, NOK, GBP, SEK, USD exchange',title, ok_button='Start')

#Peamine programm, kus rahavahetus toimub
while exchange:
    amount, og_note, new_note = values()

    if new_note in all_notes.keys():

        exchange_amount = amount / rate[og_note] * rate[new_note]
        wallet = []

        if exchange_amount < min(banknotes[new_note]):
            gui.msgbox('Insufficient funds to exchange!',title)

        elif all_notes[new_note] == []:
            gui.msgbox(f'Sorry, we are out of {new_note} notes',title)
        else:

            mode = gui.choicebox('Choose the desirable exchange mode', title, ['Minimum number of notes','Maximum number of notes','Only small notes','Only big notes','Custom number of notes','All different notes'])
            if mode == 'Minimum number of notes':
                min_notes(banknotes, new_note)

            elif mode == 'Maximum number of notes':
                max_notes(banknotes, new_note)

            elif mode == 'Custom number of notes':
                custom(banknotes, new_note)

            elif mode == 'All different notes':
                all_sum(banknotes, new_note)

            elif mode == 'Only small notes':
                only_small(banknotes, new_note)

            elif mode == 'Only big notes':
                only_big(banknotes, new_note)

            unexchangeable = math.floor(round(exchange_amount / rate[new_note] * rate[og_note], 5)*100)/100
            gui.msgbox(final_string(wallet, unexchangeable, new_note, og_note),title)
            exchange = gui.ynbox('Do you want to make another exchange?', title)

    else:
        gui.msgbox('That currency is not in the ATM!')
    
