# Lean files cited by `prog_cm_bernstein_library`

Collected from the ledger evidence blobs (`sources[].path` + `sha256`) and, where present, the auditor's `STATEMENT_LOCK.json`. `recorded` is the hash written when the claim was filed or locked; `current` is the hash of the file copied here. Upstream files (openai/math, openai/NavierStokesAndEuler, Lake packages) are listed with their hash and not redistributed; fetch them at the pinned commit. Where no hash was recorded (papers ED-03 to ED-08, written before hashes went into the ledger), the file is compared with the version last committed to AutoevolveAI before the Zenodo record was created; if they differ, that publication-time version is the one copied here. That commit is the best available proxy for what the paper compiled, not a recorded lock.

| file | via | recorded sha256 | status |
|---|---|---|---|
| `lean/formal_cert/Programmes/CompletelyMonotone/Applications.lean` | ledger evidence | `a6a0d17048eb3e2d...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/Basic.lean` | ledger evidence | `eaebc8f68fcab5cc...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/Bernstein.lean` | ledger evidence | `9e192c438a949b6d...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/Controls.lean` | ledger evidence | `1469ffd336424ef3...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/Corollaries.lean` | ledger evidence | `45e2ff5f4e8562f7...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/Examples.lean` | ledger evidence | `27994bc788426556...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/Laplace.lean` | ledger evidence | `fc721ec52eb51e97...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/Limits.lean` | ledger evidence | `04819006b336f37c...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/MathlibOnly.lean` | ledger evidence | `d0da3c865357431d...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/MathlibOnlyBridge.lean` | ledger evidence | `40c0d8be82caacc7...` | copied; sha256 matches record |
| `lean/formal_cert/Programmes/CompletelyMonotone/NegativeControls.lean` | ledger evidence | `83f5de212ee3f6ad...` | copied; sha256 matches record |
| `[upstream] .lake/packages/mathlib/Mathlib/Analysis/Calculus/AbsolutelyMonotone.lean` | ledger evidence | `55d9937e8c6b7285...` | upstream: listed, not copied — openai/math @ fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb (Apache-2.0; pinned local copy) |
| `[upstream] OAI/Analysis/Triangular/Energy/Basic.lean` | ledger evidence | `1b201a3f0062fc59...` | upstream: listed, not copied — openai/math @ fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb (Apache-2.0; pinned local copy) |
| `[upstream] OAI/Analysis/Triangular/Energy/Universal.lean` | ledger evidence | `35765ec2deda6020...` | upstream: listed, not copied — openai/math @ fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb (Apache-2.0; pinned local copy) |

Full hashes: `lean_manifest.json`. `tools/check_consistency.py` re-hashes every copied file.
