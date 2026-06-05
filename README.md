<p align="center">
  <img src="./Kanojo2D_Logo.png" alt="Kanojo2D Logo" width="180" style="max-width:100%; height:auto;" />
</p>

# Animus Engine

> A full-stack conversational AI application driven by a custom, polyglot backend architecture.

<div align="center" style="display:inline-flex; gap:16px; align-items:center; background:#111; border:1px solid rgba(255,255,255,0.12); border-radius:18px; padding:16px 24px; box-shadow:0 12px 32px rgba(0,0,0,0.25);">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Typescript_logo_2020.svg/3840px-Typescript_logo_2020.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail" alt="TypeScript" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/FastAPI_logo.svg/3840px-FastAPI_logo.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail" alt="FastAPI" width="50" />
  <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/kafka-logo.png" alt="Kafka" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/3840px-Go_Logo_Blue.svg.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail" alt="Go" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Groq_logo.svg/250px-Groq_logo.svg.png?_=20240313080133" alt="Groq" width="50" />
</div>

## Overview

Animus Engine is an interactive, cross-platform full-stack application that leverages advanced LLMs and an event-driven architecture to create highly responsive virtual agents. Powered by a custom polyglot backend (TypeScript, Python, Go), the engine seamlessly blends low-latency dialogue generation, persistent stateful memory, and dynamic emotional modeling to deliver a deeply interactive and lifelike user experience.

## Features

* **Polyglot Microservice Architecture:** Utilizes a custom, slot-based Inter-Process Communication (IPC) bridge to reliably route complex data and database queries between Go, Python, and TypeScript services.
* **Persona-Driven AI:** Engage with dynamic virtual assistants engineered for nuanced, personality-rich interactions.
* **Immersive User Interface:** Features a visual novel-inspired frontend with rich atmospheric design and dynamic real-time text streaming (typewriter-style rendering) for natural pacing.
* **Persistent Stateful Memory:** Conversation history and contextual data are saved and loaded via strictly-typed database interfaces, allowing long-term continuity across sessions.
* **Customizable Behavioral Profiles:** Supports multiple distinct agent personas, enabling varied conversational styles, adaptive moods, and unique contextual scenarios.
* **Dynamic Emotional Modeling:** The system simulates real-time emotional shifts and situational events (e.g., fatigue, frustration, or spontaneous mood changes), requiring the user to adapt their conversational approach.
* **Responsive Design:** Fully optimized for fluid performance across both mobile and desktop environments.
* **Intuitive Dashboard:** Streamlined UI with quick-access controls for session history, persona management, and application settings.

## Tech Stack

* TypeScript
* FastAPI
* Kafka
* Go
* Groq
