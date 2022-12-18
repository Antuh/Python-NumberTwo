# Получение данных от пользователя
def getData():
    while True:
        print("Введите 'y' для добавления данных, и 'n' для завершения")
        check: str = input()
        if check in ["y", "Y", "yes", "Yes", "YES"]:
            while True:
                try:
                    print('Введите номер номер, ФИО и возраст:')
                    id_user, surname, name, patronymic, year = map(str, input().split())
                    print(f"Вы ввели: {id_user} {surname} {name} {patronymic} {year}")
                    assert year.isdigit(), id_user.isdigit()
                except ValueError:
                    print('Не правильно внесены данные!')
                except:
                    print('Ошибка!')
                # Запись данных в файл
                try:
                    my_file = open("DataPeople.txt", "a", encoding='utf8')
                    my_file.write(f"{id_user} {surname} {name} {patronymic} {year}\n")
                    print("Данные были записаны в файл")
                    my_file.close()
                except PermissionError:
                    print('У вас нет доступа к данному файлу!')
                except:
                    print('Ошибка!')
        else:
            exit()


if __name__ == '__main__':
    getData()