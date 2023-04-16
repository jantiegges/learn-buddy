import streamlit as st
from streamlit_chat import message

st.title("Your Pair Learning Buddy")
st.caption("This is a website for you to learn with your AI learn buddy. You can upload files containing context for your learning (e.g. lecture scripts, slides, etc.) and your buddy will help you learn by asking you questions about the content.")


st.header("Upload Context Files")
uploaded_files = st.file_uploader(
    "Choose a file", type="pdf", accept_multiple_files=True)

if uploaded_files is not None:
    for file in uploaded_files:
        bytes_data = file.read()
        st.write(file.name)
        st.write(bytes_data)


st.header("Prompt your Buddy")
prompt = st.text_input(
    "Prompt your buddy to ask you a question about the context you uploaded.")

st.header("Chat with your Learning Buddy")

# Initialization
if 'bot_history' not in st.session_state:
    st.session_state['bot_history'] = ['Question 1']

if 'user_history' not in st.session_state:
    st.session_state['user_history'] = []

bot_history = st.session_state['bot_history']
user_history = st.session_state['user_history']

chat_len = len(bot_history)

for i, m in enumerate(bot_history):
    message(m, key=f"bot{i}")

    if i < chat_len-1:
        message(user_history[i], is_user=True, key=f"user{i}")


def test():
    print("Hello")


user_input = st.text_input("You:", on_change=test)

if st.button("Send"):
    st.session_state['user_history'].append(user_input)
    st.session_state['bot_history'].append("Question " + str(chat_len + 1))

    # Refresh the page
    st.experimental_rerun()


# @st.cache
# def chat():

#     # c_chat = st.container()
#     # with st.spinner("Thinking..."):
#     #     time.sleep(2)
#     # c_chat.write(message("Hey buddy!"))

#     # answer = st.text_input(
#     #     "Answer your buddy.")
#     # c_chat.write(message(answer), is_user=True)

#     msg = st.text_area("You:")

#     history_bot = st.session_state.get('history_bot', [])
#     history_user = st.session_state.get('history_user', [])

#     for i, msg in enumerate(history_bot):
#         st.write(message(msg))
#         st.write(message(history_user[i]), is_user=True)

#     if msg:
#         st.session_state.history_user.append(msg)
#         st.session_state.history_bot.append("Fake Answer")


# # if button is clicked refresh the page
# if st.button("Send"):
#     st.session_state.history_bot.append("Fake Question")
#     chat()
