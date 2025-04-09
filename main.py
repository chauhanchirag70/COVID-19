import csv
import sys
import patient

patient.patientinfo()
#second menu started
while(1):
     print('''
----------------------------------------------------------------------------------------------------
|                                       CHOOSE YOUR OPTION                                         |
|                                       1. COVID - 19 TEST                                         |
|                                       2. BEDS AVAILABILITY                                       |
|                                       3. OXYGEN AVAILABILITY                                     |
|                                       4. EXIT                                                    |
----------------------------------------------------------------------------------------------------
''')
     ch=int(input("Enter Your Choice \t:\t"))
     if ch==1:           #covid test
          print('''
----------------------------------------------------------------------------------------------------
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     COVID - 19 TEST     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
----------------------------------------------------------------------------------------------------
''')
          print("CHOOSE THE SYMPTOMS IN RESPECT OF YES / NO WHICH YOU HAVE ")
          count=0
          s1=input("1. FEVER(Y/N)\t\t\t\t:\t")
          s2=input("2. DRY COUGH(Y/N)\t\t\t:\t")
          s3=input("3. TIREDNESS(Y/N)\t\t\t:\t")
          s4=input("4. ACHES AND PAINS(Y/N)\t\t\t:\t")
          s5=input("5. SORE THROAT(Y/N)\t\t\t:\t")
          s6=input("6. DIARHOEA(Y/N)\t\t\t:\t")
          s7=input("7. HEADACHE(Y/N)\t\t\t:\t")
          s8=input("8. LOSS OF TASTE AND SMELL(Y/N)\t\t:\t")
          s9=input("9. A RASH ON SKIN(Y/N)\t\t\t:\t")
          s10=input("10. DIFFICULTY IN BREATHING(Y/N)\t:\t")
          s11=input("11. CHEST PAIN OR PRESSURE(Y/N)\t\t:\t")
          s12=input("12. LOSS OF SPEECH OR MOVEMENT(Y/N)\t:\t")

          if s1=="Y" or s1=="y" :
              count+=1

          if s2=="Y" or s2=="y":
              count+=1

          if s3=="Y" or s3=="y":
              count+=1

          if s4=="Y" or s4=="y":
              count+=1

          if s5=="Y" or s5=="y":
              count+=1

          if s6=="Y" or s6=="y":
              count+=1

          if s7=="Y" or s7=="y" :
              count+=1

          if s8=="Y" or s8=="y":
              count+=1

          if s9=="Y" or s9=="y":
              count+=1

          if s10=="Y" or s10=="y":
              count+=1

          if s11=="Y" or s11=="y":
              count+=1

          if s12=="Y" or s12=="y":
              count+=1
          print("--------------------------------------------------------")
          print("\n\nTotal no. of symptoms counted positive\t:\t",count)
          print("--------------------------------------------------------")
          
          if count>=10:
              print("\nYou are highly infected with the following symptoms which you have entered as Yes, Consult a doctor and take proper treatment according to your symptoms.")
          elif count>=8:
              print("\nYou are mildly infected with the following symptoms which you have entered as Yes, Consult a doctor and take proper treatment according to your symptoms.")
          elif count>=5:
              print("\nFound Positive according to the manual test. Take precautions and maintain distance from others.")
          else :
              print("\nCongratulations!! You found negative")

     elif ch==2:              #checking of beds availability
          print('''
----------------------------------------------------------------------------------------------------
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     BEDS AVAILABILITY   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
----------------------------------------------------------------------------------------------------
''')
          with open('oxygen.csv', 'r') as file:
               my_reader = csv.reader(file, delimiter=',')
               '''for row in my_reader:
                    print()'''
               while(1):
                    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
