import streamlit as st
import pandas as pd
import plotly.express as px

# Read the data from CSV
df = pd.read_csv("World_Bank_Program_Budget_and_All_Funds_20240406.csv")

# Data preprocessing
df['Fiscal Year'] = df['Fiscal Year'].astype(str)
df['Bank Budget (BB) (US$, Millions)'] = df['Bank Budget (BB) (US$, Millions)'].fillna(0)
df['All Funds (US$, Millions)'] = df['All Funds (US$, Millions)'].fillna(0)


def app():
    st.title('Regional Budget Analysis')

    # Budget Allocation by Region (FY2024)
    st.subheader('Budget Allocation by Region (FY2024)')
    df_region = df[(df['Fiscal Year'] == '2024') & (df['Work Program'] == 'Country Engagement')]
    df_region = df_region[df_region['Unit'] != 'Africa']
    df_region = df_region.groupby('Unit')['All Funds (US$, Millions)'].sum().reset_index()

    fig1 = px.pie(df_region, values='All Funds (US$, Millions)', names='Unit',
                  title='Budget Allocation by Region (FY2024)')
    st.plotly_chart(fig1, use_container_width=True)

    # Budget per Capita by Region
    st.subheader('Budget per Capita by Region (FY2024)')
    # Population data for each region (As of April 2023)
    population_data = {
        'Africa East': 486000000,
        'Africa West': 448000000,
        'East Asia & Pacific': 2320000000,
        'Europe & Central Asia': 918000000,
        'Latin America & Caribbean': 653000000,
        'Middle East & North Africa': 456000000,
        'South Asia': 1868000000
    }

    # Calculate 'Budget per Capita (US$)'
    df_region['Population'] = df_region['Unit'].map(population_data)
    df_region['Budget per Capita (US$)'] = df_region['All Funds (US$, Millions)'] * 1000000 / df_region['Population']
    df_region = df_region[df_region['Unit'] != 'Other Operational Units\' Allocations']

    # Sort the dataframe by 'Budget per Capita (US$)' in descending order
    df_region_sorted = df_region.sort_values('Budget per Capita (US$)', ascending=False)

    # Bar Chart
    fig2 = px.bar(df_region_sorted, x='Unit', y='Budget per Capita (US$)', title='Budget per Capita by Region (FY2024)')
    fig2.update_layout(xaxis_title='Region', yaxis_title='Budget per Capita (US$)')
    st.plotly_chart(fig2, use_container_width=True)


if __name__ == '__main__':
    app()