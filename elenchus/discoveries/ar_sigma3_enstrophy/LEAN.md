# Lean files cited by `ar_sigma3_enstrophy`

Collected from the ledger evidence blobs (`sources[].path` + `sha256`) and, where present, the auditor's `STATEMENT_LOCK.json`. `recorded` is the hash written when the claim was filed or locked; `current` is the hash of the file copied here. Upstream files (openai/math, openai/NavierStokesAndEuler, Lake packages) are listed with their hash and not redistributed; fetch them at the pinned commit. Where no hash was recorded (papers ED-03 to ED-08, written before hashes went into the ledger), the file is compared with the version last committed to AutoevolveAI before the Zenodo record was created; if they differ, that publication-time version is the one copied here. That commit is the best available proxy for what the paper compiled, not a recorded lock.

| file | via | recorded sha256 | status |
|---|---|---|---|
| `lean/results/autoresearch/2026-10-25/H7/Autoresearch_Enstrophy.lean` | ledger evidence | `c7c9f24cfe2e623f...` | copied; sha256 matches record |
| `lean/results/autoresearch/2026-10-25/H7/contribution/Autoresearch_EnstrophyFlow.lean` | ledger evidence | `4cd746897f58f7a1...` | copied; sha256 matches record |
| `lean/results/autoresearch/2026-10-25/H7/contribution/Autoresearch_EnstrophyFlowControls.lean` | ledger evidence | `7a3904240f4734df...` | copied; sha256 matches record |
| `lean/results/autoresearch/2026-10-25/H7/contribution/OwnerAxioms.lean` | ledger evidence | `706ac512aef519e4...` | copied; sha256 matches record |
| `lean/external/SocrateAI-Scientific-QuantumFluids/lean_src/QuantumFluidsShell.lean` | ledger evidence | `8da44064789a2489...` | copied; sha256 matches record |
| `lean/external/SocrateAI-Scientific-QuantumFluids/lean_src/ShellHamiltonian.lean` | ledger evidence | `5755576ed170a561...` | copied; sha256 matches record |

Full hashes: `lean_manifest.json`. `tools/check_consistency.py` re-hashes every copied file.
