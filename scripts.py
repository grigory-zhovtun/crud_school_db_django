from datacenter.models import (
    Commendation,
    Subject,
    Schoolkid,
    Lesson,
    Chastisement,
    Mark
)
import random



UNACCEPTABLE_GRADE=3
BEST_MARK=5

COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражён!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растёшь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно всё получится!"
]


def get_current_student(student_full_name):
    try:
        return Schoolkid.objects.get(
            full_name__icontains=student_full_name.strip()
        )
    except Schoolkid.DoesNotExist:
        print(f'Ученика со строкой «{student_full_name}» в ФИО не существует.')
        return None
    except Schoolkid.MultipleObjectsReturned:
        print(f'Найдено несколько учеников, содержащих «{student_full_name}» в ФИО.')
        return None


def fix_marks(schoolkid):
    updated = (Mark.objects
               .filter(schoolkid=schoolkid, points__lte=UNACCEPTABLE_GRADE)
               .update(points=BEST_MARK))
    print(f'Исправлено оценок: {updated}')


def fix_chastisement(schoolkid):
    kid = Schoolkid.objects.get(
        full_name__contains=schoolkid
    )
    chastisement_kid = Chastisement.objects.filter(
        schoolkid=kid
    )
    chastisement_kid.delete()


def get_random_commendation() -> str:
    return random.choice(COMMENDATIONS)


def create_commendation(name, subject_title):
    kid = Schoolkid.objects.get(
        full_name__contains=name
    )
    subject = Subject.objects.get(
        title__iexact=subject_title,
        year_of_study=kid.year_of_study
    )
    lesson = (Lesson.objects.filter(
        year_of_study=kid.year_of_study,
        group_letter=kid.group_letter,
        subject=subject
    ).order_by('-date').first())
    Commendation.objects.create(
        text=get_random_commendation(),
        created=lesson.date,
        schoolkid=kid,
        subject=subject,
        teacher=lesson.teacher
    )