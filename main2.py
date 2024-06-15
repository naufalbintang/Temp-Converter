import os

while True:
    os.system('cls')
    unit = ["celcius", "fahrenheit", "kelvin", "reaumur"]
    print(f"\n1. {unit[0]}") # celcius
    print(f"2. {unit[1]}") # fahrenheit
    print(f"3. {unit[2]}") # kelvin 
    print(f"4. {unit[3]}") # reaumur

    temp_input = float(input("Masukkan angka: "))
    unit_input = int(input("Masukkan satuan awal: "))
    unit_output = int(input("Masukkan satuan akhir: "))

    conversion = {
        # celcius to
        (1, 2): (temp_input * 9 / 5) + 32, #fahrenheit
        (1, 3): temp_input + 273.15, #kelvin
        (1, 4): temp_input * 4 / 5, #reaumur
        # fahrenheit to 
        (2, 1): (temp_input - 32) * 5 / 9, #celcius
        (2, 3): (temp_input - 32) * 5 / 9, #kelvin
        (2, 4): (temp_input - 32) * 4 / 9, #reaumur
        # kelvin to
        (3, 1): temp_input - 273.15, #celcius
        (3, 2): (temp_input - 273.15) * 4 / 5, #fahrenheit
        (3, 4): (temp_input - 273.15) * 4 / 5, #reaumur
        # reaumur to
       (4, 1): temp_input * 5 / 4, #celcius
       (4, 2): temp_input * 9 / 4 + 32, #fahrenheit
       (4, 3): temp_input * 5 / 4 + 273.15, #kelvin
    }
 
    if unit_input == unit_output:
       pass
    else:
      print(f"{temp_input} {unit[unit_input-1]} = {conversion[(unit_input, unit_output)]:.2f} {unit[unit_output-1]}\n")
    
    response = str(input("Apakah ingin keluar? (y/n): "))
    if response.lower() == "y":
       break 