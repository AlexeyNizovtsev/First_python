name= input("Введите имя студента: ").strip()
surname= input("Введите фамилию студента: ").strip()
year= input("Введите год рождения студента: ").strip()
print(name+'_'+ surname+'_'+ year)
buff=name
name=surname
surname=buff
print(name+'_'+ surname+'_'+ str(int(year)+60))
