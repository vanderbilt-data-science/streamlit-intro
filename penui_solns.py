#This file describes the streamlit interface for a penguins UI
import streamlit as st
import pandas as pd
import seaborn as sns
from basic_analysis import *
import plotly.express as px

st.title('Exploring the Penguins Dataset')
st.write('Learn a little more about penguins...')

st.header('Basic data structure')
st.write('Below, we can see the basic contents of the penguins data.  :smile:')
if 'df' not in st.session_state:
    df = pd.read_csv('penguins.csv')
    st.session_state.df = df
df = st.session_state.df
nrow_orig = len(df)

#show dataframe
st.dataframe(df.head())

#Optional cleaning operations
st.header('Optional cleaning operations')
if st.button('Remove NAs'):
    df.dropna(inplace=True)
    st.write('Dropped NAs.  The new data size is: ', len(df), 'with ', nrow_orig - len(df), 'rows removed.')
    st.session_state.df = df
df = st.session_state.df

#Basic data visualization
st.header('Basic data visualization')
st.write("Let's take a look at the basic distribution of the data.")
st.write(len(df))

st.subheader('Categorical variables')
fig = plot_multiple(df, include='object', figsize=(9,4))
st.pyplot(fig)

st.subheader('Numerical variables')
fig = plot_multiple(df, exclude='object', figsize=(9,4))
st.pyplot(fig)

#Advanced data visualization
st.header('Relationships')
with st.beta_expander("View pairwise relationships"):
    hue_sel = st.selectbox('Group visualization', ['None', 'island', 'species', 'sex'])
    hue_col = None if hue_sel == 'None' else hue_sel
    pplt = sns.pairplot(data=df, hue=hue_col)
    st.pyplot(pplt)

#Interactivity
st.header('Interact')
st.write('Choose two columns and view the interaction:')
col_vars = df.columns.tolist()
c1, c2 = st.beta_columns(2)
xvar = c1.selectbox('X variable', col_vars, index=2)
yvar = c2.selectbox('Y variable', col_vars, index=3)

scatter_plt = px.scatter(df, x=xvar, y=yvar)
st.plotly_chart(scatter_plt)

#Model
st.header('Model')
st.write('Choose a good threshold for classification using the slider below')
thresh_val = st.slider('Select threshold', min_value=0.0, max_value=0.99, value=0.5, step=0.01)

if 'pred_df' not in st.session_state:
    pred_df = generate_test_data()
    st.session_state.pred_df = pred_df

disp = tune_threshold(st.session_state.pred_df, thresh_val)
disp.plot(cmap='RdPu').figure_
#st.pyplot(disp.plot(cmap='RdPu').figure_)

#Predict
st.sidebar.header('Predict')
st.sidebar.write('Make predictions about penguin of interest')

with st.sidebar.form('pred_form'):
    c1, c2, c3 = st.beta_columns(3)
    sel_species = c1.selectbox('Species', df['species'].unique())
    sel_island = c2.selectbox('Island', df['island'].unique())
    sel_mass = c3.number_input('Body Mass (g)', min_value=10, max_value = 7500, value=2500)
    submitted = st.form_submit_button("Submit")
    if submitted:
        pred_input = {'species':sel_species, 'island':sel_island, 'mass':sel_mass}
        sex = penguins_predict(pred_input, thresh_val)
        st.write('Based on your inputs and a threshold of ', thresh_val, 'the predicted penguin sex is: ', sex)

