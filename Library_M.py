print("*****************************************************************************")
print("*****************************************************************************")
print("***************************Welcome to DJH Library ***************************")
print("*****************************************************************************")
print("*****************************************************************************")
namel=input("Enter the librarian name : ")
pw=int(input("Enter your library code :"))
name=input("\nEnter your name : ")
for i in range(1,10):
     age=int(input("Enter your age : "))
     if age>5 and age<100:
          break
     else:
          print("Enter your correct age")
          continue
for i in range(0,10):
     gen=input("Gender(male/female) : ")
     if gen[0:6]=="female":
          break
     elif gen[0:4]=="male":
          break
     else:
          continue
for i in range(1,10):
     date=input("Date(DD/MM/YYYY) : ")
     if "2020" in date:
               break
     elif "2021" in date:
               break
     else:
          continue
add=input("Enter your address : ")
for i in range(0,10):
     phone=int(input("Phone number : "))
     ph=str(phone)
     if len(ph)!=10:
          p=print("*****Give the Correct Phone number*****")
          continue
     else:
          break
#Library books available
for i in range(1,20):
     choice=int(input("\nTypes of book available are :\n\t1.General book \n\t2.Noval book \n\t3.Fantasy and Comic Book\n\t4.Action and Adventure \n\t5.Horror,Detective and Mystery \n\t6.Move onto the next step.\n\nEnter the type of book you recommend :")) 
     if choice==1:
          print("\nGeneral book")
          choice=int(input("\n The books under this category are  :\n\t1.Encyclopedia \n\t2.General knowledge quiz book \n\t3.Oxford Dictionary\n\nSelect the book :"))
          if choice==1:
                   print("\nTitle of the book : Encyclopedia")
                   aut="Jean le Rond d Alembert and Denis Diderot"
                   acc=101
                   typ="Scholarly source"
                   print("Author of the book :",aut)
                   print("Account number :",acc)
                   print("Type of book :",typ)
          elif choice==2:
                   print("\nTitle of the book : General knowledge quiz book")
                   aut="Derek O Brien"
                   acc=102
                   typ="Quiz"
                   print("Author of the book :",aut)
                   print("Account number :",acc)
                   print("Type of book :",typ)
          elif choice==3:
                   print("\nTitle of the book : Oxford Dictionary")
                   pub="Oxford University Press"
                   acc=103
                   typ="Dictionary"
                   print("Publisher of the book :",pub)
                   print("Account number :",acc)
                   print("Type of book :",typ)
          else:
                print("\nIf you want other general book please say us")
                general=input("Enter the general book name : ")
     elif choice==2:
                print("\nNoval book")
                choice=int(input("\nThe books under this category are \n\t1.Normal People \n\t2.An Era of Darkness \n\t3.Fear:Trump in the White House \n\t4.The Farthest Field \n\t5.Golden Child \n\t6.Half The Night Is Gone \n\t7.The Overstory \n\t8.Interior Chinatown \n\t9. King and the Dragonflies \n\t10.The Dead Are Arising : The Life of Malcolm X\n\nSelect the type of noval book:"))
                if choice==1:
                     print("\nTitle of the book : Normal People")
                     aut="Sally Rooney"
                     acc=201
                     typ="Love Story"
                     Award="Costa book award 2019"
                     print("Author of thebook :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                     print("Award :",Award)
                elif choice==2:
                     print("\nTitle of the book : An Era of Darkness")
                     aut="Shashi Tharoor"
                     acc=202
                     typ="Inglorious Empire"
                     Award="Sahitya Akademi Award 2019"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                     print("Award :",Award)
                elif choice==3:
                     print("\nTitle of the book - Fear:Trump in the White House")
                     aut="Bob Woodward"
                     acc=203
                     typ="Story of the President of the United of America"
                     Award="PEN America Literary Service Award 2019"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                     print("Award :",Award)
                elif choice==4:
                     print("\nTitle of the book : The Farthest Field")
                     aut="Raghu Karnad"
                     acc=204
                     typ="non-friction"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                elif choice==5:
                     print("\nTitle of the book : Golden Child")
                     aut="Claira Adam"
                     acc=205
                     typ="Story about Clyde and his twin sons"
                     Award="Desmond Elliott Prize"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                     print("Award :",Award)
                elif choice==6:
                     print("\nTitle of the book : Half The Night Is Gone")
                     aut="Amitabha Bagchi"
                     acc=206
                     Award="DSC Prize"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Award :",Award)
                elif choice==7:
                     print("\nTitle of the book : The Overstory")
                     aut="Richard Power"
                     acc=207
                     typ="Tree and people(Friction)"
                     Award="Pulitzer Prize"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                     print("Award :",Award)
                elif choice==8:
                     print("\nTitle of the book : Interior Chinatown")
                     aut="Charles Yu"
                     acc=208
                     typ="Friction"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                elif choice==9:
                     print("\nTitle of the book : King and the Dragonflies")
                     aut= "Kacen Callender"
                     acc=209
                     typ="Young people literature"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                elif choice==10:
                     print("\nTitle of the book - The Dead Are Arising: The Life of Malcolm X")
                     aut="Les Payne and Tamara Payne"
                     acc=210
                     typ="Non-friction"
                     print("Author of the book :",aut)
                     print("Account number :",acc)
                     print("Type of book :",typ)
                else:
                     print("\nIf you want other noval book please say us")
                     noval=input("Enter the noval name : ")
     elif choice==3:
               print("\nFantasy and Comic Book")
               choice=int(input("\nThe books under this category are\n\t1.Nimona \n\t2.Saga \n\t3.The Secret of the nagas \n\t4.Rat Queen \n\t5.The spire \n\t6.The Stonekeeper \n\t7.Seven to Eternity \n\t8.Sandman \n\t9.Bone \n\t10.Birthright\n\nSelect the type of Fantasy and Comic book:"))
               if choice==1:
                     print("\nTitle of the book : Nimona")
                     aut="Noelle Stevenson"
                     acc=301
                     print("Author of the book :",aut)
                     print("Account number :",acc)
               elif choice==2:
                     print("\nTitle of the book : Saga")
                     aut="Brian K.Vaughan,Fiona Staples"
                     acc=302
                     print("Author of the book :",aut)
                     print("Account number :",acc)
               elif choice==3:
                     print("\nTitle of the book : The Secret of the nagas")
                     aut="Amish Tripathi"
                     acc=303
                     print("Author of the book :",aut)
                     print("Account number :",acc)
               elif choice==4:
                     print("\nTitle of the book : Rat Queen")
                     aut="Kurtis J Wiebe,Roc Upchurch"
                     acc=304
                     print("Author of the book :",aut)
                     print("Account number :",acc)
               elif choice==5:
                     print("\nTitle of the book : The spire")
                     aut="Simon Sprrier,Jeff Stokely"
                     acc=305
                     print("Author of the book :",aut)
                     print("Account number :",acc)
               elif choice==6:
                     print("\nTitle of the book : The Stonekeeper")
                     aut="Kazu Kibuishi"
                     acc=306
                     print("Author of the book :",aut)
                     print("Account number :",acc)
               elif choice==7:
                    print("\nTitle of the book : Seven to Eternity")
                    aut="Rich Remender,Jerome Opena"
                    acc=307
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==8:
                    print("\nTitle of the book : Sandman ")
                    aut="Neil Gaiman"
                    acc=308
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==9:
                    print("\nTitle of the book : Bone")
                    aut="Jeff Smith"
                    acc=309
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==10:
                    print("\nTitle of the book : Birthright")
                    aut="Nora Roberts"
                    acc=310
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               else:
                    print("\nIf you want other fantasy and comic book please say us")
                    fantasy , comic=input("Enter the fantasy and comic book name : ")
     elif choice==4:
               print("\nAction and Adventure")
               choice=int(input("\nThe books under this category are \n\t1.Jurassic Park \n\t2.The Hunger Game \n\t3.The Da Vinci Code \n\t4.The Bourne Identity \n\t5.Divergent \n\t6.The Count of Monte Cristo \n\t7.The Hunt for Red October \n\t8.Harry Potter \n\t9.Rhythm of War \n\t10.Devoted\n\nSelect the type of action and adventure book:"))
               if choice==1:
                    print("\nTitle of the book : Jurassic Park")
                    aut="Michael Crichton"
                    acc=401
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==2:
                    print("\nTitle of the book : The Hunger Game")
                    aut="Suzanne Collins"
                    acc=402
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==3:
                    print("\nTitle of the book :The Da Vinci Code")
                    aut="Dan Brown"
                    acc=403
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==4:
                    print("\nTitle of the book : The Bourne Identity ")
                    aut="Robert Ludlum"
                    acc=404
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==5:
                    print("\nTitle of the book : Divergent ")
                    aut="Veronica Roth"
                    acc=405
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==6:
                    print("\nTitle of the book : The Count of Monte Cristo")
                    aut="Alexandre Dumas"
                    acc=406
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==7:
                    print("\nTitle of the book : The Hunt for Red October")
                    aut="Tom Clancy"
                    acc=407
                    print("Author of the book :",aut)
                    print("Account number :",acc)
               elif choice==8:
                   print("\nTitle of the book : Harry Potter ")
                   aut="J.K. Rowling."
                   acc=408
                   print("Author of the book :",aut)
                   print("Account number :",acc)
               elif choice==9:
                   print("\nTitle of the book : Rhythm of War ")
                   aut=" Brandon Sanderson"
                   acc=409
                   print("Author of the book :",aut)
                   print("Account number :",acc)
               elif choice==10:
                   print("\nTitle of the book : Devoted")
                   aut="Dean Koontz"
                   acc=410
                   print("Author of the book :",aut)
                   print("Account number :",acc)
               else:
                   print("\nIf you want other action and adventure book please say us")
                   action , adventure=input("Enter the action and adventure book name : ")
     elif choice==5:
              print("\nHorror,Detective and Mystery")
              choice=int(input("\nThe books under this category are\n\t1.The Last Dickens \n\t2.Bookhunter \n\t3.The Turkish Gambit \n\t4.The Hound of the Baskervilles \n\t5.Dracula \n\t6.The Mystery of Marie Roget \n\t7.The Silence of the Lambs \n\t8.Last Days \n\t9.The Shining \n\t10.Red Dragon\n\nSelect the type of Horror,Detective and Mystery book :"))
              if choice==1:
                   print("\nTitle of the book : The Last Dickens")
                   aut="Matthew Pearl"
                   acc=501
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==2:
                   print("\nTitle of the book :Bookhunter")
                   aut="John Hill Burton"
                   acc=502
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==3:
                   print("\nTitle of the book : The Turkish Gambit ")
                   aut="Boris Akunin"
                   acc=503
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==4:
                   print("\nTitle of the book : The Hound of the Baskervilles")
                   aut="Arthur Conan Doyle"
                   acc=504
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==5:
                   print("\nTitle of the book : Dracula ")
                   aut="Bram Stoker"
                   acc=505
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==6:
                   print("\nTitle of the book : The Mystery of Marie Roget")
                   aut="Edgar Allan Poe"
                   acc=506
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==7:
                   print("\nTitle of the book : The Silence of the Lambs ")
                   aut="Thomas Harris"
                   acc=507
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==8:
                   print("\nTitle of the book : Last Days")
                   aut="Adam Nevill"
                   acc=508
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==9:
                   print("\nTitle of the book : The Shining ")
                   aut="Stephen King"
                   acc=509
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              elif choice==10:
                   print("\nTitle of the book : Red Dragon")
                   aut="Thomas Harris"
                   acc=510
                   print("Author of the book :",aut)
                   print("Account number :",acc)
              else:
                   print("\nIf you want other Horror,Detective and Mystery book please say us")
                   Horror,Detective ,Mystery=input("Enter the Horror,Detective and Mystery book name : ")
     elif choice==6: 
              break
print("\nYou are here to:")
choice=int(input("\n\t1.Borrow a book \n\t2.Read a book \n\t3.Return the book \n\t4.Read a newspaper \n\t5.Read a magazine\nEnter the choice : "))
print("\nYou can enter the library ")
print("\n.........After your work is done,you have to answer some questions and then get a receipt to leave the library...........")

if choice==1:
    print("\n***************************************************************\n")
    print("\n**************** You have borrowed a book ****************\n")
    print("\n***************************************************************\n")
    for i in range(1,10):
         n=input("Name : ")
         if n==name:
              break
         else:
              print("Enter the same name as above")
              continue
    for i in range(1,10):
         a=int(input("Age : "))
         if a==age:
              break
         else:
              print("Enter the same age as above")
              continue
    for i in range(0,10):
         gen=input("Gender(male/female) : ")
         if gen[0:6]=="female":
              break
         elif gen[0:4]=="male":
              break
         else:
              continue
    for i in range(1,10):
        phone=int(input("Phone number : "))
        ph=str(phone)
        if len(ph)!=10:
            p=print("*****Give the Correct Phone number*****")
            continue
        else:
          break
    a=input("Address : ")
    for i in range(1,10):
         nl=input("In which language do you want the book(english/malayalam/tamil/telugu/kannadam/hindi) : ")
         if nl=="english" or nl=="malayalam" or nl=="tamil" or nl=="telugu" or nl=="kannadam" or nl=="hindi":
              break
         else:
              continue
    ac=int(input("Account number of the book : "))
    if ac==101:
          print("Title of the book : Encyclopedia")
    elif ac==102:
          print("Title of the book : General knowledge quiz book")
    elif ac==103:
          print("Title of the book : Oxford Dictionary")
    elif ac==201:
          print("Title of the book : Normal People")
    elif ac==202:
          print("Title of the book : An Era of Darkness")
    elif ac==203:
          print("Title of the book - Fear:Trump in the White House")
    elif ac==204:
          print("Title of the book : The Farthest Field")
    elif ac==205:
          print("Title of the book : Golden Child")
    elif ac==206:
          print("Title of the book : Half The Night Is Gone")
    elif ac==207:
          print("Title of the book : The Overstory")
    elif ac==208:
          print("Title of the book : Interior Chinatown")
    elif ac==209:
          print("Title of the book : King and the Dragonflies")
    elif ac==210:
          print("Title of the book - The Dead Are Arising: The Life of Malcolm X")
    elif ac==301:
          print("\nTitle of the book : Nimona")
    elif ac==302:
          print("\nTitle of the book : Saga")
    elif ac==303:
          print("\nTitle of the book : The Secret of the nagas")
    elif ac==304:
          print("\nTitle of the book : Rat Queen")
    elif ac==305:
          print("\nTitle of the book : The spire")
    elif ac==306:
          print("\nTitle of the book : The Stonekeeper")
    elif ac==307:
          print("\nTitle of the book : Seven to Eternity")
    elif ac==308:
          print("\nTitle of the book : Sandman ")
    elif ac==309:
          print("\nTitle of the book : Bone")
    elif ac==310:
          print("\nTitle of the book : Birthright")
    elif ac==401:
          print("\nTitle of the book : Jurassic Park")
    elif ac==402:
          print("\nTitle of the book : The Hunger Game")
    elif ac==403:
          print("\nTitle of the book :The Da Vinci Code")
    elif ac==404:
          print("\nTitle of the book : The Bourne Identity ")
    elif ac==405:
          print("\nTitle of the book : Divergent ")
    elif ac==406:
          print("\nTitle of the book : The Count of Monte Cristo")
    elif ac==407:
          print("\nTitle of the book : The Hunt for Red October")
    elif ac==408:
          print("\nTitle of the book : Harry Potter ")
    elif ac==409:
          print("\nTitle of the book : Rhythm of War ")
    elif ac==410:
          print("\nTitle of the book : Devoted")
    elif ac==501:
          print("\nTitle of the book : The Last Dickens")
    elif ac==502:
          print("\nTitle of the book :Bookhunter")
    elif ac==503:
          print("\nTitle of the book : The Turkish Gambit ")
    elif ac==504:
          print("\nTitle of the book : The Hound of the Baskervilles")
    elif ac==505:
          print("\nTitle of the book : Dracula ")
    elif ac==506:
          print("\nTitle of the book : The Mystery of Marie Roget")
    elif ac==507:
          print("\nTitle of the book : The Silence of the Lambs ")
    elif ac==508:
          print("\nTitle of the book : Last Days")
    elif ac==509:
          print("\nTitle of the book : The Shining ")
    elif ac==510:
          print("\nTitle of the book : Red Dragon")
    pg=int(input("No of pages in a book : "))
    for i in range(1,10):
         bd=input("Borrowing Date(DD/MM/YYYY): ")
         if "2020" in bd:
                   break
         elif "2021" in bd:
                   break
         else:
                   print("Enter a date from the current year or upcoming year(2020/2021)")
                   continue
    for i in range(1,10):
         rd=input("Returning Date(DD/MM/YYYY): ")
         if "2020" in rd:
                   break
         elif "2021" in rd:
                   break
         else:
                   print("Enter a date from the current year or upcoming year(2020/2021)")
                   continue
    d=int(input("No of days to be borrowed : "))
    amount=d*10
    am=print("Amount to be paid on the returning day is ",amount)
    print(" ***************** Fine should be paid for late submission of library book **************** ")
elif choice==2:
    print("\n*************************************************************\n")
    print("\n**************** You have read a book ****************\n ")
    print("\n*************************************************************\n")
    for i in range(1,10):
         n=input("Name : ")
         if n==name:
              break
         else:
              print("Enter the same name as above")
              continue
    for i in range(1,10):
         a=int(input("Age : "))
         if a==age:
              break
         else:
              print("Enter the same age as above")
              continue
    for i in range(0,10):
         gen=input("Gender(male/female) : ")
         if gen[0:6]=="female":
              break
         elif gen[0:4]=="male":
              break
         else:
              continue
    for i in range(1,10):
         d=input("Date(DD/MM/YYYY): ")
         if "2020" in d:
                   break
         elif "2021" in d:
                   break
         else:
                   print("Enter a date correctly(2020/2021)")
                   continue
    ad=input("Address  : ")
    for i in range(1,10):
         nl=input("In which language do you want the book(english/malayalam/tamil/telugu/kannadam/hindi) : ")
         if nl=="english" or nl=="malayalam" or nl=="tamil" or nl=="telugu" or nl=="kannadam" or nl=="hindi":
              break
         else:
              continue
    for i in range(1,25):
         ac=int(input("Account number of the book : "))
         if ac==101:
              print("Title of the book : Encyclopedia")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==102:
              print("Title of the book : General knowledge quiz book")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==103:
              print("Title of the book : Oxford Dictionary")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==201:
              print("Title of the book : Normal People")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==202:
              print("Title of the book : An Era of Darkness")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==203:
              print("Title of the book - Fear:Trump in the White House")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==204:
              print("Title of the book : The Farthest Field")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==205:
              print("Title of the book : Golden Child")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==206:
              print("Title of the book : Half The Night Is Gone")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==207:
              print("Title of the book : The Overstory")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==208:
              print("Title of the book : Interior Chinatown")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==209:
              print("Title of the book : King and the Dragonflies")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==210:
              print("Title of the book - The Dead Are Arising: The Life of Malcolm X")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==301:
              print("\nTitle of the book : Nimona")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==302:
              print("\nTitle of the book : Saga")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==303:
              print("\nTitle of the book : The Secret of the nagas")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==304:
              print("\nTitle of the book : Rat Queen")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==305:
              print("\nTitle of the book : The spire")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==306:
              print("\nTitle of the book : The Stonekeeper")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==307:
              print("\nTitle of the book : Seven to Eternity")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue 
         elif ac==308:
              print("\nTitle of the book : Sandman ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==309:
              print("\nTitle of the book : Bone")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==310:
              print("\nTitle of the book : Birthright")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==401:
              print("\nTitle of the book : Jurassic Park")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==402:
              print("\nTitle of the book : The Hunger Game")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==403:
              print("\nTitle of the book :The Da Vinci Code")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==404:
              print("\nTitle of the book : The Bourne Identity ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==405:
              print("\nTitle of the book : Divergent ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==406:
              print("\nTitle of the book : The Count of Monte Cristo")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==407:
              print("\nTitle of the book : The Hunt for Red October")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==408:
              print("\nTitle of the book : Harry Potter ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==409:
              print("\nTitle of the book : Rhythm of War ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==410:
              print("\nTitle of the book : Devoted")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==501:
              print("\nTitle of the book : The Last Dickens")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==502:
              print("\nTitle of the book :Bookhunter")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==503:
              print("\nTitle of the book : The Turkish Gambit ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==504:
              print("\nTitle of the book : The Hound of the Baskervilles")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==505:
              print("\nTitle of the book : Dracula ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==506:
              print("\nTitle of the book : The Mystery of Marie Roget")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==507:
              print("\nTitle of the book : The Silence of the Lambs ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==508:
              print("\nTitle of the book : Last Days")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==509:
              print("\nTitle of the book : The Shining ")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
         elif ac==510:
              print("\nTitle of the book : Red Dragon")
              choice=int(input("Press 1 to continue and 2 to exist"))
              if choice==2:
                    break
              else:
                    continue
elif choice==3:
    print("\n***************************************************************\n")
    print("\n**************** You returned the book ****************\n")
    print("\n***************************************************************\n")
    for i in range(1,10):
         n=input("Name : ")
         if n==name:
              break
         else:
              print("Enter the same name as above")
              continue
    for i in range(1,10):
         a=int(input("Age : "))
         if a==age:
              break
         else:
              print("Enter the same age as above")
              continue
    for i in range(0,10):
         gen=input("Gender(male/female) : ")
         if gen[0:6]=="female":
              break
         elif gen[0:4]=="male":
              break
         else:
              continue
    ad=input("Address : ")
    for i in range(0,10):
        phone=int(input("Phone number : "))
        ph=str(phone)
        if len(ph)!=10:
            p=print("*****Give the Correct Phone number*****")
            continue
        else:
            break
    ac=int(input("Account number of the book : "))
    if ac==101:
          print("Title of the book : Encyclopedia")
    elif ac==102:
          print("Title of the book : General knowledge quiz book")
    elif ac==103:
          print("Title of the book : Oxford Dictionary")
    elif ac==201:
          print("Title of the book : Normal People")
    elif ac==202:
          print("Title of the book : An Era of Darkness")
    elif ac==203:
          print("Title of the book - Fear:Trump in the White House")
    elif ac==204:
          print("Title of the book : The Farthest Field")
    elif ac==205:
          print("Title of the book : Golden Child")
    elif ac==206:
          print("Title of the book : Half The Night Is Gone")
    elif ac==207:
          print("Title of the book : The Overstory")
    elif ac==208:
          print("Title of the book : Interior Chinatown")
    elif ac==209:
          print("Title of the book : King and the Dragonflies")
    elif ac==210:
          print("Title of the book - The Dead Are Arising: The Life of Malcolm X")
    elif ac==301:
          print("\nTitle of the book : Nimona")
    elif ac==302:
          print("\nTitle of the book : Saga")
    elif ac==303:
          print("\nTitle of the book : The Secret of the nagas")
    elif ac==304:
          print("\nTitle of the book : Rat Queen")
    elif ac==305:
          print("\nTitle of the book : The spire")
    elif ac==306:
          print("\nTitle of the book : The Stonekeeper")
    elif ac==307:
          print("\nTitle of the book : Seven to Eternity")
    elif ac==308:
          print("\nTitle of the book : Sandman ")
    elif ac==309:
          print("\nTitle of the book : Bone")
    elif ac==310:
          print("\nTitle of the book : Birthright")
    elif ac==401:
          print("\nTitle of the book : Jurassic Park")
    elif ac==402:
          print("\nTitle of the book : The Hunger Game")
    elif ac==403:
          print("\nTitle of the book :The Da Vinci Code")
    elif ac==404:
          print("\nTitle of the book : The Bourne Identity ")
    elif ac==405:
          print("\nTitle of the book : Divergent ")
    elif ac==406:
          print("\nTitle of the book : The Count of Monte Cristo")
    elif ac==407:
          print("\nTitle of the book : The Hunt for Red October")
    elif ac==408:
          print("\nTitle of the book : Harry Potter ")
    elif ac==409:
          print("\nTitle of the book : Rhythm of War ")
    elif ac==410:
          print("\nTitle of the book : Devoted")
    elif ac==501:
          print("\nTitle of the book : The Last Dickens")
    elif ac==502:
          print("\nTitle of the book :Bookhunter")
    elif ac==503:
          print("\nTitle of the book : The Turkish Gambit ")
    elif ac==504:
          print("\nTitle of the book : The Hound of the Baskervilles")
    elif ac==505:
          print("\nTitle of the book : Dracula ")
    elif ac==506:
          print("\nTitle of the book : The Mystery of Marie Roget")
    elif ac==507:
          print("\nTitle of the book : The Silence of the Lambs ")
    elif ac==508:
          print("\nTitle of the book : Last Days")
    elif ac==509:
          print("\nTitle of the book : The Shining ")
    elif ac==510:
          print("\nTitle of the book : Red Dragon")
    
    for i in range(1,10):
         bda=input("Date in which the book is borrowed(DD/MM/YYYY): ")
         if "2020" in bda:
              break
         elif "2021" in bda:
              break
         else:
              print("Enter a date from the current year or upcoming year(2020/2021)")
              continue
    for i in range(1,10):
         dat=input("Date in which book should be returned(mentioned on the borrowing day)(DD/MM/YYYY): ")
         if "2020" in dat:
              break
         elif "2021" in dat:
              break
         else:
              print("Enter a date from the current year or upcoming year(2020/2021)")
              continue
    d2=int(input("Number of days you should have the book : "))
    for i in range(1,10):
         rda=input("Date in which the book is returned(DD/MM/YYYY): ")
         if "2020" in rda:
             break
         elif "2021" in rda:
             break
         else:
             print("Enter a date from the current year or upcoming year(2020/2021)")
             continue
    if dat!=rda:
        print(" ***************** Fine should be paid for late submission of library book **************** ")
        d3=int(input("No of extra days you had the book : "))
        d4=(d2*10)+(d3*15)
        am=print("Amount that should be paid today including the fine is RS.",d4)
    else:
        du=int(input("Number of days you had the book : "))
        amo=du*10
        am=print("Amount to be paid today is ",amo)
elif choice==4:
    print("\n******************************************************************\n")
    print("\n**************** You have read a newspaper ****************\n")
    print("\n******************************************************************\n")
    for i in range(1,10):
         n=input("Name : ")
         if n==name:
              break
         else:
              print("Enter the same name as above")
              continue
    for i in range(1,10):
         a=int(input("Age : "))
         if a==age:
              break
         else:
              print("Enter the same age as above")
              continue
    for i in range(0,10):
         gen=input("Gender(male/female) : ")
         if gen[0:6]=="female":
              break
         elif gen[0:4]=="male":
              break
         else:
              continue
    for i in range(1,10):
         dn=input("Date(DD/MM/YYYY): ")
         if "2020" in dn:
              break
         elif "2021" in dn:
              break
         else:
              print("Enter a date from the current year or upcoming year(2020/2021)")
              continue
    ad=input("Address : ")
    for i in range(1,10):
         nl=input("In which language do you want the newspaper(english/malayalam/tamil/telugu/kannadam/hindi) : ")
         if nl=="english" or nl=="malayalam" or nl=="tamil" or nl=="telugu" or nl=="kannadam" or nl=="hindi":
              break
         else:
              continue
    newsp=input("The newspaper that you recommend is ")
elif choice==5:
    print("\n*****************************************************************\n")
    print("\n**************** You have read a magazine ****************\n")
    print("\n*****************************************************************\n")
    for i in range(1,10):
         n=input("Name : ")
         if n==name:
              break
         else:
              print("Enter the same name as above")
              continue
    for i in range(1,10):
         a=int(input("Age : "))
         if a==age:
              break
         else:
              print("Enter the same age as above")
              continue
    for i in range(0,10):
         gen=input("Gender(male/female) : ")
         if gen[0:6]=="female":
              break
         elif gen[0:4]=="male":
              break
         else:
              continue
    for i in range(1,10):
         dm=input("Date(DD/MM/YYYY): ")
         if "2020" in dm:
              break
         elif "2021" in dm:
              break
         else:
              print("Enter a date from the current year or upcoming year(2020/2021)")
              continue
    ad=input("Address : ")
    for i in range(1,10):
         nl=input("In which language do you want the magazine(english/malayalam/tamil/telugu/kannadam/hindi) : ")
         if nl=="english" or nl=="malayalam" or nl=="tamil" or nl=="telugu" or nl=="kannadam" or nl=="hindi":
              break
         else:
              continue
    m=input("The magazines that you recommend : ")
li=input("Are you a member of the library association(yes/no) : ")
if li=="no" :
    no=input("Do you want to be a member of library association(yes/no) : ")
    if no=="yes" :
          print("\n******************************************************************************************************\n")
          print("\n**************** Answer these questions to become a member of the library association ****************\n")
          print("\n******************************************************************************************************\n")
          for i in range(1,10):
               n=input("Name : ")
               if n==name:
                    break
               else:
                    print("Enter the same name as above")
                    continue
          for i in range(1,10):
               Age=int(input("Age : "))
               if Age==age:
                    break
               else:
                    print("Enter the same age as above")
                    continue
          if Age>=5 and Age<=15:
               print("You belong to kids group")
          elif Age>15 and Age<=25:
               print("You belong to teenage group")
          elif Age>25 and Age<=50:
               print("You belong to adult group")
          elif Age>50 and Age<=100:
               print("You belong to oldage group")
          else:
               print("Enter your correct age")
          for i in range(0,10):
               gen=input("Gender(male/female) : ")
               if gen[0:6]=="female":
                    break
               elif gen[0:4]=="male":
                    break
               else:
                    continue
          for i in range(0,10):
              phone=int(input("Phone no : "))
              ph=str(phone)
              if len(ph)!=10:
                  p=print("*****Give the Correct Phone number*****")
                  continue
              else:
                  break
          n1=input("Is the whatsapp number same as phone num(yes/no)?  ")
          if n1=="yes":
               print("**Arrival of new books will be notified through whatsapp**")
          elif n1=="no":
              for i in range(0,10):
                  n2=int(input("Whatsapp number : "))
                  n=str(n2)
                  if len(n)!=10:
                      p=print("*****Give the Correct Whatsapp number*****")
                      continue
                  else:
                       print("**Arrival of new books will be notified through whatsapp**")
                       break
          else:
               print("Enter either (yes) or (no)")
          Ad=input("Enter your residental address : ")
          Addr=input("Enter your additional address : ")
          city=input("Enter your city : ")
          g=input("Are you a graduate(yes/no) : ")
          if g=="yes":
               p=input("Enter your profession : ")
          elif g=="no":
               s=input("Enter your school or college name : ")
               r=int(input("Enter your roll number : "))
          else:
               print("Enter either (yes) or (no)")
          Email=input("Enter your email id : ")
          Hobbies=input("Enter your special interest or hobbies : ")
          bk=input("Books to be recommended : ")
          choice=int(input('What will you be using the library for ?\n\t1.Reference\n\t2.Relaxation\n\t3.Knowledge gathering\n\t4.Job seeking\n\t5.All of the above\n\tEnter your choice'))
          if choice==1:
               print("\nI will you be using the library for Reference\n")
          elif choice==2:
               print("\nI will you be using the library for Relaxation\n")
          elif choice==3:
               print("\nI will you be using the library for Knowledge gathering\n")
          elif choice==4:
               print("\nI will you be using the library for Job seeking\n")
          elif choice==5:
               print("\nI will you be using the library for All of the above choices\n")
          choice=int(input('What section of the library would you like access to ?\n\t1.Magazines\n\t2.Fiction\n\t3.Non-fiction\n\t4.Research&Reference\n\t5.Education\n\t6.Poetry\n\t7.Others\n\tEnter your choice '))
          if choice==1:
               print("\nYou can access Magazines from the first group\n")
          elif choice==2:
               print("\nYou can access Fiction from the second group\n")
          elif choice==3:
               print("\nYou can access Non-fiction from the third group\n")
          elif choice==4:
               print("\nYou can access Reseaerch & Reference from the fourth group\n")
          elif choice==5:
               print("\nYou can access Education from the fifth group\n")
          elif choice==6:
               print("\nYou can access Poetry from the sixth group\n")
          elif choice==7:
               print("\nYou can access Other type of books from seventh to tenth group\n")
          print("************************************************************************\n")
          print("\n******** Now,you are also a member of the library association ********\n")
          print("************************************************************************\n")
    elif no=="no":
          print("\nAs a member you can have many benifits.\nYou can give it a try.\n")
    else:
          print("Enter either (yes) or (no)")
elif li=="yes":
     print("\n************************************************************************************************\n")
     print("\n********As a member of the library association,you have to answer some general question*********\n ")
     print("\n************************************************************************************************\n")
     for i in range(1,10):
          n=input("Name : ")
          if n==name:
               break
          else:
               print("Enter the same name as above")
               continue
     for i in range(1,10):
          Age=int(input("Age : "))
          if Age==age:
               break
          else:
               print("Enter the same age as above")
               continue
     if Age>=5 and Age<=15:
          print("You belong to kids group")
     elif Age>15 and Age<=25:
          print("You belong to teenage group")
     elif Age>25 and Age<=50:
          print("You belong to adult group")
     elif Age>50 and Age<=100:
          print("You belong to oldage group")
     else:
          print("Enter your correct age.")
     for i in range(0,10):
          gen=input("Gender(male/female) : ")
          if gen[0:6]=="female":
               break
          elif gen[0:4]=="male":
               break
          else:
               continue
     for i in range(0,10):
              phone=int(input("Phone no : "))
              ph=str(phone)
              if len(ph)!=10:
                  p=print("*****Give the Correct Phone number*****")
                  continue
              else:
                  break
     n1=input("Is the whatsapp number same as phone num(yes/no)?  ")
     if n1=="yes":
              print("**Arrival of new books will be notified through whatsapp**")
     elif n1=="no":
              for i in range(0,10):
                  n2=int(input("Whatsapp number : "))
                  n=str(n2)
                  if len(n)!=10:
                      p=print("*****Give the Correct Whatsapp number*****")
                      continue
                  else:
                       print("**Arrival of new books will be notified through whatsapp**")
                       break
     else:
              print("Enter either (yes) or (no)")
     Ad=input("Enter your residental address : ")
     Addr=input("Enter your additional address : ")
     city=input("Enter your city : ")
     g=input("Are you a graduate(yes/no) : ")
     if g=="yes":
          p=input("Enter your profession : ")
     elif g=="no":
          s=input("Enter your school or college name : ")
          r=int(input("Enter your roll number : "))
     else:
          print("Enter either (yes) or (no)")
     Email=input("Enter your email id : ")
     Hobbies=input("Enter your special interest or hobbies : ")
     choice=int(input('What will you be using the library for ?\n\t1.Reference\n\t2.Relaxation\n\t3.Knowledge gathering\n\t4.Job seeking\n\t5.All of the above\nEnter your choice: '))
     if choice==1:
          print("\nI will you be using the library for Reference\n")
     elif choice==2:
          print("\nI will you be using the library for Relaxation\n")
     elif choice==3:
          print("\nI will you be using the library for Knowledge gathering\n")
     elif choice==4:
          print("\nI will you be using the library for Job seeking\n")
     elif choice==5:
          print("\nI will you be using the library for All of the above choices\n")
     choice=int(input('What section of the library would you like access to ?\n\t1.Magazines\n\t2.Fiction\n\t3.Non-fiction\n\t4.Research&Reference\n\t5.Education\n\t6.Poetry\n\t7.Others\nEnter your choice:'))
     if choice==1:
          print("\nYou can access Magazines from the first group\n")
     elif choice==2:
          print("\nYou can access Fiction from the second group\n")
     elif choice==3:
          print("\nYou can access Non-fiction from the third group\n")
     elif choice==4:
          print("\nYou can access Reseaerch&Reference from the fourth group\n")
     elif choice==5:
          print("\nYou can access Education from the fifth group\n")
     elif choice==6:
          print("\nYou can access Poetry belongs from sixth group\n")
     elif choice==7:
          print("\nYou can access Other type of books from seventh to tenth group\n")
else:
     print("Enter either (yes) or (no)")
for i in range (1,10):
     aso=input("Are you a member of the library association(yes/no) : ")
     if aso=="yes":
          break
     elif aso=="no":
          break
     else:
          print("Enter either (yes) or (no)")
          continue
print("You have answered all our questions")
print("\nHere is your receipt : ")
print("\n*************************************************************************************************")
print("\n*************************************************************************************************")
print("*****************************************DJH Library*********************************************")
print("*************************************************************************************************")
print("\tEnter the librarian name : ",namel)
print("\tEnter your library code : ",pw)                  
print("\n****************************************Visitor Details******************************************")
print("\n\tEnter your name : ",name)
print("\tEnter your age : ",age)
print("\tEnter your gender(male/female) : ",gen)
print("\tDate(DD/MM/YYYY) : ",date)
print("\tEnter your address : ",add)
print("\tPhone number : ",phone)
print("\tAre you a member of the library association(yes/no) : ",aso)
print("\n********************You can visit the Library at 9:00 am to 10:00 pm ****************************")
print("*************************Library will be closed on all saturdays*********************************")
print("*********************************Thank You,Visit Again Later*************************************")
print("\n*************************************************************************************************")
print("*************************************************************************************************")
