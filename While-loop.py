#While loop
#ASCII Value
counter = 65
while counter < 91:
     if counter < 70:  #skipping a condition using continue
       counter+=1
       continue
     print(str(counter) , "=" , chr(counter))
     counter+=1
     if counter > 85 :
         break   #coming out of a loop after a particular condition

