def dpre(df):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import KBinsDiscretizer

    
    # Data Cleaning
    # handeling missing values
    mean_age = df['Age'].mean()
    df['Age'].fillna(mean_age, inplace=True)
    #Convert categorical to numerical
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    

    # Data Transformation``
    # Create a new column representing family size
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    # Normalization
    df['Fare'] = (df['Fare'] - df['Fare'].mean()) / df['Fare'].std()

    # Data Reduction
    # Remove unnecessary columns
    df.drop(['Name'], axis=1, inplace=True)
    df.drop(['PassengerId'], axis=1, inplace=True)

    # Data Discretization
    # Discretize age into categories
    bins = [0, 18, 30, 50, df['Age'].max()]
    labels = ['child', 'young_adult', 'adult', 'senior']
    df['AgeCategory'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    # Discretize fare into categories
    fare_bins = [-float('inf'), 10, 20, 30, float('inf')]
    fare_labels = ['very_low', 'low', 'medium', 'high']
    df['FareCategory'] = pd.cut(df['Fare'], bins=fare_bins, labels=fare_labels, right=False)

    df.to_csv("res_dpre.csv", index=False)
    print("Dataset has been successfully saved as res_dpre.csv")
