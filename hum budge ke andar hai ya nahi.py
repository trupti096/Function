# Iss program mein hum students ki ginti aur ek student ke kharche se hisaab se 
# pure NavGurukul ka ek mahine ka kharcha nikalenge
# input ka use kar ke do values ka input lo:
# Number of students
# Ek student ka kharcha
# Iss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya 
# usse kam hai toh print karein "Hum budget ke andar hain" nahi toh print karo ki
#  hum budget ke bahar hain.


#print
def total_kharcha(number_of_students,ek_student_ka_kharcha):
    if ek_student_ka_kharcha<50000:
        print("hum budget ke andar hai")
    else:
        print("hum budget ke bahar hai")
total_kharcha(100,10000)

#return
def total_kharcha(number_of_students,ek_student_ka_kharcha):
    if ek_student_ka_kharcha<50000:
        return "hum budget ke andar hai"
    else:
        return "hum budget ke bahar hai"
print(total_kharcha(100,10000))
