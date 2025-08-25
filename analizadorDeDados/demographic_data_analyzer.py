import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    num_bachelors = len(df[df['education'] == 'Bachelors'])
    total_num = len(df)
    percentage_bachelors = round((num_bachelors / total_num) * 100, 1)

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    num_higher_rich = len(higher_education[higher_education['salary'] == '>50K'])
    higher_education_rich = round((num_higher_rich / len(higher_education)) * 100, 1)
    
    num_lower_rich = len(lower_education[lower_education['salary'] == '>50K'])
    lower_education_rich = round((num_lower_rich / len(lower_education)) * 100, 1)

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    num_rich_min_workers = len(num_min_workers[num_min_workers['salary'] == '>50K'])
    
    rich_percentage = round((num_rich_min_workers / len(num_min_workers)) * 100, 1)

    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    percentage_rich_per_country = (rich_country_counts / country_counts) * 100
    
    highest_earning_country = percentage_rich_per_country.idxmax()
    highest_earning_country_percentage = round(percentage_rich_per_country.max(), 1)

    india_rich_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich_df['occupation'].value_counts().idxmax()

    if print_data:
        print("Número de cada raça:\n", race_count) 
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem com diploma de bacharel: {percentage_bachelors}%")
        print(f"Porcentagem com educação superior que ganha >50K: {higher_education_rich}%")
        print(f"Porcentagem sem educação superior que ganha >50K: {lower_education_rich}%")
        print(f"Mínimo de horas de trabalho: {min_work_hours} horas/semana")
        print(f"Porcentagem de ricos entre os que trabalham o mínimo de horas: {rich_percentage}%")
        print("País com a maior porcentagem de ricos:", highest_earning_country)
        print(f"Maior porcentagem de ricos no país: {highest_earning_country_percentage}%")
        print("Ocupação mais popular na Índia para quem ganha >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }