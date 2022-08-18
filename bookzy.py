"""bookzee (feel free to steal idea or register domain before me) """

import csv
#deposits csv
deposits_2018 = 'Deposits_20222.csv'
extended_deposits = 'EtsyDirectCheckoutPayments20222.csv'
current_month = 'Feb_2022-2.csv'
# fees = float(row[8])  #feb
fees_2018 = 0

materials_2018 = 0
crystal_cost = 0
assets_2018 = 0

with open(extended_deposits, 'r') as f:
  next(f) #skips the first row
  net_deposit = 0
  gross_deposit = 0
  fees = 0
  for row in csv.reader(f):
    gross_deposit += float(row[7])
    net_deposit += float(row[9])
    fees += float(row[8])

  print('The total gross amount is: {}'.format(gross_deposit))
  print('The total net deposit amount is: {}'.format(net_deposit))
  print('The total fees are: {}'.format(fees))
  print('Total materials is: {}'.format(materials_2018))
  print('Net deposit minus materials in 2022: ')
  print(net_deposit - materials_2018)
