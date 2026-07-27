## SYSTEMS ARCHITECTURE

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
       ├─► [7 Network Modules] ---> Main Affective Computing Engine
       ├─► [RL-Policy] ---> Neural Spike Reward System
       ├─► [User-defined RAG] ---> Context-awareness
       ├─► [Groq API / LLM]   ---> Main Foundational Model (Reasoning Hub)
       ├─► [Transport module] ---> Streamlines short-term memory to long-term memory from application cache [interaction]
       ▼
[Event Broker Interface] ---> (Configurable via .env: Native Asyncio Queue OR Kafka)
       │                      (Decouples sensory stream from state persistence)
       ▼
   [Go Engine]        ---> Handles long-term memory, state serialization, and context injection
```

### LIM [Limbic Network]

```text
[Incoming App Output / Sensory Data Dict]
                       │
                       ▼
 ╔═════════════════════════════════════════════════════════════════════════════════╗
 ║                                LIMNetwork Class                                 ║
 ║                                                                                 ║
 ║  ┌───────────────────────────────────────────────────────────────────────────┐  ║
 ║  │ 1. thalamus(sensory_data)                                                 │  ║
 ║  │    Routes incoming data by type and triggers the main processing chain.   │  ║
 ║  │                                                                           │  ║
 ║  │    [str] ────────► SensoryOutput.Text                                     │  ║
 ║  │    [bytearray] ──► SensoryOutput.Audio                                    │  ║
 ║  │    [ndarray] ────► SensoryOutput.Video                                    │  ║
 ║  │         │                 │                 │                             │  ║
 ║  └─────────┼─────────────────┼─────────────────┼─────────────────────────────┘  ║
 ║            │                 │                 │                                ║
 ║            ▼                 ▼                 ▼                                ║
 ║  ┌───────────────────────────────────────────────────────────────────────────┐  ║
 ║  │ 2. amygdala(sensor_data)                                                  │  ║
 ║  │    The emotional processing core.                                         │  ║
 ║  │                                                                           │  ║
 ║  │  A. extract_affective_state()                                             │  ║
 ║  │     └──► Sends data to [Groq LLM] via client.chat.completions             │  ║
 ║  │     └──► Returns JSON payload: [Valence, Arousal, Dominance] (VAD)        │  ║
 ║  │                                                                           │  ║
 ║  │  B. emotion.map_vad_to_angles(VAD)                                        │  ║
 ║  │     └──► Passed into the [QuantumEmotion] engine                          │  ║
 ║  │     └──► VAD mapped to Theta, Phi, and r                                  │  ║
 ║  │     └──► Calculates the 3D Bloch Vector (x, y, z)                         │  ║
 ║  │                                                                           │  ║
 ║  │  C. emotion.compute_emotion_transition()                                  │  ║
 ║  │     └──► Evaluates current emotional_state against affective_state        │  ║
 ║  │     └──► Asynchronously updates the state_vector (emotional state)        │  ║
 ║  │                                                                           │  ║
 ║  │  D. cen.get_working_memory()                                              │  ║
 ║  │     └──► Iterates over stimulus_dict (Valence, Arousal, Dominance)        │  ║
 ║  │     └──► Asynchronously forms long-term memories via CEN                  │  ║
 ║  │                                                                           │  ║
 ║  │  E. update_emotion_matrix()                                               │  ║
 ║  │     └──► Triggered if the resulting Bloch vector is non-zero              │  ║
 ║  └─────────┬─────────────────────────────────────────────────────────────────┘  ║
 ║            │                                                                    ║
 ║            ▼                                                                    ║
 ║  ┌───────────────────────────────────────────────────────────────────────────┐  ║
 ║  │ 3. Emotion Matrix Dictionary                                              │  ║
 ║  │    Maps the Bloch vector coordinates (x, y, z) to human emotions.         │  ║
 ║  │                                                                           │  ║
 ║  │  ├─ X-Axis ──► Positive: Surprise      | Negative: Fear                   │  ║
 ║  │  ├─ Y-Axis ──► Positive: Zeal          | Negative: Calm / Angry           │  ║
 ║  │  └─ Z-Axis ──► Positive: Happy         | Negative: Sad / Depressed        │  ║
 ║  └───────────────────────────────────────────────────────────────────────────┘  ║
 ║                                                                                 ║
 ║  ┌───────────────────────────────────────────────────────────────────────────┐  ║
 ║  │ 4. Thalamus Post-Processing (Attention Routing)                           │  ║
 ║  │    After amygdala processing concludes for a sensory input.               │  ║
 ║  │                                                                           │  ║
 ║  │  A. check_attention()                                                     │  ║
 ║  │     └──► Takes updated emotion.state_vector, timestamp, and decay rate    │  ║
 ║  │     └──► Calls cen.attention_check() to generate an attentionGate         │  ║
 ║  │                                                                           │  ║
 ║  │  B. cen.push_attention()                                                  │  ║
 ║  │     └──► Asynchronously pushes the attentionGate and sensor_data to CEN   │  ║
 ║  └───────────────────────────────────────────────────────────────────────────┘  ║
 ╚═════════════════════════════════════════════════════════════════════════════════╝
