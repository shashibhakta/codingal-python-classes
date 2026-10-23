tempertaure = int(input("Enter today's tempertaure in Celsius: "))
if tempertaure < 20:
    outfit = "jacket"
    print("It is cold today. ")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It's a warm day.")
print("Wear a", outfit)
is_raining = input("Is it raining today? (Yes/No):")
if is_raining =="yes ":
    print("Bring an umbrella!")
wind_speed = int(input("Enter the wind speed in km/h : "))
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over your" , outfit)
else:
    needs_windbreaker ="no"
    print("It is calm today.")
    print("No windbreaker needed over you", outfit)
has_puddles = input("Are there puddles on the goruond? (yes/no):")
if has_puddles =="yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)
print("")
print("Weather check completed!")
print("====WEATHER OUTFIT PICKER ====")
print("Tempertaure:", tempertaure)
print("Outfit Chosen:", outfit)
print("Rainging:", is_raining)
print("Windbreaking Needed:", needs_windbreaker)
print("Shoes Chosen:", shoes)
print("====================================")

















