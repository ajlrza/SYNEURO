# SYNAPSE


### 
The SYNAPSE architecture utilizes dual-cache mechanism for hot, live, application
instance as the AI agent continuously interact with the user. This ensures that strong
short-term memory is enforced, along with complexity provided by the hilbert space. 
It balances the native normal caching mechanism for hardware compliance and the 
quantum association for comlexity.

A middleware is also used that acts as the "transport" layer for the agent's brain
passing down the memories all the way to the Neo4j Graph DB for human-like long-term memory.


┌───────────────────────────────── SYSTEM RAM / GPU VRAM ─────────────────────────────────┐
│                                                                                         │
│  ┌───────────────────────────────┐               ┌───────────────────────────────┐      │
│  │   HALF HILBERT CACHE (Cⁿ)     │ ◄───────────► │   HALF NORMAL CACHE (Rⁿ)      │      │
│  │  • Continuous wave function   │  Interference │  • Discrete token IDs / text  │      │
│  │  • Complex numbers & phases   │   & Mapping   │  • Static vector embeddings   │      │
│  │  • Quantum Emotions / Flow    │               │  • Recent raw chat history    │      │
│  └───────────────┬───────────────┘               └───────────────┬───────────────┘      │
└──────────────────┼───────────────────────────────────────────────┼──────────────────────┘
                   │                                               │
                   ▼                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                              APPLICATION MIDDLEWARE                                     │
│    • Handles the measurement (collapse) of the Hilbert space into discrete states.      │
│    • Pairs the collapsed quantum state values with the raw text/normal embeddings.      │
└──────────────────────────────────────────┬──────────────────────────────────────────────┘
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                   NEO4J GRAPH DB                                        │
│          • Nodes: Persistent text entities, normal embeddings, and anchors.             │
│          • Edges: Entanglement strengths, phase relationships, and causal links.        │
└─────────────────────────────────────────────────────────────────────────────────────────┘
