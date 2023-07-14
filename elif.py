## using elif statement instead of multiple if statements
#test with GPT summary

state = 'Aasam'
if state == 'Rajasthan':
    petorl_price = 108.18
    print('Petrol price in ',state, 'is ', petorl_price)
elif state == 'Maharashtra':
    petorl_price = 111.30
    print('Petrol price in ',state, 'is ', petorl_price)
elif state == 'Gujrat':
    petorl_price = 107.00
    print('Petrol price in ',state, 'is ', petorl_price)
else:
    petorl_price = 110.00
    print('Petrol price in ',state, 'is ', petorl_price)
