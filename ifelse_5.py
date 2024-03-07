nilai = int(input("nilai : "))

print("Nilai anda :", nilai, '\n')

if nilai <= 100:
    print('A')
elif nilai <= 85:
    print('B')
elif nilai <= 74:
    print('C')
elif nilai <= 60:
    print('D')
elif nilai <= 45:
    print('E')
else :
    print('nilai melebihi 100')