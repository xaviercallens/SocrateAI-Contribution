# Lean files cited by `p3_isothermal_theorem`

Collected from the ledger evidence blobs (`sources[].path` + `sha256`) and, where present, the auditor's `STATEMENT_LOCK.json`. `recorded` is the hash written when the claim was filed or locked; `current` is the hash of the file copied here. Upstream files (openai/math, openai/NavierStokesAndEuler, Lake packages) are listed with their hash and not redistributed; fetch them at the pinned commit. Where no hash was recorded (papers ED-03 to ED-08, written before hashes went into the ledger), the file is compared with the version last committed to AutoevolveAI before the Zenodo record was created; if they differ, that publication-time version is the one copied here. That commit is the best available proxy for what the paper compiled, not a recorded lock.

| file | via | recorded sha256 | status |
|---|---|---|---|
| `lean/formal_cert/Programmes/EvoGraph/BirthDeath.lean` | STATEMENT_LOCK.json; ledger evidence | `51383b6af304fe54...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/EvoGraph/EvoGraphImportAll.lean` | STATEMENT_LOCK.json | `7750097280b7c983...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/EvoGraph/EvoGraphPlantedControls.lean` | STATEMENT_LOCK.json; ledger evidence | `d3c875ee01fac100...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/EvoGraph/Examples.lean` | STATEMENT_LOCK.json; ledger evidence | `7156a702948565b0...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/EvoGraph/Transport.lean` | STATEMENT_LOCK.json; ledger evidence | `71babd503d7ee936...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/PopGen/Absorption.lean` | STATEMENT_LOCK.json; ledger evidence | `86fb5168a6b1efe0...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/PopGen/MoranModel.lean` | STATEMENT_LOCK.json; ledger evidence | `b0822dc0ee83505f...` | copied; sha256 matches record |

Full hashes: `lean_manifest.json`. `tools/check_consistency.py` re-hashes every copied file.
