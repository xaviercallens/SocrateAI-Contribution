# Lean files cited by `certified_bao`

Collected from the ledger evidence blobs (`sources[].path` + `sha256`) and, where present, the auditor's `STATEMENT_LOCK.json`. `recorded` is the hash written when the claim was filed or locked; `current` is the hash of the file copied here. Upstream files (openai/math, openai/NavierStokesAndEuler, Lake packages) are listed with their hash and not redistributed; fetch them at the pinned commit. Where no hash was recorded (papers ED-03 to ED-08, written before hashes went into the ledger), the file is compared with the version last committed to AutoevolveAI before the Zenodo record was created; if they differ, that publication-time version is the one copied here. That commit is the best available proxy for what the paper compiled, not a recorded lock.

| file | via | recorded sha256 | status |
|---|---|---|---|
| `lean/formal_cert/BAOCert/Axioms.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (7e26b9cbc83a) |
| `lean/formal_cert/BAOCert/Core.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (04ad62f74250) |
| `lean/formal_cert/BAOCert/EdS.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (04ad62f74250) |
| `lean/formal_cert/BAOCert/Fit.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (04ad62f74250) |
| `lean/formal_cert/BAOCert/FitOm101.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (04ad62f74250) |
| `lean/formal_cert/BAOCert/Tampered.lean` | cited in the paper text (no hash recorded) | `-` | copied; identical to the version last committed before publication (04ad62f74250) |

Full hashes: `lean_manifest.json`. `tools/check_consistency.py` re-hashes every copied file.
