# Lean files cited by `p2_certified_zero_point`

Collected from the ledger evidence blobs (`sources[].path` + `sha256`) and, where present, the auditor's `STATEMENT_LOCK.json`. `recorded` is the hash written when the claim was filed or locked; `current` is the hash of the file copied here. Upstream files (openai/math, openai/NavierStokesAndEuler, Lake packages) are listed with their hash and not redistributed; fetch them at the pinned commit. Where no hash was recorded (papers ED-03 to ED-08, written before hashes went into the ledger), the file is compared with the version last committed to AutoevolveAI before the Zenodo record was created; if they differ, that publication-time version is the one copied here. That commit is the best available proxy for what the paper compiled, not a recorded lock.

| file | via | recorded sha256 | status |
|---|---|---|---|
| `lean/formal_cert/Programmes/ZeroPoint/Basic.lean` | STATEMENT_LOCK.json | `7d59f1817767ae64...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/ZeroPointCert/Basic.lean` | STATEMENT_LOCK.json | `0241b6afa500e46a...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/ZeroPointCert/Controls.lean` | STATEMENT_LOCK.json | `2e95e21b70af3b4a...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/ZeroPointCert/RejectA2.lean` | STATEMENT_LOCK.json | `ab0f5f297b0a24ba...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/ZeroPointCert/RejectTampered.lean` | STATEMENT_LOCK.json | `02f6930b22e47d7c...` | copied; sha256 matches record |
| `lean/papers/p2_certified_zero_point/data/lean/Basic.lean` | ledger evidence | `0241b6afa500e46a...` | copied; sha256 matches record |
| `lean/papers/p2_certified_zero_point/data/lean/Controls.lean` | ledger evidence | `2e95e21b70af3b4a...` | copied; sha256 matches record |
| `lean/papers/p2_certified_zero_point/data/lean/RejectA2.lean` | ledger evidence | `ab0f5f297b0a24ba...` | copied; sha256 matches record |
| `lean/papers/p2_certified_zero_point/data/lean/RejectTampered.lean` | ledger evidence | `02f6930b22e47d7c...` | copied; sha256 matches record |

Full hashes: `lean_manifest.json`. `tools/check_consistency.py` re-hashes every copied file.
