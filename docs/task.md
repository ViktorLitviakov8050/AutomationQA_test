# ✅ Plan for AQA Home Test Implementation

## 📁 Project Setup (Both WAP & API tests)
- [ ] Create two separate GitHub repositories:
  - `aqa-wap-test`
  - `aqa-api-test`
- [ ] Initialize each repo with:
  - `.gitignore` (Python + Pytest + IDE)
  - `README.md`
  - Virtual environment (`venv`)
- [ ] Install dependencies:
  - `selenium`
  - `pytest`
  - `requests`
  - `pytest-html` (optional)
  - `python-dotenv` (optional for config management)

---

## 📱 Part 1: WAP (Web App) Testing Plan

### ✅ Objective:
Automate a mobile web scenario on [https://twitch.tv](https://twitch.tv) using Selenium and Chrome mobile emulator.

### 📋 Checklist:
- [ ] Set up Chrome mobile emulation in Selenium WebDriver
- [ ] Navigate to Twitch homepage
- [ ] Click the search icon
- [ ] Type **"StarCraft II"** into the search bar
- [ ] Scroll down twice
- [ ] Click on a streamer
- [ ] Wait for full page load
- [ ] Handle modal or pop-up (if present)
- [ ] Take a screenshot of the loaded streamer page
- [ ] Add error handling and logging
- [ ] Wrap all steps in a Pytest test case
- [ ] (Optional) Create a Page Object Model (POM) structure

### 📤 Delivery:
- [ ] Add a **GIF** of the test running locally in `README.md`
- [ ] (Optional) Add a short architecture overview of your test structure
- [ ] Push to GitHub & share repo link

---

## 🌐 Part 2: REST API Testing Plan

### ✅ Objective:
Write 2+ test cases using either:
- `https://poetrydb.org`
- `https://catfact.ninja/facts`

### 📋 Checklist:
- [ ] Choose one API (PoetryDB or Cat Facts)
- [ ] Write 2 or more test cases:
  - Include clear **test steps**
  - Define **expected results**
  - Define how you will **validate** the results (e.g., response code, keys, data types, content)
- [ ] Use `pytest` for API testing
- [ ] (Optional) Use `pytest.mark.parametrize` for multiple inputs

### 📤 Delivery:
- [ ] Create markdown table in `README.md` showing:
  - Test Step | Expected Result | Validation Approach
- [ ] Explain *why* you chose each validation method
- [ ] Push to GitHub & share repo link

---

## 🧠 Pro Tips (for the interview)
- Structure your code clearly — use folders like `/tests`, `/pages`, or `/utils`.
- Add comments and docstrings — especially for tricky logic.
- Be ready to explain **why** you chose certain tools or patterns (e.g., Pytest over unittest).
- Commit often with meaningful messages.