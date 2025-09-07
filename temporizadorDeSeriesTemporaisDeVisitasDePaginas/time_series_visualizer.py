import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data
df = pd.read_csv(
    'fcc-forum-pageviews.csv', 
    parse_dates=['date'], 
    index_col='date'
)

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=2)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Preparar dados
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Agrupar por ano e mês e calcular média
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Nomes dos meses na ordem correta
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar.plot(kind='bar', ax=ax)

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", labels=month_order)
    plt.tight_layout()
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Cores para os meses
    month_colors = ["#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4",
                    "#46f0f0", "#f032e6", "#bcf60c", "#fabebe", "#008080", "#e6beff"]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1, palette="Set2")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    
    # Month-wise box plot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", 
                   "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=month_order, palette=month_colors)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
