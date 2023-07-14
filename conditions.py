### practicing the conditional logic in python with if & elif
country = 'india'
state = 'Karnataka'
if country.capitalize() == 'India'
    if state.lower() in('rajasthan','gujrat','karnataka'):
        petorl_price = 108.18
        print('Petrol price in ',state, 'is ', petorl_price)
    elif state.lower() == 'maharashtra':
        petorl_price = 111.30
        print('Petrol price in ',state, 'is ', petorl_price)
else:
    petorl_price = 110.00
    print('Petrol price in ',state, 'is ', petorl_price)
