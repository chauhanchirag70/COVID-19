
import csv

def patientinfo():
     print('''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
|                                          COVID - 19                                              |
|                                      24X7 HELPLINE SYSTEM                                        |
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
''')
     #patient information entries
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     PATIENT ADMISSION FORM   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        
     with open('data.csv', 'a', encoding='UTF8') as f:
           
          pname=input("Patient Name \t\t\t:\t ")
          age=int(input("Age \t\t\t\t:\t "))
          dob=input("Date of birth \t\t\t:\t ")
          while(1):
               print('''GENDER
          M - MALE 
          F - FEMALE
          ''')
               g=input("Choose Gender (M/F) \t\t:\t")
               if g=="M" or g=="m" or g=="F" or g=="f":
                   gender=g.upper()
                   break
               else :
                    print("You have entered an invalid gender. Please enter a valid gender.")

          while(1):
               print('''Blood Groups
          A+
          B+
          A-
          B-
          AB+
          AB-
          O+
          O-''')
               bld=input("Choose patient's Blood group \t:\t")
               if bld=="A+" or bld=="a+" or bld=="B+" or bld=="b+" or bld=="A-" or bld=="a-" or bld=="B-" or bld=="b-" or bld=="AB+" or bld=="ab+" or bld=="Ab+" or bld=="aB+" or bld=="AB-" or bld=="ab-"or bld=="Ab-" or bld=="aB-" or bld=="O+" or bld=="o+" or bld=="O-" or bld=="o-":
                    bld=bld.upper()
                    break
               else :
                    print("You have entered an invalid blood group. Please enter a valid Blood Group.")
                         
                    
          addr=input("Address \t\t\t:\t ")
          pin=int(input("Pin code \t\t\t:\t "))
          city=input("City \t\t\t\t:\t ")
          state=input("State \t\t\t\t:\t ")
          cont=int(input("Patient Contact No. \t\t:\t "))
          atname=input("Attendant Name \t\t\t:\t ")
          atcont=int(input("Attenadent Contact No. \t\t:\t "))
          now=input("Today's Date \t\t\t:\t")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

          print("\n\n\n")
          print("....................................................................................................")
          print("                                 CONFIRM INFORMATION")
          print("....................................................................................................")
          print("---------------------------------   Patient Details      -------------------------------------------")
          print("Patient Name \t\t  = ",pname.upper(),"\t\tAge = ",age)
          print("Date of Birth(DD/MM/YYYY) = ",dob,"\tGender = ",gender.upper())
          print("Patient Blood Group \t  = ",bld)
          print("\n\n---------------------------------- Additional Information -------------------------------------------")
          print("Residential Address \t  = ",addr.upper())
          print("State       \t\t  = ",state.upper(),"\t\tCity = ",city.upper(),"\t\tPin Code = ",pin)
          print("Contact No.      \t  = ",cont)
          print("\n\n----------------------------------   Attendant Details    -------------------------------------------")
          print("Attendant Name \t\t  = ",atname.upper())
          print("Attendant Contact \t  = ",atcont)
          print("\n\nDate =",now)
          print("....................................................................................................")

          input("Press Enter to record the following given information!!!!!!!")

          writer = csv.writer(f)
          row=[pname.upper(),age,dob,gender.upper(),bld.upper(),addr.upper(),city.upper(),state.upper(),pin,cont,atname.upper(),atcont,now]
          writer.writerow(row)
     #patient information submission


          
