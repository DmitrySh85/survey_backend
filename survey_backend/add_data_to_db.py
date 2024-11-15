import json
import os
import django
import pandas as pd


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "survey_backend.settings")
django.setup()

from survey.models import Question
from employees.models import Employee


def insert_questions_to_db():

    file = "files/questions.xlsx"
    df = pd.read_excel(file)
    insert_df_to_db(df)


def insert_users_to_db():
    with open("files/users.json", "r") as file:
        data = json.load(file)
        for user in data:
            try:
                result = Employee.objects.create(**user)
                print(f"Пользователь {result} успешно создан")
            except Exception as e:
                print(e)


def insert_df_to_db(df: pd.DataFrame) -> dict:
    for _, row in df.iterrows():
        row_values = [None if pd.isna(value) else value for value in row.values.tolist()]
        text = row_values[0]
        first_answer = str(row_values[2]) if row_values[1] else ""
        second_answer = str(row_values[3]) if row_values[2] else ""
        third_answer = str(row_values[4]) if row_values[3] else ""
        fourth_answer = str(row_values[5]) if row_values[4] else ""
        valid_answer_number = int(row_values[5])
        description = row_values[6]

        question = Question.objects.create(
            text=text,
            first_answer=first_answer,
            second_answer=second_answer,
            third_answer=third_answer,
            fourth_answer=fourth_answer,
            valid_answer_number=valid_answer_number,
            description=description
        )
        print(f'Вопрос "{question}" добавлен в базу данных')
    print("Успешно сохранено в базу данных.")


if __name__ == "__main__":
    #insert_questions_to_db()
    insert_users_to_db()