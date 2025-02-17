# SolarAI Chatbot

SolarAI is an AI-powered chatbot that specializes in answering questions related to solar energy, installation, and market trends. This application is built using Streamlit and integrates with Google's Gemini API to generate responses.

## Features
- AI-powered responses tailored to solar-related queries.
- Distinguishes between technical and non-technical queries.
- Provides a conversational interface using Streamlit.
- Custom UI with avatars and dark-mode-inspired chat styling.

## Technologies Used
- **Python**: For backend logic.
- **Streamlit**: To create the web interface.
- **Google Gemini API**: For AI-generated responses.
- **Requests**: For API calls.
- **Regular Expressions (re)**: To filter relevant queries.
- **Logging**: For debugging and error handling.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/solar-ai-chatbot.git
   cd solar-ai-chatbot
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up the Gemini API key:
   - Replace `GEMINI_API_KEY` in `chatbot.py` with your valid API key.
   - (Recommended) Store the key securely using environment variables.

4. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## File Structure
```
solar-ai-chatbot/
│── chatbot.py       # Handles API calls and query classification
│── app.py           # Streamlit frontend for the chatbot
│── requirements.txt # Required Python dependencies
│── README.md        # Documentation
```

## Usage
1. Start the chatbot by running `streamlit run app.py`.
2. Enter a question related to solar energy in the chat input.
3. The chatbot will classify the query and generate a relevant response.
4. Continue the conversation as needed.

## Example Queries
```
- How efficient are monocrystalline solar panels?
- What are the advantages of net metering?
- How do solar inverters work?
- What is the latest market trend in solar energy?
```

## Security Considerations
- Do **not** expose the API key in a public repository.
- Use **environment variables** to securely store API credentials.
- Validate user input to prevent malicious queries.

## License
This project is open-source and available under the [MIT License](LICENSE).

---
Developed by Tushar Singhal

