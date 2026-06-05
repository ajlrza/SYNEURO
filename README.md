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

## 📖 Overview

Animus Engine is a high-performance Human-Computer Interaction (HCI) middleware designed to bridge stateless Large Language Models (LLMs) with dynamic, real-time environments. It operates as the cognitive orchestration layer—handling temporal continuity (long-term memory), affective computing (state machines), and high-throughput sensory data ingestion. 

By decoupling core AI logic from the client interface, Animus provides an un-opinionated backend architecture. It is purpose-built for virtual agents and embodied AI (robotics, edge devices) where sub-millisecond coordination, deterministic state serialization, and minimal buffer bloat are structural requirements.

## ✨ Core Architecture

* **Custom IPC Bridge:** A slot-based Inter-Process Communication mechanism built to bypass HTTP/gRPC overhead. It routes strict-typed telemetry and database queries across Go, Python, and TypeScript runtimes with ultra-low latency.
* **Event-Driven Messaging (Kafka):** Ingests concurrent sensor/input data and decouples text generation from state persistence. This ensures strict event sequencing and scalable asynchronous processing under heavy I/O loads.
* **Low-Latency Streaming Pipeline:** Pipes chunked LLM tokens directly from upstream inference providers (e.g., Groq API) through the transport layer to the WebSocket client, enforcing tight conversational rhythm.
* **Stateful Memory Management (Go):** A concurrent, race-free persistence layer that actively manages and injects context windows and conversational history into the agent's execution pipeline.
* **Dynamic Affective State Machine:** Replaces static system prompting with a deterministic runtime engine. It calculates an agent’s internal variables (e.g., environmental uncertainty, fatigue, behavioral shifts) in real-time, enforcing situational awareness on every turn.

## 🛠️ Tech Stack

* **Systems Infrastructure & Memory:** Go
* **Inference Pipeline & Logic:** Python, FastAPI
* **Gateway Layer & WebSockets:** TypeScript, Node.js
* **Distributed Message Broker:** Apache Kafka
* **Low-Latency Hardware Inference:** Groq API (Llama Architecture)

---

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed on your host machine:
* [Docker](https://www.docker.com/) & Docker Compose (for Kafka/Zookeeper)
* [Go](https://go.dev/) (1.20+)
* [Python](https://www.python.org/) (3.10+)
* [Node.js](https://nodejs.org/) (18+)
* A valid [Groq API Key](https://groq.com/)

### Installation

**1. Clone the repository**
```bash
git clone [https://github.com/your-org/animus-engine.git](https://github.com/your-org/animus-engine.git)
cd animus-engine
```

**2. Start the Kafka Message Broker**
```bash
docker-compose up -d
```

**3. Set up environment variables**
```bash
cp .env.example .env
# Edit .env to add your GROQ_API_KEY and custom port configurations
```

**4. Spin up the microservices**
Run the core services concurrently using the provided Makefile:
```bash
make start-all
```
*(This will initialize the Go Memory Manager, Python Inference Pipeline, and TS Gateway).*

---

## 🔌 Usage Example: Connecting a Client

Once the engine is running, your edge device or front-end client can connect to the TypeScript Gateway via WebSocket to stream sensor telemetry and receive LLM tokens in real-time.

```javascript
// Example: Client-side connection to Animus Engine
const socket = new WebSocket('ws://localhost:8080/v1/stream');

socket.onopen = () => {
  console.log('Connected to Animus Neural Gateway');
  
  // Send sensory/context data to the engine
  const payload = {
    event_type: "sensor_input",
    timestamp: Date.now(),
    data: {
      user_proximity: 1.2, // meters
      ambient_noise_db: 45
    }
  };
  socket.send(JSON.stringify(payload));
};

// Stream chunked LLM response and affective state updates
socket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.type === 'token') {
    process.stdout.write(response.content);
  } else if (response.type === 'affective_state') {
    console.log(`\n[State Shift] Agent Alertness: ${response.state.alertness}`);
  }
};
```

## 🤝 Contributing
Contributions are welcome! Please review our [Contributing Guidelines](CONTRIBUTING.md) and ensure all PRs pass the strict-typing and latency benchmark tests.

## 📄 License
This project is licensed under the [MIT License](LICENSE).
