
def my_bkash():
    print("1. Check balance")
    print("2. request statement")
    print("3. Change PIN")
    print("4. Priyo Number")
    print("5. Save Bill")
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
  print("6. Pay Bill")                                   #www.facebook.com/muzahidsife
  print("7. Microfinance")
  print("8. Download Bkash App")
  print("9. My Bkash")
  print("10. Reset PIN")

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

      elif statement == "2":
          print("Successfully statement requested")

          back = input()
          if back == "0":
              return my_bkash()

      elif statement == "3":

          number = input("Your phone number :")
          if number == number:
              change_pin = input("Your previous PIN : ")
              Current_pin = input("Set PIN : ")
              print(f"Yor Bkash PIN ({change_pin}) changed to {Current_pin}")
              back = input()
              if back == "0":
                  return my_bkash()

      elif statement == "4":
          priyo_number = input("Add a priyo number: ")

          if len(priyo_number) == 11 or 13 or 14:
              if priyo_number.startswith("+880"):
                  priyo_number = "+880" + priyo_number[4:]
              elif priyo_number.startswith("880"):
                  priyo_number = "+880" + priyo_number[3:]
              else:
                  priyo_number = "+880" + priyo_number[1:]

          print(f"You successfully added {priyo_number} as your priyo number.")

      elif statement =="5":
          save_bill =input("Enter your bill number : ")
          print(f"Your {save_bill} number has been saved ")

      elif statement =="6":
          print("Bkash MNP service isn't available right now")

      elif statement =="7":
          print("This service isn't available right now")

      elif statement =="8":
          print("This service isn't available right now")

      elif statement =="9":
          print("Contact customer care -16247")

      elif statement == "0":
          return all()

  elif a == "10":
      print("Contact customer care -16247")


if __name__ == "__main__":
    login()

