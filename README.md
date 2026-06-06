<p align="center">
  <img src="./Syneuro.png" alt="Syneuro Logo" width="180" style="max-width:100%; height:auto;" />
</p>

# Syneuro Engine
> 
<div align="center" style="display:inline-flex; gap:16px; align-items:center; background:#111; border:1px solid rgba(255,255,255,0.12); border-radius:18px; padding:16px 24px; box-shadow:0 12px 32px rgba(0,0,0,0.25);">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/FastAPI_logo.svg/3840px-FastAPI_logo.svg.png" alt="FastAPI" width="50" />
  <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/kafka-logo.png" alt="Kafka" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/3840px-Go_Logo_Blue.svg.png" alt="Go" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Groq_logo.svg/250px-Groq_logo.svg.png" alt="Groq" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/Python-logo.png" alt="Python" width="50" />
</div>

## 📖 Overview

Syneuro Engine is a high-performance distributed Affective Computing (AFC) middleware designed to bridge stateless Foundation Models (LLMs, VLMs, and audio models) with dynamic, real-time environments.

Purpose-built for virtual agents and embodied AI (robotics, edge devices), Animus handles temporal continuity, affective computing, and high-throughput sensory data ingestion with sub-millisecond coordination and deterministic state serialization.

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
* **Event-Driven Messaging (Kafka):** Ingests concurrent sensor/input data and decouples text generation from state persistence, ensuring strict event sequencing.
* **Stateful Memory Management (Go):** A concurrent, race-free persistence layer that actively manages and injects context windows into the cognitive networks.
* **Low-Latency Streaming Pipeline:** Pipes chunked LLM tokens directly from upstream inference (e.g., Groq API) through the transport layer to the WebSocket client.

[User App / Webcams]
       │ (WebRTC connection: UDP, zero head-of-line blocking)
       ▼
  [LiveKit Server]    ---> Handles ultra-low latency A/V routing & VAD
       │
       ▼
[Python Agent Worker] ---> Pipecat 
       │                   
       │
       ├─► [OpenCV] ---> Extracts facial points & visual context
       ├─► [AI Model]  ---> Main AI model 
       │
       ▼
 [Kafka State Topic]  ---> (Decoupled stream buffer for memory & state)
       │
       ▼
   [Go Engine]        ---> Handles long-term memory, state serialization, and context injection


### Prerequisites
* [Docker](https://www.docker.com/) & Docker Compose
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

**2. Start the Message Broker & Microservices**
```bash
docker-compose up -d
cp .env.example .env
make start-all
```

---

## 🔌 Usage Examples

### 1. Backend: Initializing the Cognitive Architecture
The core logic resides in the Python FastAPI layer, where the `agentBrain` is instantiated to process incoming Kafka events.

```python
# inference/brain.py
from networks import DFMNetwork, CENetwork, SALNetwork, SENNetwork, VISNetwork, LIMNetwork, VENNetwork

class AgentBrain:
    def __init__(self):
        # Configure the cognitive networks
        self.DFM = DFMNetwork() # Default Mode (Idle/Memory)
        self.CEN = CENetwork()  # Executive (Reasoning)
        self.SAL = SALNetwork() # Salience (Manager/Router)
        self.SEN = SENNetwork() # Sensorimotor (Communication)
        self.VIS = VISNetwork() # Visual (Observation)
        self.LIM = LIMNetwork() # Limbic (Affective/Mood)
        self.VEN = VENNetwork() # Ventral (Interrupts/Randomness)

    async def process_stimulus(self, event_payload):
        # Salience network decides which system handles the input
        active_network = self.SAL.evaluate(event_payload)
        response = await active_network.execute(event_payload, mood_state=self.LIM.current_state)
        return self.SEN.format_output(response)
```

### 2. Edge Device / Front-End: Streaming Telemetry
Connect to the TypeScript Gateway via WebSocket to send sensory data and receive cognitive output.

```javascript
// client.js
const socket = new WebSocket('ws://localhost:8080/v1/stream');

socket.onopen = () => {
  // Trigger the VENNetwork (Unexpected stimulus) or VISNetwork
  const payload = {
    event_type: "visual_interrupt",
    timestamp: Date.now(),
    data: { user_entered_frame: true }
  };
  socket.send(JSON.stringify(payload));
};

socket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.type === 'token') {
    process.stdout.write(response.content);
  } else if (response.type === 'limbic_update') {
    console.log(`\n[Limbic Shift] Agent Mood: ${response.state.mood}`);
  }
};
```

## 🤝 Contributing
Contributions to network architectures (specifically expanding `CENetwork` tool-use or `LIMNetwork` emotional heuristics) are highly encouraged. Please review our [Contributing Guidelines](CONTRIBUTING.md).

## 📄 License
This project is licensed under the [MIT License](LICENSE).