```

### CEN [Central Executive Network] & SAL [Salience Network]

```text
[Raw Environmental Data]             [Agent Output / Multimodal Data]
          │                                         │
          ▼                                         ▼
 ╔═════════════════════════╗          ╔══════════════════════════════╗
 ║ SALNetwork (Salience)   ║          ║ CENNetwork (Central Exec.)   ║
 ║                         ║          ║                              ║
 ║ 1. Ingests raw data     ║          ║ 1. Init & Filter Modalities  ║
 ║ 2. signal_network() ────╫──┐       ║    (Text, Audio, Video, etc.)║
 ║                         ║  │       ║                              ║
 ║ 3. divert_attention()   ║  │       ║ 2. Text Processing           ║
 ║    └─ Routes Memory     ║  │       ║    └─ __handle_text_output() ║
 ║                         ║  │       ║                              ║
 ║ 4. store_attention() ───╫──┼──────►║ 3. PPC (Parietal Cortex)     ║
 ╚══════════╦══════════════╝  │       ║    └─ Fuses sensory spikes   ║
            │                 │       ║                              ║
            ▼                 │       ║ 4. Dorsolateral Prefrontal   ║
 ╔═════════════════════════╗  │       ║    ├─ push_attention()       ║
 ║       RAG Module        ║◄─┘       ║    └─ attention_check()      ║
 ║                         ║          ╚══════════════════════════════╝
 ║ ├─ context_rag()        ║ 
 ║ ├─ add_memory()         ║
 ║ └─ add_temp_memory()    ║
 ╚═════════════════════════╝
```


### SYNAPSE

The SYNAPSE architecture utilizes dual-cache mechanism for hot, live, application
instance as the AI agent continuously interact with the user. This ensures that strong
short-term memory is enforced, along with complexity provided by the hilbert space. 
It balances the native normal caching mechanism for hardware compliance and the 
quantum association for comlexity.

A middleware is also used that acts as the "transport" layer for the agent's brain
passing down the memories all the way to the Neo4j Graph DB for human-like long-term memory.

```text
┌───────────────────────────────── SYSTEM RAM / GPU VRAM ─────────────────────────────────┐
│                                                                                         │
│     ┌───────────────────────────────┐                 ┌───────────────────────────────┐ │
│     │ HALF HILBERT CACHE (Cⁿ)       │                 │ HALF NORMAL CACHE (Rⁿ)        │ │
│     │ • Continuous wave function    │  Interference   │ • Discrete token IDs / text   │ │
│     │ • Complex numbers & phases    │  ───────────►   │ • Static vector embeddings    │ │
│     │ • Quantum Emotions / Flow     │   & Mapping     │ • Recent raw chat history     │ │
│     └───────────────┬───────────────┘                 └───────────────┬───────────────┘ │
│                     │                                                 │                 │
└─────────────────────┼─────────────────────────────────────────────────┼─────────────────┘
                      │                                                 │
                      ▼                                                 ▼
      ┌─────────────────────────────────────────────────────────────────────────────────┐
      │ APPLICATION MIDDLEWARE                                                          │
      │ • Handles the measurement (collapse) of the Hilbert space into discrete states. │
      │ • Pairs the collapsed quantum state values with the raw text/normal embeddings. │
      └───────────────────────────────────┬─────────────────────────────────────────────┘
                                          │
                                          ▼
      ┌─────────────────────────────────────────────────────────────────────────────────┐
      │ NEO4J GRAPH DB                                                                  │
      │ • Nodes: Persistent text entities, normal embeddings, and anchors.              │
      │ • Edges: Entanglement strengths, phase relationships, and causal links.         │
      └─────────────────────────────────────────────────────────────────────────────────┘
```
