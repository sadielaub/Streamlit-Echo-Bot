import streamlit as st
prompt = st.chat_input("Say something")
if promt: 
  st.write(f"User has sent the following prompt: {prompt}")
