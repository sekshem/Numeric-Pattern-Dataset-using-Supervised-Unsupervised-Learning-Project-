from faker import Faker
import pandas as pd
import numpy as np
import random
import os

# Initialize Faker
fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

# Number of records
NUM_ROWS = 10000

data = []

for _ in range(NUM_ROWS):

    age = random.randint(20, 60)

    experience = max(0, age - random.randint(20, 25))

    education = random.randint(50, 100)

    skill = random.randint(40, 100)

    performance = random.randint(50, 100)

    projects = random.randint(1, 20)

    attendance = random.randint(60, 100)

    training = random.randint(10, 200)

    iq = random.randint(80, 150)

    income = (
        25000
        + experience * 3500
        + education * 250
        + skill * 500
        + performance * 400
        + np.random.normal(0, 5000)
    )

    target = (
        0.15 * income
        + 3 * experience
        + 2 * skill
        + 1.8 * performance
        + 4 * projects
        + np.random.normal(0, 100)
    )

    data.append([
        age,
        income,
        experience,
        education,
        skill,
        performance,
        projects,
        attendance,
        training,
        iq,
        target
    ])

columns = [
    "Feature_1_Age",
    "Feature_2_Income",
    "Feature_3_Experience",
    "Feature_4_Education",
    "Feature_5_Skill",
    "Feature_6_Performance",
    "Feature_7_Projects",
    "Feature_8_Attendance",
    "Feature_9_TrainingHours",
    "Feature_10_IQ",
    "Target"
]

df = pd.DataFrame(data, columns=columns)


for col in df.columns:
    df.loc[df.sample(frac=0.02).index, col] = np.nan


duplicates = df.sample(50, random_state=42)

df = pd.concat([df, duplicates], ignore_index=True)

outliers = np.random.choice(df.index, 50)

df.loc[outliers, "Feature_2_Income"] *= 5

output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "numeric_pattern.csv"
)

df.to_csv(output_path, index=False)

print("=" * 60)
print("Dataset Generated Successfully")
print("=" * 60)
print(df.head())
print("\nShape :", df.shape)
print("\nSaved To :", output_path)