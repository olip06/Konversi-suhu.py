print("/n Program Konversi Suhu/n")

fahrenheit = float(input("masukkan suhu dalam fahrenheit:"))

#fahrenheit ke kelvin
celcius = (5/9)*(fahrenheit-32)
kelvin = celcius + 273
print("suhu dari fahrenheit ke kelvin", kelvin, "kelvin")

#kelvin ke fahrenheit
kelvin = float(input("masukkan nilai suhu dalam kelvin:"))
celcius = kelvin-273
fahrenheit = ((9/5)*celcius) + 32
print("suhu dari kelvin ke fahrenheit:", fahrenheit, "fahrenheit")