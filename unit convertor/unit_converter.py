import streamlit as st

# Function for conversions
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meters": {"kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084},
        "kilometers": {"meters": 1000, "miles": 0.621371, "feet": 3280.84},
        "miles": {"meters": 1609.34, "kilometers": 1.60934, "feet": 5280},
        "feet": {"meters": 0.3048, "kilometers": 0.0003048, "miles": 0.000189394},
    }
    
    if from_unit == to_unit:
        return value  
    
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None  

def weight_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value 
    
    if from_unit == "kilograms" and to_unit == "grams":
        return value * 1000
    elif from_unit == "kilograms" and to_unit == "pounds":
        return value * 2.20462
    elif from_unit == "grams" and to_unit == "kilograms":
        return value / 1000
    elif from_unit == "grams" and to_unit == "pounds":
        return value * 0.00220462
    elif from_unit == "pounds" and to_unit == "kilograms":
        return value * 0.453592
    elif from_unit == "pounds" and to_unit == "grams":
        return value * 453.592
    else:
        return None

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return None

# Streamlit UI
st.title("Simple Unit Converter")
st.write("Convert between different units effortlessly!")

# Categories and Units
categories = {
    "Length": ["meters", "kilometers", "miles", "feet"],
    "Weight": ["kilograms", "grams", "pounds"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

category = st.selectbox("Choose a category:", list(categories.keys()))
units = categories[category]

from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)
value = st.number_input("Enter value:", min_value=0.0, format="%.4f")

# Convert button logic
if st.button("Convert"):
    if category == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif category == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif category == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    else:
        st.error("Invalid conversion!")