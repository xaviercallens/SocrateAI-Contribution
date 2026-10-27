# Lean files cited by `p2_navier_stokes_audit`

Collected from the ledger evidence blobs (`sources[].path` + `sha256`) and, where present, the auditor's `STATEMENT_LOCK.json`. `recorded` is the hash written when the claim was filed or locked; `current` is the hash of the file copied here. Upstream files (openai/math, openai/NavierStokesAndEuler, Lake packages) are listed with their hash and not redistributed; fetch them at the pinned commit. Where no hash was recorded (papers ED-03 to ED-08, written before hashes went into the ledger), the file is compared with the version last committed to AutoevolveAI before the Zenodo record was created; if they differ, that publication-time version is the one copied here. That commit is the best available proxy for what the paper compiled, not a recorded lock.

| file | via | recorded sha256 | status |
|---|---|---|---|
| `lean/results/proposal2/2026-10-26/A2/evidence/audit/ChallengeDump_NS.lean` | ledger evidence | `f7421203d6366170...` | copied; sha256 matches record |
| `lean/results/proposal2/2026-10-26/A2/evidence/audit/Semantics.lean` | ledger evidence | `48544ac7febe09f1...` | copied; sha256 matches record |
| `lean/results/proposal2/2026-10-26/A2/evidence/audit/Semantics2.lean` | ledger evidence | `10e3d9bff7637a41...` | copied; sha256 matches record |
| `lean/results/proposal2/2026-10-26/A2/evidence/controls/env/EnvControl.lean` | ledger evidence | `dacec70f1df142fc...` | copied; sha256 matches record |
| `lean/results/proposal2/2026-10-26/A2/evidence/controls/forged/Importer.lean` | ledger evidence | `80ce448a29b373ef...` | copied; sha256 matches record |
| `lean/results/proposal2/2026-10-26/A2/evidence/controls/forged/src/A2Forged.lean` | ledger evidence | `0417c7073a2f21ad...` | copied; sha256 matches record |
| `lean/results/proposal2/2026-10-26/A2/evidence/lean_scripts/A2Replay.lean` | ledger evidence | `d93172e97de47b6f...` | copied; sha256 matches record |
| `[upstream] Euler/Solution.lean` | ledger evidence | `5dced6caecbfd85d...` | upstream: listed, not copied — openai/NavierStokesAndEuler @ f9e8bc5b38b6e212696e8a30e3e91517af887bbd (Apache-2.0) |
| `[upstream] NavierStokes/ComparatorSolution.lean` | ledger evidence | `52950d5d618a8d34...` | upstream: listed, not copied — openai/NavierStokesAndEuler @ f9e8bc5b38b6e212696e8a30e3e91517af887bbd (Apache-2.0) |

Full hashes: `lean_manifest.json`. `tools/check_consistency.py` re-hashes every copied file.
