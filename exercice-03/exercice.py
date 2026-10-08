temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

moyenne = sum(temperatures) / len(temperatures)
resultat = round(moyenne, 2)
minimum = min(temperatures)
maximum = max(temperatures)
print("La température moyenne est :", resultat)
print("Min :", minimum)
print("Max :", maximum)

jours = []
for temperature in temperatures:
    if temperature > 15:
        jours.append(temperature)

print("Jours > 15°C :", len(jours))

Fahrenheit = [temp * 9/5 + 32 for temp in temperatures]
print("Fahrenheit :", Fahrenheit)

for i, temp in enumerate(temperatures):
    print(f"Jour {i+1} : {temp}°C")


