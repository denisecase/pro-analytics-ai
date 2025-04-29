# SPACE.md

# Storage and Processing Space Requirements for pro-analytics-ai

This project begins with a **small, curated training set (~100 KB)** based on the [pro-analytics-01](https://github.com/denisecase/pro-analytics-01) educational materials.

However, building a functioning LLM brain from even this small corpus requires substantial memory, disk space, and supporting environment setup.

---

## Model Growth Funnel: How 100 KB Grows to 300 GB

| Step / Artifact | Full Precision Model | 8-bit Quantized Model | 4-bit Quantized Model |
|:----------------|:---------------------|:----------------------|:----------------------|
| Raw Text Corpus | 100 KB | 100 KB | 100 KB |
| Tokenized Dataset | ~200 KB | ~200 KB | ~200 KB |
| Training Dataset (Packed Format) | ~1 MB | ~1 MB | ~1 MB |
| Python Environment (transformers, torch, etc.) | ~5 GB | ~5 GB | ~5 GB |
| Extra Packages (quantization, bitsandbytes, etc.) | None | ~0.5 GB | ~1 GB |
| Model Architecture Initialization (RAM only) | Tiny | Tiny | Tiny |
| Training Logs, Caches, Temps | ~0.5–1 GB | ~0.5–1 GB | ~0.5–1 GB |
| Gradient Checkpoints (Optional) | 10–50 GB | 5–20 GB | 2–10 GB |
| Validation Snapshots (Optional) | 50–300 GB | 20–80 GB | 10–40 GB |
| Final Trained Model (Weights) | ~300 GB | ~80–90 GB | ~35–45 GB |
| Optimizer State Files (Optional) | ~100–200 GB | ~30–50 GB | ~15–25 GB |

---

## Space Cleanup Guidance

| Temporary Artifact | Delete After Training? | Reason |
|:-------------------|:------------------------|:-------|
| Training Logs, Caches | Yes | Saves small space, cleans working directory |
| Gradient Checkpoints | Yes (unless retraining) | Large; safe to remove for inference |
| Validation Snapshots | Yes (keep best model only) | Very large; only best needed |
| Optimizer States | Yes (if only doing inference) | Large; not needed for just answering questions |

---

## Disk Space Summary

| Phase | Estimated Total Disk Usage |
|:------|:---------------------------|
| After Training Full Model | ~455–805 GB |
| After Quantizing 8-bit Model | ~135–230 GB |
| After Quantizing 4-bit Model | ~65–125 GB |

Final disk needs depend heavily on:
- How many snapshots/checkpoints you save
- How much intermediate junk you delete
- Whether you quantize to 8-bit or 4-bit

---

# Short Visual (Small up to Huge then back down to just Very Large)

```plaintext
100 KB (Raw Text)
 → 1 MB (Tokenized + Packed)
 → 5 GB (Libraries Installed)
 → 300+ GB (Model + Training Garbage)
 → (After Quantization and Cleanup)
 → 40–90 GB (Usable 4-bit or 8-bit Model)
```

## Final Notes

- RAM minimum: 32 GB (64 GB preferred)
- Disk minimum: 1 TB SSD recommended
- Python version: 3.11 recommended
- Best environment: Ubuntu 20.04+ (or WSL2 on Windows 11)
- Optional but helpful: GPU (NVIDIA T4, A10, RTX 3060+)

Even starting with a tiny amount of text, growing a working LLM system requires **serious hardware** and **significant storage**.
