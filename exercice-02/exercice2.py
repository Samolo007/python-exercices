

temperature = int(input("Entrez la température : "))

if temperature < 0:
    print(f"{temperature}°C: gel")

elif temperature < 15:
    print(f"{temperature}°C: froid")

elif temperature < 25:
    print(f"{temperature}°C: doux")

else:
    print(f"{temperature}°C: chaud")

année = int(input("Entrez une année : "))

if année % 4 == 0 and (année % 100 != 0) or (année % 400 == 0):
    print(f"{année} : bissextile.")

else:
    print(f"{année} : non bissextile.")