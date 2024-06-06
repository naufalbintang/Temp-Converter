temp_input = float(input("Masukkan angka: "))
unit_input = str(input("Masukkan satuan awal: "))
unit_output = str(input("Masukkan satuan akhir: "))

conversion = {
    "c": {
        "f": lambda x: (x * 9 / 5) + 32,
        "r": lambda x: x * 4/ 5,
        "k": lambda x: x + 273.15
    },
    "f": {
        "c": lambda x: (x - 32) * 5 / 9,
        "r": lambda x: (x - 32) * 4 / 9,
        "k": lambda x: (x - 32) * 5 / 9 + 273.15
    },
    "r": {
        "f": lambda x: x * 9 / 4 + 32,
        "c": lambda x: x * 5 / 4,
        "k": lambda x: x * 5 / 4 + 273.15
    },
    "k": {
        "f": lambda x: (x - 273.15) * 4 / 5,
        "c": lambda x: x - 273.15,
        "r": lambda x: (x - 273.15) * 4 / 5
    }
}

def formula(temp_input, unit_input, unit_output):
    return conversion[unit_input.lower()][unit_output.lower()](temp_input)

print(f"Hasil konversi: {formula(temp_input, unit_input, unit_output):.2f} {unit_output}")


    
