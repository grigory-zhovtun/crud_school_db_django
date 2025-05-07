# Scripts for Electronic Diary

Small helper scripts for the **Electronic Diary** Django project.
They let a teacher quickly:

* find a pupil by name *(even if you type only first or last name);*
* change bad marks (`2` and `3`) to excellent marks (`5`);
* delete all punishments (*chastisements*) for a pupil;
* add a nice **commendation** to the last lesson of a subject.

> Made for learning Django ORM.
> Code is short and easy to read.

---

## Requirements

* Python 3.10+
* Django 4.x
* A running Electronic Diary project with the models from `datacenter.models`.

_No extra packages needed._

---

## How to run in Django shell

1.  **Open the Django shell:**
    ```bash
    python manage.py shell
    ```

2.  **Inside the shell, import the module and use the functions:**
    ```python
    import scripts

    # Find pupil
    # Prints a message if zero or many pupils found.
    kid = scripts.get_current_student("Stepan")

    # Change all 2/3 marks to 5
    scripts.fix_marks("Иванов")

    # Remove punishments
    scripts.fix_chastisement("Иванов")

    # Add a commendation to the last lesson of the subject
    scripts.create_commendation(
        name="Иванов Иван",          # pupil's full name or part of it
        subject_title="Математика"   # exact subject title
    )
    ```

That’s all 🎉

---

## Function list

| Function                                     | What it does                                                                                       | Returns                 |
|----------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------|
| `get_current_student(name)`                  | Find one pupil by part of full name. Prints a message if zero or many pupils are found.             | `Schoolkid` object or `None` |
| `fix_marks(schoolkid_name_or_obj)`           | Change every mark ≤ `3` to `5` for the specified pupil. Accepts pupil's name or `Schoolkid` object. | —                       |
| `remove_chastisements(schoolkid_name_or_obj)`| Delete all `Chastisement` entries for the specified pupil. Accepts pupil's name or `Schoolkid` object. | —                       |
| `get_random_commendation()`                  | Pick one nice phrase from the predefined list.                                                     | `str`                   |
| `create_commendation(name, subject_title)`   | Add a `Commendation` with a random phrase to the last lesson of the specified subject for a pupil.   | —                       |

---

## Tips

* Call `scripts.get_random_commendation()` if you just need a random commendation phrase.
* After editing `scripts.py` while the Django shell is open, reload the module to apply changes:
    ```python
    import importlib
    import scripts # if you haven't imported it with this name
    importlib.reload(scripts)
    ```

---

## License

MIT – do whatever you want, just keep the link to the original if you share or modify.