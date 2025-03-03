import streamlit as st
import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

st.title("Rock, Paper, Scissors Game")

st.write("Choose your move:")

user_choice = st.radio("Select one:", ["Rock", "Paper", "Scissors"], index=0)

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Play"):  
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    st.session_state.history.append((user_choice, computer_choice, result))
    
    st.write(f"**Your choice:** {user_choice}")
    st.write(f"**Computer's choice:** {computer_choice}")
    st.subheader(result)

st.write("### Previous Matches")
for i, (u_choice, c_choice, res) in enumerate(reversed(st.session_state.history[-5:]), 1):
    st.write(f"{i}. You: {u_choice} | Computer: {c_choice} | Result: {res}")
