# Real‑time Voice Fraud Detection

## Overview
This project presents a proof‑of‑concept **early‑warning system** for voice phishing (vishing). It simulates real‑time analysis of call audio by transcribing short chunks and classifying the evolving transcript to surface risk signals during the conversation.

## Motivation
Traditional fraud detection often runs **after** the call or relies on metadata, which is too late to protect victims. The goal here is to provide **in‑call** risk feedback.

## Methodology
- **Streaming simulation**: Audio is processed in **6‑second overlapping chunks** to mimic a live call.
- **ASR**: Whisper transcribes each chunk.
- **Classifier**: A fine‑tuned **mBERT** model analyzes the accumulated transcript to detect fraud intent.
- **Risk scoring**: A continuously updated risk score is shown; above **0.80** triggers a **HIGH RISK** alert.

## Data Strategy
Due to privacy restrictions on real English fraud calls, the project uses the **quanshiyun/anti_fraud_dataset** (Chinese). The model was trained on a **24k sample subset** to validate architecture feasibility.

## Results
- **ROC‑AUC**: **0.978**
- **Accuracy**: **91.7%**
- **Demo**: A Gradio interface updates transcript and risk level every few seconds, demonstrating real‑time viability.

## Conclusions
- **Feasibility**: Whisper + mBERT detects fraud intent in a file‑based real‑time simulation.
- **Early signals**: High‑risk indicators appear within the first **6–12 seconds** in many cases.
- **Limitations**: Real deployment requires target‑language call audio and testing on live VoIP streams.

## Future Work
1. **Live capture** from microphone/VoIP instead of file simulation.
2. **Sliding window** (e.g., last 30s) instead of full transcript accumulation.
3. **Localization** with English/Hebrew vishing datasets.

## Authors
- Daniel Drori
- Gal Aviv
