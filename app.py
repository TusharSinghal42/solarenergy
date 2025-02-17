import streamlit as st
from chatbot import generate_response

# Set page configuration with an icon
st.set_page_config(page_title="SolarAI", page_icon="⚡")


# Display title with icon
st.markdown("""
    <h1 style="display: flex; align-items: center; color: black;">
        <img src="https://cdn-icons-png.flaticon.com/512/2906/2906276.png" width="40" style="margin-right: 10px;">
        SolarAI
    </h1>
""", unsafe_allow_html=True)

st.write("Ask me anything about solar energy, installation, or market trends!")
st.divider()

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Custom CSS for dark mode, aligned messages, and avatars
st.markdown("""
    <style>
        body, .stApp {
            background-color: white !important;
        }
        .chat-container {
            display: flex;
            align-items: center;
            margin: 10px 0;
        }
        .user-container {
            justify-content: flex-end;
        }
        .assistant-container {
            justify-content: flex-start;
        }
        .chat-message {
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
            max-width: 70%;
        }
        .user-message {
            background-color: #b61c1c;
            color: white;
            text-align: right;
        }
        .assistant-message {
            background-color: #333;
            color: white;
            text-align: left;
        }
        .chat-icon {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            margin: 0 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Display conversation history with icons
for chat in st.session_state.conversation_history:
    if chat["role"] == "user":
        st.markdown(f"""
            <div class="chat-container user-container">
                <div class="chat-message user-message">{chat['content']}</div>
                <img src="https://cdn-icons-png.flaticon.com/512/1144/1144760.png" class="chat-icon">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-container assistant-container">
                <img src="https://cdn-icons-png.flaticon.com/512/4712/4712038.png" class="chat-icon">
                <div class="chat-message assistant-message">{chat['content']}</div>
            </div>
        """, unsafe_allow_html=True)

# Get new user input
text = st.chat_input("Enter your question")

if text:  # Ensure input is not empty
    st.session_state.conversation_history.append({"role": "user", "content": text})
    st.markdown(f"""
        <div class="chat-container user-container">
            <div class="chat-message user-message">{text}</div>
            <img src="https://cdn-icons-png.flaticon.com/512/1144/1144760.png" class="chat-icon">
        </div>
    """, unsafe_allow_html=True)

    # Generate and display assistant response
    response = generate_response(text)
    st.session_state.conversation_history.append({"role": "assistant", "content": response})
    st.markdown(f"""
        <div class="chat-container assistant-container">
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712038.png" class="chat-icon">
            <div class="chat-message assistant-message">{response}</div>
        </div>
    """, unsafe_allow_html=True)


