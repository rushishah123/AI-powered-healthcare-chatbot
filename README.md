# AI-powered Healthcare Chatbot

This project is a collection of small services that work together to power a healthcare chatbot. Think of your computer running many little helpers (containers) that talk to each other.

## How to run it

1. **Install Docker and Docker Compose**
   - Download and install Docker Desktop from the official website.
2. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd AI-powered-healthcare-chatbot
   ```
3. **Copy `.env.example` to `.env`**
   ```bash
   cp .env.example .env
   ```
   Fill in any values if needed.
4. **Build and start the helpers**
   ```bash
   docker-compose up --build
   ```
5. **Open the chatbot**
   - Visit [http://localhost:8501](http://localhost:8501) in your web browser.
6. **Talk to it**
   - Type a question or upload a file to see the chatbot work.
