import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr
from typing import List



#importing the dataframes to use in visualizations
def load_world_cup_df():
    return pd.read_csv("data/FIFA - World Cup Summary.csv")

def load_volcano_df():
    return pd.read_csv("data/volcanoes_updated.csv")

def load_merged_df():
    return pd.read_csv("data/merged_df.csv")

def load_volcano_true_df():
    return pd.read_csv("data/volcanoes_true.csv")

def load_volcano_false_df():
    return pd.read_csv("data/volcanoes_false.csv")



# volcano_df, volcano_true_df, volcano_false_df, merged_df = import_dataframes()

#first visualization
def plot_dataframe_rows_1(volcano_true_df, volcano_false_df):
    num_rows_True = len(volcano_true_df)
    num_rows_False = len(volcano_false_df)

    fig, ax = plt.subplots()
    bar_width = 0.35

    bar1 = ax.bar(1, num_rows_True, bar_width, label='True')
    bar2 = ax.bar(1 + bar_width, num_rows_False, bar_width, label='False')

    ax.set_xticks([1 + bar_width / 2])
    ax.set_xticklabels([''])

    ax.legend()

    plt.xlabel("World Cup Year")
    plt.ylabel("Number of Eruptions")
    plt.savefig("images/1.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
    
    
#second visualization
def plot_vei_value_by_year(volcano_df):
    sns.set(style="darkgrid")
    sns.pointplot(x="World_Cup_Year", y="fields.vei", data=volcano_df)
    plt.title("VEI Value by World Cup Year")
    plt.xlabel("World Cup Year")
    plt.ylabel("VEI Value")
    plt.savefig("images/2.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
    




#third visualization
def plot_avg_vei_value_by_year(volcano_df):
    sns.set(style="darkgrid")
    sns.barplot(x="World_Cup_Year", y="fields.vei", data=volcano_df)
    plt.title("AVG/VEI Value by Year")
    plt.xlabel("World Cup Year")
    plt.ylabel("VEI Value")
    plt.savefig("images/3.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
    

#fourth visualization
def plot_vei_value_by_world_cup_year(volcano_df):
    fig, ax = plt.subplots()

    # Group the data by World_Cup_Year
    grouped = volcano_df.groupby('World_Cup_Year')

    # Plot the lines for each group
    for name, group in grouped:
        ax.plot(group['fields.year'], group['fields.vei'], marker='o', linestyle='-', label=str(name))

    # Add the legend, labels, and title
    ax.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('VEI Value')
    ax.set_title('VEI Value by World Cup Year')
    plt.savefig("images/4.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
    

#fifth and sixth visualization
def visualize_vei_values(volcano_df):
    # Scatter plot for World Cup years
    sns.set(style="darkgrid")
    world_cup = volcano_df[volcano_df['World_Cup_Year'] == True]
    sns.scatterplot(x=world_cup.index, y="fields.vei", data=world_cup)
    plt.title("VEI Value of Eruptions in World Cup Years")
    plt.xlabel("Year of Eruption")
    plt.ylabel("VEI Value")
    plt.savefig("images/5.jpeg", dpi=300, bbox_inches='tight')
    plt.show()

    # Scatter plot for non-World Cup years
    sns.set(style="darkgrid")
    non_world_cup = volcano_df[volcano_df['World_Cup_Year'] == False]
    sns.scatterplot(x=non_world_cup.index, y="fields.vei", data=non_world_cup)
    plt.title("VEI Value of Eruptions in Non-World Cup Years")
    plt.xlabel("Year of Eruption")
    plt.ylabel("VEI Value")
    plt.savefig("images/6.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
    

#lucky number seven
def plot_champions_vei(df, title, xlabel, ylabel, filename):
    filtered_df = df[df['World_Cup_Year'] == True]
    sns.boxplot(x="CHAMPION", y="fields.vei", data=filtered_df)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
    
    

#heatmap visualization

def visualize_correlation(merged_df, key_column='key_column'):
    #dropping key column to have only numerical values for pearson-r test
    merged_df = merged_df.drop(key_column, axis=1)

    #create correlation matrix
    correlation_matrix = merged_df.corr(method='pearson')
    # create a dictionary to store the significant correlations
    significant_correlations = {}

    for i in range(correlation_matrix.shape[0]):
        for j in range(correlation_matrix.shape[0]):
            if i >= j:
                continue
            corr, p_value = pearsonr(correlation_matrix.iloc[i], correlation_matrix.iloc[j])
            if p_value < 0.05:
                significant_correlations[(correlation_matrix.columns[i], correlation_matrix.columns[j])] = corr

    #creating a heatmap to visualize the relationship among statistically significant correlations. 
    data = []
    for i, j in significant_correlations.items():
        data.append((i[0], i[1], j))
    df = pd.DataFrame(data, columns=['Variable 1', 'Variable 2', 'Correlation'])

    plt.figure(figsize=(10,8))
    sns.heatmap(df.pivot('Variable 1', 'Variable 2', 'Correlation'), annot=True)
    plt.title('Heatmap of Correlations')
    plt.savefig("images/heatmap.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
