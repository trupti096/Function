# Ek function define kijiye jo ki drivers ki speed check karega. 
# Aur ye function speed naam ka ek parameter lega.

# 1 Agar speed 70 se kam hai to ye “ok” print karega.

# 2 Agar driver ki speed 70 se jyaada hai to function use har 5 km ke liye 1 point dega (ye 70 ko count nahi karega).example ke liye agar speed 80 hai to print karega “points:2” .

# 3 Agar driver ko 12 points se jyaada points milte hai to , function “License suspended” print karega.


def speed1(speed):
	speed2=speed-70
	point=speed2//5
	if speed<=70:
		print('ok')
	elif point>12:
		print('licence suspended')
	elif speed>70:
		print('point',point)
speed=int(input('enter:'))
speed1(speed)
    