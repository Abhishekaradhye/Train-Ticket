train_info = {'12345':{'ctype':{'2S':{'l':{'available':[1,4,7],
                                      'booked'  :[10,13,16]},
                                'm':{'available':[2,5,8],
                                     'booked'  :[11,14,17]},
                                'u':{'available':[3,6,9],
                                       'booked' :[12,15,18]} 
                                    }
                             }
                    }
              }
              
tno = input('Enter train number here : ')
if tno in train_info:
  cno = input('Enter coach type : ')
  if cno in train_info[tno]['ctype']:
    berth = input('Enter berth type : ')
    if berth in train_info[tno]['ctype'][cno]:
      count = len(train_info[tno]['ctype'][cno][berth]['available'])
      print(f"Number of berths available : {count}")
      available_berth_nos = train_info[tno]['ctype'][cno][berth]['available']
      print(available_berth_nos)
      try:
        btno = int(input('Enter the berth number to book : '))
        if btno in train_info[tno]['ctype'][cno][berth]['available']:
          train_info[tno]['ctype'][cno][berth]['available'].remove(btno)
          train_info[tno]['ctype'][cno][berth]['booked'].append(btno)
          print('Booking Succeeded.')
          print(f"{train_info[tno]['ctype'][cno][berth]['available']} are the available berths.")
          print(f"{train_info[tno]['ctype'][cno][berth]['booked']} are the booked berths.")
          print('...Thank You...')
        else:
          print('Error : Invalid berth number entered !')
      except ValueError as e:
        print('Error : You entered invalid berth number !')
    else:
      print('Error : Invaid berth !')
  else:
    print('Error : In valid coach type !')
else:
  print('Error : Invalid train number !')
