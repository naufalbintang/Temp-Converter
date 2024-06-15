import os

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
    
def hitung(angka):
    '''fungsi untuk menghitung nilai konversi'''
    hasil = conversion[unit_input.lower()][unit_output.lower()](angka)
    return hasil

def display_hasil(hasil):
    print(f'{temp_input} {unit_input} = {hasil:.2f} {unit_output}')


while True:
    '''main program'''
    os.system('cls')
    print(f'{'KONVERTER SUHU':^37}')
    print(f'{'-'*37}')
    temp_input = float(input("\nMasukkan angka: "))
    unit_input = str(input("Masukkan satuan awal (c, f, r, k): "))
    unit_output = str(input("Masukkan satuan akhir (c, f, r, k): "))
    if unit_input == unit_output:
        print(f'{temp_input:.2f} {unit_input} = {temp_input:.2f} {unit_output}')
    else:
        HASIL = hitung(temp_input)
        display_hasil(HASIL)

    '''break'''
    is_done = input('Apakah sudah selesai (y/n)? ')
    if is_done == 'y':
        break
    else:
        None
    

    
