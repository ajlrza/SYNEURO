<p align="center">
  <img src="./Syneuro.png" alt="Syneuro Logo" width="180" style="max-width:100%; height:auto;" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
</p>

## 📖 Overview

Syneuro is an LLM Persona Architecture designed to simulate complex emotions via Python & PyTorch

## Architecture

* **`SALNetwork` (Salience):** The core router. It actively monitors incoming telemetry and decides whether the emotion should be in a resting state or active.
* **`CENetwork` (Central Executive):** Handles high-level reasoning, complex problem solving, tool execution, and goal-directed behavior influenced by emotion.
* **`LIMNetwork` (Limbic):** The affective state machine powered by a custom, mini Recurrent Looped Transformer (RLT). Responsible for the internal mood, emotional responses, and assigns emotional weight to memory formation randomness.