----------------- PLEASE SELECT THE APPROPRIATE OPTION TO SEARCH THE BEDS AVAILABILITY -------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                       1. ZONE WISE
                                       2. CITY WISE
                                       3. STATE WISE
                                       4. EXIT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                    N=int(input("Choose your option (1-4)\t:\t"))
                    if N==1 :
                         print('''
                                   ----------------------
                                      ZONES AVAILABLE
                                   ----------------------
                                           EAST
                                           WEST
                                           NORTH
                                           SOUTH
                                           CENTRAL
                                           NORTH EAST
                                           NORTH WEST
                                           SOUTH EAST
                                           SOUTH WEST
                                   ----------------------
''')
                         
                         zone = input("Enter Zone\t:\t")
                         csv_file = csv.reader(open('oxygen.csv', "r"), delimiter=",")
                         #loop through the csv list
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         print("\t\t",zone.upper(),"ZONE HOSPITAL NAME AND THEIR BEDS AVAILABLE")
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         for row in csv_file:
                              #if current rows 2nd value is equal to input, print that row
                              if zone.upper() == row[5]:
                                   print("Hospital Name \t\t:\t",row[1])
                                   print("Location \t\t:\t",row[4])
                                   print("Beds Availability \t:\t",row[7])
                                   print("Contact No. \t\t:\t",row[8])
                                   print("----------------------------------------------------------------------------------------------------")
                         break
                    elif N==2:
                         print('''
                                      CITY AVAILABLE
                                   ------------------------
                                         NEW DELHI
                                         NOIDA
                                         GURUGRAM
                                   ------------------------''')
                         
                         City = input("Enter City\t:\t")
                         csv_file = csv.reader(open('oxygen.csv', "r"), delimiter=",")
                         #loop through the csv list
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         print("\t\t",City.upper(),"CITY HOSPITAL NAME AND THEIR BEDS AVAILABLE")
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         for row in csv_file:
                              #if current rows 2nd value is equal to input, print that row
                              if City.upper() == row[4]:
                                   print("Hospital Name \t\t:\t",row[1])
                                   print("Beds Availability \t:\t",row[7])
                                   print("Contact No. \t\t:\t",row[8])
                                   print("----------------------------------------------------------------------------------------------------")
                         break
                    elif N==3:
                         print('''
                                      STATE AVAILABLE
                                   ------------------------
                                         DELHI
                                         HARYANA
                                         UP
                                   ------------------------''')
                         
                         state = input("Enter State\t:\t")
                         csv_file = csv.reader(open('oxygen.csv', "r"), delimiter=",")
                         #loop through the csv list
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         print("\t\t",state.upper(),"STATE HOSPITAL NAME AND THEIR BEDS AVAILABLE")
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         for row in csv_file:
                              #if current rows 2nd value is equal to input, print that row
                              if state.upper() == row[3]:
                                   print("Hospital Name \t\t:\t",row[1])
                                   print("Beds Availability \t:\t",row[7])
                                   print("Contact No. \t\t:\t",row[8])
                                   print("----------------------------------------------------------------------------------------------------")     
                         break
                    
                    elif ch==4:              #exit from menu
                         break
                    else:
                         print("You have entered an invalid choice. Please enter a valid choice (1-4)")
                         
     elif ch==3:              #checking of oxygen availability
          print('''
----------------------------------------------------------------------------------------------------
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     OXYGEN AVAILABILITY  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
----------------------------------------------------------------------------------------------------
''')
          with open('oxygen.csv', 'r') as file:
               my_reader = csv.reader(file, delimiter=',')
               '''for row in my_reader:
                    print(row)'''
               while(1):
                    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------- PLEASE SELECT THE APPROPRIATE OPTION TO SEARCH THE OXYGEN AVAILABILITY -------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                       1. ZONE WISE
                                       2. CITY WISE
                                       3. STATE WISE
                                       4. EXIT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                    N=int(input("Choose your option (1-4)\t:\t"))
                    if N==1 :
                         print('''
                                   ----------------------
                                      ZONES AVAILABLE
                                   ----------------------
                                           EAST
                                           WEST
                                           NORTH
                                           SOUTH
                                           CENTRAL
                                           NORTH EAST
                                           NORTH WEST
                                           SOUTH EAST
                                           SOUTH WEST
                                   ----------------------
''')
                         
                         zone = input("Enter Zone\t:\t")
                         csv_file = csv.reader(open('oxygen.csv', "r"), delimiter=",")
                         #loop through the csv list
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         print("\t\t",zone.upper(),"ZONE HOSPITAL NAME AND THEIR OXYGEN AVAILABLE")
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         for row in csv_file:
                              #if current rows 2nd value is equal to input, print that row
                              if zone.upper() == row[5]:
                                   print("Hospital Name \t\t:\t",row[1])
                                   print("Location \t\t:\t",row[4])
                                   print("Oxygen Availability \t:\t",row[6])
                                   print("Contact No. \t\t:\t",row[8])
                                   print("----------------------------------------------------------------------------------------------------")
                         break
                    elif N==2:
                         print('''
                                      CITY AVAILABLE
                                   ------------------------
                                         NEW DELHI
                                         NOIDA
                                         GURUGRAM
                                   ------------------------''')
                         
                         City = input("Enter City\t:\t")
                         csv_file = csv.reader(open('oxygen.csv', "r"), delimiter=",")
                         #loop through the csv list
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         print("\t\t",City.upper(),"CITY HOSPITAL NAME AND THEIR OXYGEN AVAILABLE")
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         for row in csv_file:
                              #if current rows 2nd value is equal to input, print that row
                              if City.upper() == row[4]:
                                   print("Hospital Name \t\t:\t",row[1])
                                   print("Oxygen  Availability \t:\t",row[6])
                                   print("Contact No. \t\t:\t",row[8])
                                   print("----------------------------------------------------------------------------------------------------")
                         break
                    elif N==3:
                         print('''
                                      STATE AVAILABLE
                                   ------------------------
                                         DELHI
                                         HARYANA
                                         UP
                                   ------------------------''')
                         
                         state = input("Enter State\t:\t")
                         csv_file = csv.reader(open('oxygen.csv', "r"), delimiter=",")
                         #loop through the csv list
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         print("\t\t",state.upper(),"STATE HOSPITAL NAME AND THEIR OXYGEN AVAILABLE")
                         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                         for row in csv_file:
                              #if current rows 2nd value is equal to input, print that row
                              if state.upper() == row[3]:
                                   print("Hospital Name \t\t:\t",row[1])
                                   print("Oxygen  Availability \t:\t",row[6])
                                   print("Contact No. \t\t:\t",row[8])
                                   print("----------------------------------------------------------------------------------------------------")
     
                         break
                    elif ch==4:              #exit from menu
                         break
                    else:
                         print("You have entered an invalid choice. Please enter a valid choice (1-4)")
               
     elif ch==4:              #exit from software
          exit()
     else:
          print("You have entered an invalid choice. Please enter a valid choice between (1-4)")
