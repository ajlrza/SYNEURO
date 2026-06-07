<p align="center">
  <img src="./Syneuro.png" alt="Syneuro Logo" width="180" style="max-width:100%; height:auto;" />
</p>

# Syneuro Engine
> 
<div align="center" style="display:inline-flex; gap:16px; align-items:center; background:#111; border:1px solid rgba(255,255,255,0.12); border-radius:18px; padding:16px 24px; box-shadow:0 12px 32px rgba(0,0,0,0.25);">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/FastAPI_logo.svg/3840px-FastAPI_logo.svg.png" alt="FastAPI" width="50" />
  <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/kafka-logo.png" alt="Kafka" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/3840px-Go_Logo_Blue.svg.png" alt="Go" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/Python-logo.png" alt="Python" width="50" />
</div>

## 📖 Overview

Syneuro Engine is a high-performance distributed Affective Computing (AFC) middleware designed to bridge stateless Foundation Models (LLMs, VLMs, and audio models) with dynamic, real-time environments.

Purpose-built for virtual agents and embodied AI (robotics, edge devices), Syneuro handles temporal continuity, affective computing, and high-throughput sensory data ingestion with sub-millisecond coordination and deterministic state serialization.

## Cognitive Architecture

At the core of the Python inference pipeline is the `agentBrain`, which orchestrates LLM calls and state updates across seven distinct sub-networks, mimicking human cognitive processing:

* **`SALNetwork` (Salience):** The core router. It actively monitors incoming telemetry and decides whether the agent should be in a resting state (`DFM`) or active processing state (`CEN`).
* **`CENetwork` (Central Executive):** Handles high-level reasoning, complex problem solving, tool execution, and goal-directed behavior.
* **`DFMNetwork` (Default Mode):** The agent's baseline state. Handles internal monologue, memory consolidation, and background context summarization when no immediate user input is detected.
* **`LIMNetwork` (Limbic):** The affective state machine. Regulates the agent's internal mood, emotional responses, and assigns emotional weight to memory formation.
* **`SENNetwork` (Sensorimotor):** Manages outbound communication processing, formatting text, speech syntax, and physical hardware commands.
* **`VISNetwork` (Visual):** Dedicated to processing visual inputs, computer vision arrays, and spatial awareness feeds.
* **`VENNetwork` (Ventral Attention):** The interrupt handler. Manages sudden environmental shifts, unexpected attention grabs, and introduces necessary behavioral randomness.

## Systems Infrastructure

* **Custom IPC Bridge:** A slot-based Inter-Process Communication mechanism bypassing HTTP/gRPC overhead, routing telemetry across Go, Python, and TypeScript with ultra-low latency.
* **Swappable Event Broker (Asyncio / Kafka):** Built on the Strategy Pattern, the messaging layer is environment-configurable. It utilizes Python's native `asyncio.Queue` and Go channels for ultra-low latency, zero-overhead local MVP deployments, and seamlessly hot-swaps to Apache Kafka or Redpanda for distributed, high-throughput hardware.
* **Stateful Memory Management (Go):** A concurrent, race-free persistence layer that actively manages and injects context windows into the cognitive networks.
* **Low-Latency Streaming Pipeline:** Pipes chunked LLM tokens directly from upstream inference (e.g., Groq API) through the transport layer to the WebSocket client.

```text
[User App / Digital Avatar / Webcams]
       │ (WebRTC / WebSockets: zero head-of-line blocking)
       ▼
  [FastAPI Server]    ---> Handles ultra-low latency A/V routing & VAD
       │
       ▼
  [LiveKit Server]    ---> Handles ultra-low latency A/V routing & VAD
       │
       ▼
[Python Agent Worker] ---> (Pipecat Orchestrator & Cognitive Networks)
       │                   
       ├─► [OpenCV / Local SLM] ---> Extracts context & calculates Affective State
       ├─► [Groq API / LLM]     ---> Main Foundational Model (Reasoning Hub)
       │
       ▼
[Event Broker Interface] ---> (Configurable via .env: Native Asyncio Queue OR Kafka)
       │                      (Decouples sensory stream from state persistence)
       ▼
   [Go Engine]        ---> Handles long-term memory, state serialization, and context injection
