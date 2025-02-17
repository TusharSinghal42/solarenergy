import requests
import re
import logging

# Gemini API Key (Use environment variables or a secure method in production)
GEMINI_API_KEY = "AIzaSyBgd0du22e7dTxASubfqUxJLmKBHiyQTGU"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def is_solar_related(query):
    """Determines if a query is related to the solar industry."""
    solar_keywords = ["solar", "photovoltaic", "PV", "sunlight", "solar panel", "renewable energy", "inverter", "battery storage", "LCOE", "grid-tied", "off-grid", "solar efficiency", "net metering", "solar installation","solar energy", "solar power", "photovoltaics", "solar panels", "solar cells",
    "renewable energy", "solar radiation", "solar efficiency", "solar thermal",
    "solar inverter", "solar battery", "solar storage", "solar array", "net metering",
    "solar farms", "solar grid", "solar tracking", "off-grid solar", "grid-tied solar",
    "solar rooftop", "solar heating", "solar cooling", "solar water heater",
    "solar concentrator", "solar thermal collector", "solar photovoltaic (PV)",
    "solar energy conversion", "solar hybrid system", "solar electrification",
    "solar charge controller", "solar module", "monocrystalline solar panel",
    "polycrystalline solar panel", "thin-film solar panel", "solar LED lighting",
    "solar economics", "solar subsidies", "solar policy", "solar installation",
    "solar maintenance", "solar degradation", "solar power plant", "floating solar",
    "solar carport", "solar-powered devices", "solar energy storage",
    "solar energy advantages", "solar energy disadvantages", "solar industry",
    "solar research", "solar grid integration", "solar innovation","energy"]
    return any(re.search(rf"\b{kw}\b", query, re.IGNORECASE) for kw in solar_keywords)

def is_technical_query(query):
    """Determines if a query is technical based on keywords."""
    technical_keywords = ["efficiency", "wattage", "voltage", "inverter", "LCOE", "compliance", "NEC", "photovoltaic", "grid-tied", "MPPT"]
    return any(re.search(rf"\b{kw}\b", query, re.IGNORECASE) for kw in technical_keywords)

def generate_response(user_input):
    """Generates AI response using Gemini API only for solar-related queries."""
    if not is_solar_related(user_input):
        return "I'm specialized in solar energy topics. Please ask something related to solar technology, installation, or market trends."
    
    query_type = "technical" if is_technical_query(user_input) else "non-technical"
    
    try:
        headers = {"Content-Type": "application/json"}
        prompt = f"Provide a {query_type} response related to solar energy: {user_input}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "safetySettings": [{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"}]
        }
        response = requests.post(f"{API_URL}?key={GEMINI_API_KEY}", json=payload, headers=headers)
        response_data = response.json()
        
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            ai_response = response_data['candidates'][0]['content']['parts'][0]['text'].replace("\n", " ").replace("**", "<b>").replace("**", "</b>")
            return ai_response
        else:
            logging.error(f"Unexpected API response format: {response_data}")
            return "I couldn't generate a response. Please try again."
    except Exception as e:
        logging.error(f"Error in LLM response: {str(e)}")
        return "I'm having trouble processing your request. Please try again."
