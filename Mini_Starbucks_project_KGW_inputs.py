
import streamlit as st
import pandas as pd 
import plotly.express as px

df = pd.read_csv('data/cleaned_starbucks.csv')
st.title('🧋 Starbucks Explorer',)
page = st.sidebar.selectbox('Select a Page',['Home','Data Overview','Exploratory Data Analysis','Visualization',''])

#Home Page
if page == 'Home':
    st.title('📊 Starbucks Dataset Explore')
    st.subheader('Welcome to my Starbucks dataset explorer app')
    st.write("""
             This app provides an interactive platform to explore the Starbucks data set.
             You can visualize the distribution of data, explore relationship between features, and even make predictions on new data!
             Use the sidebar to navigate through the sections.""")
    
elif page == 'Data Overview':
    st.title('Data Overview')
    st.subheader('About the Data')
    st.write("""
            The Starbucks dataset is a comprehensive data set that gives a detail analysis of the starbucks menu options. It allows potential 
             to understand matrics like calorie intake and the fat level of all the menu option. Through understanding this dataset the 
             customer can make a more informed decision about which item from the starbucks menue is best for them""")
    st.subheader('Quick glance at the Data')
    if st.checkbox('Show DataFrame'):
        st.dataframe(df)
    if st.checkbox('Show shape of data'):
        st.write(f"The dataset contains{df.shape[0]} rows and {df.shape[1]} columns.")

elif page == 'Exploratory Data Analysis':
    st.title('Exploratory Data Analysis(EDA)')
st.subheader('Select the type of Visualization you like to explore')
eda_type = st.multiselect('Visualization Options',
                          ['Histograms','Box Plots','Scatterplots','Count Plots'])

num_col = ['Calories', 'Total Fat (g)', 'Trans Fat (g)', 'Saturated Fat (g)', 'Sodium (mg)', 'Total Carbohydrates (g)', 'Cholesterol (mg)', 'Dietary Fibre (g)', 'Sugars (g)', 'Protein (g)', 'Vitamin A (% DV)', 'Vitamin C (% DV)', 'Calcium (% DV)', 'Iron (% DV)', 'Caffeine (mg)']
if 'Histograms' in eda_type:
    st.subheader("Histograms - Visualizing Numerical Distributions")
    h_selected_col = st.selectbox("Select a numerical column for the histogram:", options=num_col)
    if h_selected_col:
        chart_title = f"Distribution of {h_selected_col.title().replace('_', ' ')}"
        if st.checkbox("Show by Species"):
            st.plotly_chart(px.histogram(df, x=h_selected_col, color='species', title=chart_title, barmode='overlay'))
        else:
           st.plotly_chart(px.histogram(df, x=h_selected_col, title=chart_title))    


if 'Box Plots' in eda_type:
    st.subheader('Box Plots - Visualization Numerical Distribution')
    b_selected_col = st.selectbox('Select a numerical column for the box plot:',num_col)
    if b_selected_col:
        chart_title = f"Distribution of {b_selected_col.title().replace('_','')}"
        st.plotly_chart(px.box(df,x = 'Beverage_category',y= b_selected_col,title = chart_title, color = 'Beverage_category'))

if 'Scatterplots' in eda_type:
    st.subheader('Scatterplots-Visualizing Relations')
    selected_col_x = st.selectbox('Select x-axis variable:',num_col)
    selected_col_y = st.selectbox('Select y-axis variable:',num_col)
    if selected_col_x and selected_col_y:
        chart_title = f"{selected_col_x.title().replace('_','')} vs. {selected_col_y.title().replace('_','')}"
        st.plotly_chart(px.scatter(df,x=selected_col_x,y= selected_col_y, color = 'Beverage_category',title=chart_title))
obj_cols = ['Beverage_category', 'Beverage','Beverage_prep']

if 'Count Plots' in eda_type:
    st.subheader('Count Plot- Visualizing Categorical Distribution')
    selected_col = st.selectbox('Select a categorical variable',obj_cols)
    if selected_col:
        chart_title = f"Distribution of {selected_col.title()}"
        st.plotly_chart(px.histogram(df, x = selected_col, color = 'Beverage_category',title = chart_title))

st.title('Adding Tabs')
tab1,tab2,tab3 = st.tabs(['First Tab', 'Second Tab', 'Third Tab'])

with tab1:
    st.header("Company's Mission Statement")
    st.write("""To be the premier purveyor of the finest coffee in the world, inspiring and nurturing the human spirit 
             — one person, one cup and one neighborhood at a time.""")
with tab2:
    st.header("Comapany commitment towards excellence")
    st.write("""We delight in the rigor of the details-no matter what our job is
            We learn and teach in the pursuit of growth
            We deliver excellence with passion and creativity""")
with tab3:
    st.header("How to Contact us")
    st.write('1(800)-777-3175')