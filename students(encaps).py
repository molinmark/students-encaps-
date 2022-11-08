import random
class student:
    def __init__(self, name, health, skills, progress, happy, intellect):
        self.__name = name
        self.__health = health
        self.__skills = skills
        self.__progress = progress
        self.__happy = happy
        self.__intellect = intellect
    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, val):
        if val < 0 or val > 10:
            print('Ошибка')
        else:
            self.__health = val

    @property
    def skills(self):
        return self.__skills
    @skills.setter
    def skills(self, val):
        if val < 0 or val > 10:
            print('Ошибка')
        else:
            self.__skills = val

    @property
    def progress(self):
        return self.__progress
    @progress.setter
    def progress(self, val):
        if val < 0 or val > 10:
            print('Ошибка')
        else:
            self.__progress = val

    @property
    def happy(self):
        return self.__happy
    @happy.setter
    def happy(self, val):
        if val < 0 or val > 10:
            print('Ошибка')
        else:
            self.__happy = val

    @property
    def intellect(self):
        return self.__intellect
    @intellect.setter
    def intellect(self, val):
        if val < 0 or val > 10:
            print('Ошибка')
        else:
            self.__intellect = val

    def study(self):
        self.__health -= 1
        self.__skills += 1
        self.__progress += 1
        self.__happy -= 1
        self.__intellect += 1
        print(self.__name, 'Cтудент активно учился!')
    def relax(self):
        self.__health += 1
        self.__skills -= 1
        self.__progress -= 1
        self.__intellect -= 1
        print(self.__name, 'Cтудент активно отдыхал!')
    def fun(self):
        self.__health -= 1
        self.__skills -= 1
        self.__progress -= 1
        self.__happy += 1
        self.__intellect -= 1
        print(self.__name, 'Cтудент активно веселился!')
    def returning_conditions(self,condition):
        if condition == 1:
            return 'Любит учиться'
        elif condition == 2:
            return 'Не любит учиться'
        elif condition == 3:
            return 'Преисполнился в своём познании'

    def apdate(self, condition, student1):
        a = random.randint(1, 12)
        if condition==1:
            if student1.end_or_not(student1) == 'всё хорошо!':
                if a == 12:
                    student1.fun()
                elif 5 <= a <= 11:
                    student1.relax()
                else:
                    student1.study()
        elif condition==2:
            if student1.end_or_not(student1) == 'всё хорошо!':
                if a == 12:
                    student1.study()
                elif 7 <= a <= 11:
                    student1.relax()
                else:
                    student1.fun()
        elif condition==3:
           if student1.end_or_not(student1) == 'всё хорошо!':
                if 1 <= a <= 4:
                    student1.study()
                elif 5 <= a <= 8:
                    student1.relax()
                else:
                    student1.fun()

    def end_or_not(self,student1):
        if self.__health == 0:
            print('Конец игры:', self.__name, ' Не имеет сил ходить по этому бренному миру')
        elif self.__skills == 0:
            print('Конец игры:', self.__name, ' Никому не нужен и ничего не умеет')
        elif self.__progress == 0:
            print('Конец игры:', self.__name, ' Отчислен, всё хорошо')
        elif self.__happy == 0:
            print('Конец игры:', self.__name, 'Колосально-нравственно страдает')
        elif self.__intellect == 0:
            print('Конец игры:', self.__name, 'берёт кредт, ведь чем успешней человек, тем больше у него долг')
        elif self.__health == 1:
            student1.relax()
        elif self.__skills == 1 or self.__progress == 1 or self.__intellect == 1:
            student1.study()
        elif self.__happy == 1:
            student1.fun()
        else:
            return 'всё хорошо!'

class game:
    def __init__(self,n):
        students = [0] * n
        conditions = [0] * n
        for i in range(n):
            conditions[i] = random.randint(1, 3)
            students[i] = student('Студент № ' + str(i+1), random.randint(3, 5),random.randint(3, 5),random.randint(3, 5),random.randint(3, 5),random.randint(3, 5))
            print(students[i].name,'; Здоровье = ',students[i].health,'; Умение = ', students[i].skills,'; Успеваемость = ', students[i].progress,'; Счастье = ', students[i].happy,'; Интеллект = ', students[i].intellect,'; Состояние: ',students[i].returning_conditions(conditions[i]))
            print()
            month=0
        while input('Хотите прожить ещё один месяц') != 'нет':
            month+=1
            print('Прошёл(шло) всего ',month,' месяц(ев)')
            for i in range(n):
                students[i].apdate(conditions[i], students[i])
                print(students[i].name, '; Здоровье = ', students[i].health, '; Умение = ', students[i].skills,'; Успеваемость = ', students[i].progress, '; Счастье = ', students[i].happy, '; Интеллект = ',students[i].intellect, '; Состояние: ', students[i].returning_conditions(conditions[i]))
                print()
def main():
    print('Персонажи: ')
    game(2)
main()