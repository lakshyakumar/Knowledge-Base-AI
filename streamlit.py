# streamlit.py
import streamlit as st
import requests

# Streamlit app title
st.title("Chat with API")

# Input field for the query
query = st.text_input("Enter your query:")

# Button to send the query
if st.button("Send Query"):
    if query:
        # API URL
        api_url = f"http://localhost:8000/query/?query={query}"
        
        try:
            # Sending GET request to the API
            response = requests.get(api_url, headers={"accept": "application/json"})
            
            # Check if the response is successful
            if response.status_code == 200:
                data = response.json()
                # Display the response
                st.write("Query:", data.get("query", "N/A"))
                st.write("Result:", data.get("result", "N/A"))
                st.write("Success:", data.get("success", "N/A"))
            else:
                st.error(f"Error: Received status code {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query.")