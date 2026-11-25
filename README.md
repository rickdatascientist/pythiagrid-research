# PythiaGrid Research

### **Autonomous systems should prove their work.**

**Open research into evidence-carrying AI agents, recoverable execution, and verifiable skill evolution.**

[Explore the research programme](RESEARCH_PROGRAM.md) · [Read EFAD v0.1 contracts](spec/PGR_CONTRACTS_V0_1.json) · [Run the conformance tooling](#run-the-public-specification) · [Publication and IP policy](PUBLICATION_POLICY.md) · [Research website source](docs/index.html)

> **North star:** Build AI systems that do not simply *claim* success. They preserve authority, retain verifiable evidence, admit uncertainty, recover safely, and earn additional capabilities through independently tested improvements.

**Research lead and credited author:** **Rick Sarkar**  
**Licence:** [MIT](LICENSE) for the material **actually contained in this public repository**. This does not license the private Mary/PythiaGrid product, models, datasets or unpublished mechanisms.  
**Research maturity:** Open specification and synthetic conformance tooling available. The three scientific tracks below are **active hypotheses**, not established state-of-the-art results or peer-reviewed publications.

---

## One research thesis, three testable problems

| Research track | Scientific problem | Current evidence state |
| :-- | :-- | :-- |
| **01 · Evidence-Carrying Agent Work** | Can an independently auditable claim survive competing agent attempts without promoting unsupported outcomes? | EFAD contracts and public conformance fixtures available; paper-level comparative superiority **unproven** |
| **02 · Recoverable Agents Benchmark** | How can we evaluate correctness after crashes, ambiguous acknowledgements, retries and restoration? | Research protocol proposed; public fault-injected comparative benchmark **not yet released** |
| **03 · Verified Skill Commons** | Can community-created skills improve agents without permission drift, benchmark manipulation or hidden regressions? | Research protocol proposed; held-out multi-source qualification **not yet executed** |

[Read hypotheses, baselines, falsification criteria, and research ethics →](RESEARCH_PROGRAM.md)

### The research loop

```text
RESEARCH QUESTION
      │
      ▼
HYPOTHESIS + PRIOR ART
      │
      ▼
FROZEN TASK / INDEPENDENT ORACLE
      │
      ▼
AGENTS, BASELINES, ADVERSARIAL CASES
      │
      ▼
EVIDENCE + CONTRADICTION AUDIT
      │
      ▼
REPRODUCIBILITY + INDEPENDENT REVIEW
      │
      ▼
PUBLIC RESULT OR HONEST ABSTENTION
```

**A pass in an implementation test is not evidence of superiority.** Any published comparative claim must include the exact test set, independent baseline, oracle, denominators, negative cases, reproducibility recipe and uncertainty. Findings that a simple evidence-aware comparator matches a more elaborate method count as useful negative research evidence, not as a marketing success.

## Evidence-First Autonomous Development (EFAD)

EFAD is a small **interoperability contract**, not another agent framework.

- **Authority:** what action was approved, for whom and within which bounds.
- **Evidence:** which predicate was checked, from which immutable source and observation.
- **Work state:** READY, ACTIVE, BLOCKED, ANDON, PASS or FAIL under a declared work-in-progress limit.
- **Capabilities:** typed least-authority adapters that declare side-effect class.

The v0.1 public surface includes JSON contracts, synthetic positive/negative cases, deterministic conformance tooling, source references and a default-deny publication gate. These tools evaluate *specific predicates*; they cannot certify general agent safety.

### Run the public specification

```bash
python -m pip install -r requirements-research.txt
python tools/conformance.py --spec spec/PGR_CONTRACTS_V0_1.json --fixtures spec/PGR_CONFORMANCE_FIXTURES_V0_1.json --out efad_conformance_receipt.json
python tools/publication_gate.py
```

The publication gate checks public file classification, configured private-identifier/secret patterns and approved file types. It **does not replace** independent legal/IP or semantic disclosure review.

## Papers and scientific status

**Working manuscript 01 — _Evidence-Carrying Synthesis for Autonomous Agents: Preserving Verified Partial Progress Without Promoting Unsupported Claims_.**

- **Lead author:** Rick Sarkar (author responsibility and final submission approval remain human).
- **Status:** internal technical research report / manuscript candidate. **Not peer-reviewed, not accepted, not an arXiv preprint.**
- **Observed engineering boundary:** tests of a local synthesizer motivated the method, but a separately coded evidence-aware comparator matched its decisions on visible synthetic cases; therefore no comparative performance or novelty advantage is claimed here.
- **Needed:** a verified strong published-method baseline, an independently authored multi-domain benchmark, sealed held-out evaluation, replicated runs, quantitative uncertainty and rights-approved public release.

**Publication strategy:** a mature empirical contribution could be considered for TMLR, NeurIPS/ICLR or an appropriate peer-reviewed venue after scientific qualification; a substantial reusable public research-software package may eventually qualify for JOSS. GitHub is a project/research distribution platform, **not peer review**.

The current manuscript and private implementation **are not copied to this public repository**. Use the [research agenda](RESEARCH_PROGRAM.md) to see what can be independently verified and contributed publicly.

## Why this matters to Mary

PythiaGrid Research is the **open scientific and interoperability layer** informing the long-term vision for Mary. The proposed research workflow separates a researcher's private workspace (for hypotheses, experiments and manuscript review) from a Commons surface (for permission-cleared benchmarks and contributions).

**Research findings do not automatically alter or authorize the Mary production system.** Public specifications, study results and product capabilities have independent review and release gates.

## Contribute carefully

Useful contributions include verified prior art; synthetic cases that disprove a claim; fair baseline definitions; reproducibility reviews; and concrete counterexamples to authority, evidence and dependency assumptions. Please do **not** post secrets, private run logs, user records, proprietary Mary source, or other people's licensed datasets.

For disclosure or security concerns, see [SECURITY.md](SECURITY.md). For the public/private IP boundary, see [PUBLICATION_POLICY.md](PUBLICATION_POLICY.md). For referenced upstream work, see [UPSTREAM_REFERENCES.md](UPSTREAM_REFERENCES.md).

## Citation, authorship and licence

Research direction, copyright and credited authorship: **Rick Sarkar**. A machine-readable [CITATION.cff](CITATION.cff) identifies the public project. Any future scholarly paper will disclose AI-assisted preparation consistent with the selected venue, and all named human authors must confirm intellectual responsibility.

The public repository's [MIT licence](LICENSE) applies only to its released code and documentation. Private Marykin Labs/PythiaGrid technology, confidential material, names/trademarks, third-party publications and separately licensed assets are not granted by MIT.

---

*Evidence before assertion. Recovery before repetition. Verification before promotion.*
