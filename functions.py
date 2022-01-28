#importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing the dataset
fashion_dataset = pd.read_csv("data/fashion_dataset.csv")

#This drops columns that are not required
fashion_dataset.drop(fashion_dataset.filter(regex="Unnamed"),axis=1, inplace=True)

def article_type_freq(year):

    #ARTICLE TYPE WITH HIGHEST SALES
    article_type = fashion_dataset[fashion_dataset["year"] == year]
    article_type_freq = article_type.groupby("articleType")["articleType"].count().reset_index(name="article_freq").sort_values(by="article_freq", ascending= False)
    article= article_type_freq.head()
    #To increase the size of the chart
    plt.figure(figsize = (6,5))
    #add colors
    colors = ['#0B1C48','#E66912','#9E3A14','#016367','#0D698B']
    #plot pie chart
    article.groupby(['articleType']).sum().plot(kind='pie', subplots=True, autopct='%1.0f%%',
                                                     colors = colors,legend = False,figsize=(10,8))
    #add title
    plt.title('Top 5 loved fashion wears in ' + str(year), {'fontsize': 15})

    # turn off the axes
    plt.axis('off')

    #Make it to donut_chart
    circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(circle)
    plt.savefig('images/articleType.png')
    return

def season_wears(season):

    season_clothes = fashion_dataset[fashion_dataset["season"] == season]
    #sorting the values

    Usage_freq = season_clothes.groupby("usage")["usage"].count().reset_index(name="usage_freq").sort_values(by="usage_freq", ascending= False)

    Usage_freq = Usage_freq[:5]

    #add colors
    colors = ['#C9595F','#372F2F','#FBCE3A','#E0D0B8','#FF1643']

    #plot pie chart
    Usage_freq.groupby(['usage']).sum().plot(kind='pie', subplots=True, autopct='%1.0f%%',explode=[0.05]*5,
                                colors = colors, legend = False,figsize=(10,8))
    # turn off the axes
    plt.axis('off')
    #add title
    plt.title('Most loved fashion usage in ' + season, {'fontsize': 20})

    plt.savefig('images/Fashion_usage.png')
    return

def top_selling(gender):
    top = fashion_dataset[fashion_dataset["gender"] == gender]
    #MASTER CATEGORY WITH THE HIGHEST SALES

    MasCat_sales = top.groupby("masterCategory")["year"].count().reset_index(name="mascat_sales")

    Master_category = MasCat_sales.groupby(['masterCategory']).sum().sort_values(by="mascat_sales", ascending= False).plot(kind='bar', color = '#372F2F',
                                                            subplots=True,legend = False)
    plt.title('Top selling wears of ' + gender, {'fontsize': 15})
    plt.xlabel('Master Category', {'fontsize':10})
    plt.xticks(rotation= 30,)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.savefig('images/Top_selling.png')
    return

def best_colour(gender):
    top = fashion_dataset[fashion_dataset["gender"] == gender]

    gender_colour = top.groupby(["baseColour"])["baseColour"].count().reset_index(name="color_freq").sort_values(by="color_freq", ascending= False)

    colour = gender_colour[:10]
    graph = sns.barplot(data= colour, x="baseColour", y="color_freq",color = '#9E3A14')
    plt.title('Favourite fashion colour of ' + gender, {'fontsize': 15})
    plt.xlabel('Colour', {'fontsize':10})
    plt.xticks(rotation= 30,)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.savefig('images/Colour.png')
    return