import os

#Путь к каталогу с файлами
catalog_promstroy = os.walk(r'W:\Общие документы\ПРАВАЯ СЛУЖБА\Охрана труда\Карты СОУТ\АО Промстрой')

# Создание списка файлов содержащихся в каталоге
folder_promstroy = []
for i in catalog_promstroy:
    folder_promstroy.append(i)

# Создание словаря ключевые слова + путь до файла
baza_promstroy = {}
for address, dirs, files in folder_promstroy:
    for file in files:
        name = (file.split('.')[0])  #отделение расширения файла (.pdf) необходимо для формирования ключа
        baza_promstroy[name] = (address+'\\'+file) #Сборка полного пути к каждому файлу адресс + имя файла с расширением

# создание списка ключей для поледующей передачи в втоподбор
word_auto_promstroy = []
for address, dirs, files in folder_promstroy:
    for file in files:
        word = (file.split('.')[0]) #отделение расширения файла (.pdf) необходимо для формирования ключа
        word_auto_promstroy.append(word)


catalog_bshsu = os.walk(r'W:\Общие документы\ПРАВАЯ СЛУЖБА\Охрана труда\Карты СОУТ\ООО БШСУ')

folder_bshsu = []
for i in catalog_bshsu:
    folder_bshsu.append(i)

baza_bshsu = {}
for address, dirs, files in folder_bshsu:
    for file in files:
        name = (file.split('.')[0])
        baza_bshsu[name] = (address+'\\'+file)

word_auto_bshsu = []
for address, dirs, files in folder_bshsu:
    for file in files:
        word = (file.split('.')[0])
        word_auto_bshsu.append(word)


catalog_nova = os.walk(r"C:\пиииитоооон а что у тебя тут за заварушка\База\Файлы")

folder_nova = []
for i in catalog_nova:
    folder_nova.append(i)

baza_nova = {}
for address, dirs, files in folder_nova:
    for file in files:
        name = (file.split('.')[0])
        baza_nova[name] = (address+'\\'+file)

word_auto_nova = []
for address, dirs, files in folder_nova:
    for file in files:
        word = (file.split('.')[0])
        word_auto_nova.append(word)
print(word_auto_nova)


catalog_tozzi = os.walk(r'W:\Общие документы\ПРАВАЯ СЛУЖБА\Охрана труда\Карты СОУТ\ООО Тоцци Восток')

folder_tozzi = []
for i in catalog_tozzi:
    folder_tozzi.append(i)

baza_tozzi = {}
for address, dirs, files in folder_tozzi:
    for file in files:
        name = (file.split('.')[0])
        baza_tozzi[name] = (address+'\\'+file)

word_auto_tozzi = []
for address, dirs, files in folder_tozzi:
    for file in files:
        word = (file.split('.')[0])
        word_auto_tozzi.append(word)


catalog_uralkal = os.walk(r'W:\Общие документы\ПРАВАЯ СЛУЖБА\Охрана труда\Карты СОУТ\ООО Урал Калий Ремонт')

folder_uralkal = []
for i in catalog_uralkal:
    folder_uralkal.append(i)

baza_uralkal = {}
for address, dirs, files in folder_uralkal:
    for file in files:
        name = (file.split('.')[0])
        baza_uralkal[name] = (address+'\\'+file)

word_auto_uralkal = []
for address, dirs, files in folder_uralkal:
    for file in files:
        word = (file.split('.')[0])
        word_auto_uralkal.append(word)


catalog_instrukcii = os.walk(r'W:\Общие документы\ПРАВАЯ СЛУЖБА\Охрана труда\Инструкции по охране труда\Инструкции')

folder_instrukcii = []
for i in catalog_instrukcii:
    folder_instrukcii.append(i)

baza_instrukcii = {}
for address, dirs, files in folder_instrukcii:
    for file in files:
        name = (file.split('.')[0])
        baza_instrukcii[name] = (address+'\\'+file)

word_auto_instrukcii = []
for address, dirs, files in folder_instrukcii:
    for file in files:
        word = (file.split('.')[0])
        word_auto_instrukcii.append(word)
