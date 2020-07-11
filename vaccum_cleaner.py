f = open("bc.txt", "r")
list=f.readlines()
f.close()
pro=[]
pro.append("******WELCOME TO RD VACCUM CLEANER******\n\n")
for a in list:
      if ',' in a:
        location,status=a.split(",")
        location=location.upper()
        status=status.upper().strip()
        
        if location == "A" and status=="DIRTY":
          pro.append("MOVING TO ROOM A....\nROOM A FOUND DIRTY...\nSUCKING....\nROOM A CLEANED...\n")
        elif location=="A" and status=="CLEAN":
          pro.append("ROOM A ALREADY CLEAN...")
        if location=="B" and status=="DIRTY":
          pro.append("MOVING TO ROOM B...\nROOM B FOUND DIRTY...\nSUCKING....\nROOM B CLEANED...\n")
        elif location=="B" and status=="CLEAN":
          pro.append("ROOM B ALREADY CLEAN...\n")

pro.append("\n\n******CLEANING COMPLETED*****")
f1 = open("ac.txt","w")    
f1.writelines(["%s\n" % item  for item in pro])   
f1.close()
 