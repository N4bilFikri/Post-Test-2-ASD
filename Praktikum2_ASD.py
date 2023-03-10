# Menggunakan liniar_search serta arr & x sebagai parameter
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# List terdapat 5 data 
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Output ke 1
print(f"1. {var[0]} di Index {linear_search(var, 'Arsel')}, {var[1]} di Index {linear_search(var, 'Avivah')}, {var[2]} di Index {linear_search(var, 'Daiva')}")

# Output ke 2
wahyu_index = linear_search(var[3], "Wahyu")
print(f"2. Wahyu di Index 3 pada kolom {wahyu_index}")

# Output ke 3
wibi_index = linear_search(var[3], "Wibi")
print(f"3. Wibi di Index 3 pada kolom {wibi_index}")
