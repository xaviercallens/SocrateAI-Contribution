# Lean files cited by `triangular_riesz`

Collected from the ledger evidence blobs (`sources[].path` + `sha256`) and, where present, the auditor's `STATEMENT_LOCK.json`. `recorded` is the hash written when the claim was filed or locked; `current` is the hash of the file copied here. Upstream files (openai/math, openai/NavierStokesAndEuler, Lake packages) are listed with their hash and not redistributed; fetch them at the pinned commit. Where no hash was recorded (papers ED-03 to ED-08, written before hashes went into the ledger), the file is compared with the version last committed to AutoevolveAI before the Zenodo record was created; if they differ, that publication-time version is the one copied here. That commit is the best available proxy for what the paper compiled, not a recorded lock.

| file | via | recorded sha256 | status |
|---|---|---|---|
| `lean/formal_cert/Triangular/AnyDensity.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (63b24aaf9802) |
| `lean/formal_cert/Triangular/Axioms.lean` | cited in the paper text (no hash recorded) | `-` | copied AT PUBLICATION COMMIT 9eb1773f0e7b (the file changed later; HEAD sha256 ba2ec76ae5acd245... differs) |
| `lean/formal_cert/Triangular/Riesz.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (8912d764bcfb) |
| `lean/formal_cert/Triangular/RieszFinite.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (4d5a6b3f1296) |

Full hashes: `lean_manifest.json`. `tools/check_consistency.py` re-hashes every copied file.
