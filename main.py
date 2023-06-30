#incomplete code
#incomplete code
#incomplete code
def my_bkash():
    print("1. Check balance")
    print("2. request statement")
    print("3. Change PIN")
    print("4. Priyo Number")
    print("5. Save Bill")  # incomplete code
    print("6. Update MNP")
    print("7. Confirm iPhone login")
    print("8. iPhone PIN reset")
    print("9. Helpline")
    print("0 Main menu")

def all():
  print("1. Send Money")
  print("2. Send Money to Non-Bkash User")
  print("3. Mobile Recharge")
  print("4. Payment")
  print("5. Cash Out")                                   #incomplete code
  print("6. Pay Bill")
  print("7. Microfinance")
  print("8. Download Bkash App")
  print("9. My Bkash")
  print("10. Reset PIN")
#incomplete code
#incomplete code
#incomplete code
def login():

  loginn = input("Bkash dial login code : ")
  if loginn == "*247#":
   all()
  else:
    print("Invalid login code")
  a = input()
  if a == "1":

    sendmoney = input("Enter receiver account no: ")
    if sendmoney == sendmoney:
       amount = input("Enter amount : ")
       if amount == amount:
         pin = input("Enter your pin number : ")
         if pin == pin:
          print(f"{amount} tk send to {sendmoney} this number")
    back =input()
    if back == "0":
     return all()
  elif a == "2":
      sendmoney = input("Enter receiver account no: ")
      if sendmoney == sendmoney:
          amount = input("Enter amount : ")
          if amount == amount:
              pin = input("Enter your pin number : ")
              if pin == pin:
                  print(f"{amount} tk send to {sendmoney} this number")
      back = input()
      if back == "0":
          return all()
  elif a == "3":
      sendmoney = input("Enter receiver account no: ")
      if sendmoney == sendmoney:
          amount = input("Enter amount : ")
          if amount == amount:
              pin = input("Enter your pin number : ")
              if pin == pin:
                  print(f"{amount} tk recharge to {sendmoney} this number")
      back = input()
      if back == "0":
          return all()
  elif a == "4":
      sendmoney = input("Enter receiver account no: ")
      if sendmoney == sendmoney:
          amount = input("Enter amount : ")
          if amount == amount:
              pin = input("Enter your pin number : ")
              if pin == pin:
                  print(f"{amount} tk paid to {sendmoney} this number")
      back = input()
      if back == "0":
          return all()
  elif a == "5":
      sendmoney = input("Enter agent account no: ")
      if sendmoney == sendmoney:
          amount = input("Enter amount : ")
          if amount == amount:
              pin = input("Enter your pin number : ")
              if pin == pin:
                  print(f"{amount} tk cashout from {sendmoney} this number")
      back = input()
      if back == "0":
          return all()
  elif a == "6":
      sendmoney = input("Enter receiver account no: ")
      if sendmoney == sendmoney:
          amount = input("Enter amount : ")
          if amount == amount:
              pin = input("Enter your pin number : ")
              if pin == pin:
                  print(f"{amount} tk recharge to {sendmoney} this number")
      back = input()
      if back == "0":
          return all()
  elif a == "7":
      sendmoney = input("Enter receiver account no: ")
      if sendmoney == sendmoney:
          amount = input("Enter amount : ")
          if amount == amount:
              pin = input("Enter your pin number : ")
              if pin == pin:
                  print(f"{amount} tk bill paid to {sendmoney} this number")
      back = input()
      if back == "0":
          return all()
  elif a == "8":
      print("session timeout, press 0")
      back = input()
      if back == "0":
          return all()
  elif a == "9":
      my_bkash()
      statement = input()
      if statement == "1":
         print("Bhai eikhaneo tk khujen?")
      back = input()
      if back == "0":
          return my_bkash()










if __name__ == "__main__":
    login()

#incomplete code
#incomplete code
#incomplete code
#incomplete code