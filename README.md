<p align="center">
  <img src="./Animus.png" alt="Animus Logo" width="180" style="max-width:100%; height:auto;" />
</p>

# Animus Engine

> An event-driven, polyglot backend for stateful and low-latency AI agents.

<div align="center" style="display:inline-flex; gap:16px; align-items:center; background:#111; border:1px solid rgba(255,255,255,0.12); border-radius:18px; padding:16px 24px; box-shadow:0 12px 32px rgba(0,0,0,0.25);">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Typescript_logo_2020.svg/3840px-Typescript_logo_2020.svg.png" alt="TypeScript" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/FastAPI_logo.svg/3840px-FastAPI_logo.svg.png" alt="FastAPI" width="50" />
  <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/kafka-logo.png" alt="Kafka" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/3840px-Go_Logo_Blue.svg.png" alt="Go" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Groq_logo.svg/250px-Groq_logo.svg.png" alt="Groq" width="50" />
</div>

## Overview

Animus Engine is a distributed backend designed to manage state, memory, and fast inference for AI agents. It uses a polyglot microservice architecture (Go, Python, TypeScript) connected by Kafka and a custom IPC bridge. 

## Architecture & Core Systems

* **Custom IPC Bridge:** Built a slot-based IPC mechanism to bypass HTTP overhead, routing strict-typed data and database queries quickly between Go, Python, and TypeScript.
* **Event-Driven Messaging:** Uses Apache Kafka to decouple text generation from state updates, ensuring strict event ordering and scalable asynchronous processing.
* **Low-Latency Streaming:** Pipes chunked LLM responses from the Groq API through the backend to the client via WebSockets with minimal buffer bloat.
* **Stateful Memory Management:** Handles concurrent database read/writes to persist long-term conversation history and context without race conditions.
* **Dynamic State Machine:** Replaces static prompting with a deterministic engine that calculates an agent's internal state (e.g., mood shifts, fatigue) in real time and injects it into the execution context.

## Tech Stack

* **Systems & Memory:** Go
* **Inference & Logic:** Python, FastAPI
* **Gateway & WebSockets:** TypeScript
* **Message Broker:** Apache Kafka
* **LLM Inference:** Groq API
