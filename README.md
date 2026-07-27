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
