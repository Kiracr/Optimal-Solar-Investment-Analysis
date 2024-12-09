import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import numpy as np
from utils import load_city_data, filter_data_by_date

CITIES = ['benin-malanville', 'sierraleone-bumbuna', 'togo-dapaong_qc']


def load_sidebar():
    """Renders the sidebar with city and date selection."""
    st.sidebar.title(' Weather & Solar Dashboard')
    selected_city = st.sidebar.selectbox('Select a City', CITIES)
    selected_date = st.sidebar.date_input('Select a Date', datetime.now().date())
    return selected_city, selected_date


def display_summary_statistics(data):
    """Displays summary statistics for the selected data."""
    st.subheader('Summary Statistics')
    st.write(data.describe())


def plot_irradiance(data):
    """Plots solar irradiance data."""
    st.subheader('Solar Irradiance Over Time')
    fig = px.line(
        data, 
        x='Timestamp', 
        y=['GHI', 'DNI', 'DHI'],
        labels={'value': 'Irradiance (W/m²)', 'Timestamp': 'Time'},
        title='Global, Direct, and Diffuse Irradiance'
    )
    st.plotly_chart(fig)


def plot_temperature_and_humidity(data):
    """Plots ambient temperature and humidity data."""
    st.subheader('Ambient Temperature and Relative Humidity')
    fig = px.line(
        data, 
        x='Timestamp', 
        y=['Tamb', 'RH'],
        labels={'value': 'Measurement', 'Timestamp': 'Time'},
        title='Temperature (°C) and Humidity (%)'
    )
    st.plotly_chart(fig)


def plot_wind_data(data):
    """Plots wind speed and gust data."""
    st.subheader('Wind Speed and Direction')
    fig = px.line(
        data, 
        x='Timestamp', 
        y=['WS', 'WSgust'],
        labels={'value': 'Wind Speed (m/s)', 'Timestamp': 'Time'},
        title='Wind Speed and Gusts'
    )
    st.plotly_chart(fig)


def plot_module_temperatures(data):
    """Plots module temperatures."""
    st.subheader('Module Temperatures (A & B)')
    fig = px.line(
        data, 
        x='Timestamp', 
        y=['TModA', 'TModB'],
        labels={'value': 'Temperature (°C)', 'Timestamp': 'Time'},
        title='Temperature of Modules A and B'
    )
    st.plotly_chart(fig)


def display_raw_data(data):
    """Displays the raw data."""
    st.subheader('Raw Data')
    st.dataframe(data)


def main():
    """Main function to execute the Streamlit app."""
    selected_city, selected_date = load_sidebar()

    # Load data for the selected city
    df = load_city_data(selected_city)
    if df.empty:
        st.error("Failed to load data. Please check the data files.")
        return

    st.sidebar.success(f"Loaded data for **{selected_city}**")

    # Filter data for the selected date
    daily_data = filter_data_by_date(df, selected_date)
    if daily_data.empty:
        st.warning(f"No data available for {selected_date} in {selected_city}.")
    else:
        st.title(f"{selected_date} - {selected_city.capitalize()} Weather & Solar Data")
        display_summary_statistics(daily_data)
        plot_irradiance(daily_data)
        plot_temperature_and_humidity(daily_data)
        plot_wind_data(daily_data)
        plot_module_temperatures(daily_data)
        display_raw_data(daily_data)


if __name__ == '__main__':
    main()
