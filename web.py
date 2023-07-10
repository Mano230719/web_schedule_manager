import streamlit as st
import functions

schedule = functions.get_schedule()


def add_item():
    item = st.session_state["new_item"] + "\n"
    schedule.append(item)
    functions.write_schedule(schedule)


st.title("My Schedule Manager")
st.subheader("This is a schedule manager made for the web")
st.write("This app is made to increase your productivity!")

for index, item in enumerate(schedule):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        schedule.pop(index)
        functions.write_schedule(schedule)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="Enter a new item:",
              placeholder="Write your plans here",
              on_change=add_item, key="new_item")
