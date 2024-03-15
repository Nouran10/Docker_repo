def vis(df):
        import matplotlib.pyplot as plt
        import pandas as pd

        # Scatter plot showing the relationship between horsepower and price
        plt.figure(figsize=(8, 6)) 
        plt.scatter(data=df, x='Age', y='Fare')
        plt.xlabel('Age')
        plt.ylabel('Fare')
        plt.title('Scatter Plot: Age vs. Fare')
        plt.savefig('vis.png')  
        plt.show()
        plt.close()