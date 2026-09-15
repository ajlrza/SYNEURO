<p align="center">
  <img src="./Syneuro.png" alt="Syneuro Logo" width="180" style="max-width:100%; height:auto;" />
</p>

# Syneuro 
> 
<div align="center" style="display:inline-flex; gap:16px; align-items:center; background:#111; border:1px solid rgba(255,255,255,0.12); border-radius:18px; padding:16px 24px; box-shadow:0 12px 32px rgba(0,0,0,0.25);">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/Python-logo.png" alt="Python" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Pytorch_logo.png" alt="PyTorch" width="50" />
</div>
## 📖 Overview

Syneuro is an LLM Persona Architecture designed to simulate complex emotions via Python & PyTorch

## Architecture

* **`SALNetwork` (Salience):** The core router. It actively monitors incoming telemetry and decides whether the emotion should be in a resting state or active
* **`CENetwork` (Central Executive):** Handles high-level reasoning, complex problem solving, tool execution, and goal-directed behavior influenced by emotion.
* **`LIMNetwork` (Limbic):** The affective state machine powered by a custom, mini Recurrent Looped Transformer (RLT). Responsible for the  internal mood, emotional responses, and assigns emotional weight to memory formation randomness.
