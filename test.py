import streamlit as st
import pandas as pd

def main():
    st.title("Streamlit Test App")
    st.write("Hello, Streamlit!")
    
    # Sample DataFrame
    df = pd.DataFrame({
        'Column 1': [1, 2, 3, 4],
        'Column 2': [10, 20, 30, 40]
    })
    
    st.write("Here's a sample DataFrame:")
    st.dataframe(df)

if __name__ == "__main__":
    main()
