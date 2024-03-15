def eda(df):
    import pandas as pd
    import numpy as np


    # Insight 1: Survival Rate by Gender
    survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()
    with open("eda-in-1.txt", "w") as file:
        file.write("Survival Rate by Gender:\n")
        file.write("Male: {:.2%}\n".format(survival_rate_by_gender[0]))
        file.write("Female: {:.2%}\n".format(survival_rate_by_gender[1]))

    # Insight 2: Average Fare by Passenger Class
    average_fare_by_class = df.groupby('Pclass')['Fare'].mean()
    with open("eda-in-2.txt", "w") as file:
        file.write("Average Fare by Passenger Class:\n")
        for pclass, avg_fare in average_fare_by_class.items():
            file.write("Class {}: ${:.2f}\n".format(pclass, avg_fare))

    # Insight 3: Percentage of Passengers with Family Onboard
    df['FamilySize'] = df['SibSp'] + df['Parch']
    passengers_with_family_percentage = (df[df['FamilySize'] > 0].shape[0] / df.shape[0]) * 100
    with open("eda-in-3.txt", "w") as file:
        file.write("Percentage of Passengers with Family: {:.2f}%\n".format(passengers_with_family_percentage))

    print("Insights saved as text files.")
