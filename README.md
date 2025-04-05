# 🧠 Famous Personality Guessing Game

A Python-based console game developed during a **Masterschool Hackathon** by a team of four:

- Ehsan Mehrali  
- Jürgen Kiensberger  
- Robert Pluntke  
- Yevheniia Belohai  


- Mentor : Florian Vogel

In this game, the player tries to guess the name of a famous person. Wikipedia articles are used as the source of truth, and AI-generated hints are provided via Gemini (Google Generative AI). The game is entirely text-based and runs in the terminal.

---

## 🚀 Features

- Console-based guessing game
- Wikipedia integration to select famous people
- Gemini AI generates five smart hints based on the article's topic
- Colorful text effects with `colorama`
- Background music with `pygame`
- Fuzzy matching to evaluate answers

---

# 🛠 Requirements

Install the required libraries with pip:

```bash
pip install pygame wikipedia-api thefuzz google-generativeai colorama
```

## 🚨 Important Setup Steps (Please Read!)

#### 1 - Run Configuration in PyCharm to make sure the game works properly in the PyCharm terminal:

- Right-click on main.py and select Modify Run Configuration.
- Click on Modify Options.
- From the dropdown, check Emulate terminal in output console.
- Click Apply. 
###
#### 2 - Obtain and Set Your API Key
To use Gemini for clue generation, you’ll need a personal API Key from Google :
#### 👉 Get your free API key here:
#### https://aistudio.google.com/app/apikey

Once you have the key, open main.py and go to line 61, then replace the placeholder with your key:
```
genai.configure(api_key="YOUR_API_KEY")
```
---

# 🧠 About the Game
#### Guess the Celebrity is an interactive console game where players try to identify celebrities based on hints extracted from their Wikipedia pages.
#### Hints are dynamically generated using Google Gemini.
#### Each round includes 5 clues related to the person's profession, achievements, or life events.
#### The game uses wikipedia-api to fetch data and thefuzz to evaluate the correctness of the guesses.

---
# 📜 Game Rules
### To learn how to play, navigate to the "Show Rules" section in the main game menu.


---