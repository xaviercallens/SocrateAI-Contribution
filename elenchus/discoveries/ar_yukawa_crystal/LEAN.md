# Lean files cited by `ar_yukawa_crystal`

Collected from the ledger evidence blobs (`sources[].path` + `sha256`) and, where present, the auditor's `STATEMENT_LOCK.json`. `recorded` is the hash written when the claim was filed or locked; `current` is the hash of the file copied here. Upstream files (openai/math, openai/NavierStokesAndEuler, Lake packages) are listed with their hash and not redistributed; fetch them at the pinned commit. Where no hash was recorded (papers ED-03 to ED-08, written before hashes went into the ledger), the file is compared with the version last committed to AutoevolveAI before the Zenodo record was created; if they differ, that publication-time version is the one copied here. That commit is the best available proxy for what the paper compiled, not a recorded lock.

| file | via | recorded sha256 | status |
|---|---|---|---|
| `lean/formal_cert/Autoresearch/Yukawa.lean` | ledger evidence | `a16397de179837dd...` | copied; sha256 matches record |
| `lean/formal_cert/Autoresearch/YukawaMix.lean` | ledger evidence | `6a940a7cb1b4b253...` | copied; sha256 matches record |
| `lean/formal_cert/Triangular/AnyDensity.lean` | ledger evidence | `0a6d86eef3ee24b2...` | copied; sha256 matches record |
| `lean/formal_cert/Triangular/Riesz.lean` | ledger evidence | `a99c2024b065360b...` | copied; sha256 matches record |
| `lean/formal_cert/Triangular/RieszFinite.lean` | ledger evidence | `7aa2f523e83a1d9e...` | copied; sha256 matches record |
| `[upstream] OAI/Analysis/Triangular/Energy/Basic.lean` | ledger evidence | `1b201a3f0062fc59...` | upstream: listed, not copied — openai/math @ fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb (Apache-2.0; pinned local copy) |
| `[upstream] OAI/Analysis/Triangular/Energy/Definitions.lean` | ledger evidence | `c375b08fe541a386...` | upstream: listed, not copied — openai/math @ fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb (Apache-2.0; pinned local copy) |
| `[upstream] OAI/Analysis/Triangular/Energy/Universal.lean` | ledger evidence | `35765ec2deda6020...` | upstream: listed, not copied — openai/math @ fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb (Apache-2.0; pinned local copy) |

Full hashes: `lean_manifest.json`. `tools/check_consistency.py` re-hashes every copied file.
