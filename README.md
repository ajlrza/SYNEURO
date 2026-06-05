<p align="center">
  <img src="./animus.png" alt="Animus Logo" width="180" style="max-width:100%; height:auto;" />
</p>

# Animus Engine

> An event-driven, distributed HCI middleware for stateful, low-latency, and embodied AI agents.

<div align="center" style="display:inline-flex; gap:16px; align-items:center; background:#111; border:1px solid rgba(255,255,255,0.12); border-radius:18px; padding:16px 24px; box-shadow:0 12px 32px rgba(0,0,0,0.25);">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Typescript_logo_2020.svg/3840px-Typescript_logo_2020.svg.png" alt="TypeScript" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/FastAPI_logo.svg/3840px-FastAPI_logo.svg.png" alt="FastAPI" width="50" />
  <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/kafka-logo.png" alt="Kafka" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/3840px-Go_Logo_Blue.svg.png" alt="Go" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Groq_logo.svg/250px-Groq_logo.svg.png" alt="Groq" width="50" />
</div>

## Overview

Animus Engine is a high-performance Human-Computer Interaction (HCI) middleware designed to bridge stateless Large Language Models (LLMs) with dynamic, real-time environments. Operating as a decentralized cognitive nervous system, it handles the complex orchestration of temporal continuity (long-term memory persistence), affective computing (deterministic state machines), and high-throughput sensory data ingestion. 

By decoupling core application logic from the client interface, Animus provides an un-opinionated backend architecture suitable for both virtual agents (highly responsive interactive interfaces) and embodied AI systems (robotics, edge devices, and physical hardware control) where sub-millisecond coordination, state serialization, and minimal buffer bloat are structural requirements.

## Architecture & Core Systems

* **Custom IPC Bridge:** A slot-based IPC mechanism built to bypass HTTP/gRPC overhead, facilitating ultra-low latency serialization and routing of strict-typed telemetry and database queries across Go, Python, and TypeScript runtimes.
* **Event-Driven Messaging:** Utilizes Apache Kafka to ingest concurrent sensor/input data and decouple text/command generation from state persistence, ensuring strict event sequencing and scalable asynchronous processing under heavy I/O loads.
* **Low-Latency Streaming Pipeline:** Pipes chunked LLM tokens directly from upstream inference providers (e.g., Groq API) through the systems transport layer to the websocket client, enforcing tight conversational rhythm and minimal perceived latency.
* **Stateful Memory Management:** A concurrent, race-free persistence layer implemented in Go that actively queries, manages, and injects context windows and conversational history into the agent execution pipeline.
* **Dynamic Affective State Machine:** Replaces static system prompting with a deterministic runtime engine that calculates an agent’s internal operational variables (e.g., environmental uncertainty, internal system fatigue, or behavioral state shifts) in real-time, enforcing situational context awareness on every turn.

## Tech Stack

* **Systems Infrastructure & Memory:** Go
* **Inference Pipeline & Logic:** Python, FastAPI
* **Gateway Layer & WebSockets:** TypeScript, Node.js
* **Distributed Message Broker:** Apache Kafka
* **Low-Latency Hardware Inference:** Groq API (Llama Architecture)
