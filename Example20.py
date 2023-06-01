char_list = []
string = input("Введите слово: ")
for c in string:
    char_list.append(c)
##letters1 = {'A','E','I','O','U','L','N','S','T','R','А','В','Е','И','Н','О','Р','С','Т'}
##letters2 = {'D','G','Д','К','Л','М','П','У'}
##letters3 = {'B','C','M','P','Б','Г','Ё','Ь','Я'}
##letters4 = {'F','H','V','W','Y','Й','Ы'}
##letters5 = {'K','Ж','З','Х','Ц','Ч'}
##letters8 = {'J','X','Ш','Э','Ю'}
##letters10 = {'Q','Z','Ф','Щ','Ъ'}
d = {int(1):'A',int(1):'E',int(1):'I',int(1):'O',int(1):'U',int(1):'L',int(1):'N',int(1):'S',int(1):'T',int(1):'R',
     int(1):'А',int(1):'В',int(1):'Е',int(1):'И',int(1):'Н',int(1):'О',int(1):'Р',int(1):'С',int(1):'Т',
     int(2):'D',int(2):'G',int(2):'Д',int(2):'К',int(2):'Л',int(2):'М',int(2):'П',int(2):'У',
     int(3):'B',int(3):'C',int(3):'M',int(3):'P',int(3):'Б',int(3):'Г',int(3):'Ё',int(3):'Ь',int(3):'Я',
     int(4):'F',int(4):'H',int(4):'V',int(4):'W',int(4):'Y',int(4):'Й',int(4):'Ы',
     int(5):'K',int(5):'Ж',int(5):'З',int(5):'Х',int(5):'Ц',int(5):'Ч',
     int(8):'J',int(8):'X',int(8):'Ш',int(8):'Э',int(8):'Ю',
     int(10):'Q',int(10):'Z',int(10):'Ф',int(10):'Щ',int(10):'Ъ'}
sum=0
i=0
while i<len(char_list):
    sum+=d.get(char_list[i],0)
    i+=1

print(sum)