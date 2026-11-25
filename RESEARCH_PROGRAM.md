# From Plausible Agents to Provable Work

### PythiaGrid Research | A three-problem research programme (candidate, 23 November 2026)

> **Research thesis.** The next important agent capability may not be planning more steps. It may be producing *verifiable results*, surviving *ambiguous failures*, and incorporating *new skills* without silently extending authority.

[EFAD specification](README.md) · [Publication policy](PUBLICATION_POLICY.md) · [Upstream references](UPSTREAM_REFERENCES.md)

**Status: proposed research agenda, not a paper or demonstrated state-of-the-art result.** No results, superiority claims, novelty verdicts, deployment authorization, or production-readiness claims follow from this page. Each hypothesis is falsifiable and needs an independent literature review, controls, reproducible public fixtures, and a separately reviewed release.

## The three research questions

| Priority | Candidate research contribution | Central question | Evidence readiness |
| --- | --- | --- | --- |
| **R1** | **Evidence-Carrying Agent Work (ECAW)** — an interoperable proof contract | Can an agent's authority, action, result and evidence be verified independently of its prose? | Existing EFAD specification/fixture starting point; cross-framework evaluation **not yet established** |
| **R2** | **Recoverable Agents Benchmark (RAB)** — fault-injected, end-to-end work evaluation | Can an agent resume consequential work after crash, lost acknowledgement, retry or restoration *without duplicate effects or false success*? | Candidate inspiration from isolated engineering studies; public reproducible benchmark **not yet established** |
| **R3** | **Verified Skill Commons (VSC)** — bounded skill-evolution protocol | Can separately contributed skills improve task performance while preserving permission boundaries, provenance, rollback and independent admission? | Concept and protocol research; community-scale validation **not yet established** |

The programme is coherent but intentionally not one monolithic paper. R1 defines what it means to *prove work*. R2 asks whether the proof remains meaningful *across failure and recovery*. R3 asks whether new capabilities can be admitted *without losing that proof*.

---

## R1 · Evidence-Carrying Agent Work

**Question.** When an LLM says “done,” can a different implementation prove that the authorized effect occurred, on the correct inputs, under the correct authority, using independently checkable evidence?

**Hypothesis H1.** A bounded, typed, content-addressed evidence contract with explicit abstention reduces unsupported success declarations compared with (a) free-form agent self-report and (b) tool logs lacking claim-to-evidence checks. The contract does *not* imply the underlying task is always correct or safe.

**Candidate scientific contribution:** an implementation-neutral verification protocol built on EFAD's public authority, evidence, work-state and adapter contracts; a minimal synthetic interoperability corpus; and empirical measurement of claim correctness under missing, contradictory, forged, stale or selectively omitted evidence.

**Pre-registered measurements:** unsupported-success rate; evidence coverage and provenance integrity; abstention precision and recall; acceptance of deliberately misleading receipts; time/cost to independently verify; portability across two genuinely distinct agent harnesses.

**Minimum convincing experiment:** at least two independent implementations, task instances with hidden ground-truth effects, blinded evaluator, positive/negative examples, adversarial evidence removal and replay. Report denominators, confidence intervals and all inconclusive outcomes; include protocol-without-content-addressing and logs-only ablations.

**Failure that would falsify the proposed advantage:** contract-based verification does not materially improve truthful outcome classification versus the strongest log-and-oracle baseline, or fails under realistic adversarial evidence.

**Relation to existing work:** scientific-workflow provenance, W3C PROV, `tau-bench`/state-based agent evaluations, execution tracing, and recent claim-receipt research. This contribution cannot claim to invent agent governance, receipts, or provenance.

**Potential reusable output:** EFAD compatible public conformance fixtures, verification protocol and independent benchmark report.

## R2 · Recoverable Agents Benchmark

**Question.** What constitutes a correct final result when an agent has dispatched a side effect but loses acknowledgement, crashes while verifying, or restores from a backup that may be incomplete?

**Hypothesis H2.** An outcome-driven agent harness that distinguishes *in-doubt*, *failed* and *verified* effects, uses operation identity and recovery evidence, and requires independent final-state checking can outperform naïve retry-and-report baselines on false-success and duplicate-effect risk. This is a testable hypothesis, not a guarantee of exactly-once execution.

**Candidate scientific contribution:** an open, synthetic fault-injection benchmark with controllable side-effect simulators, explicit crash cuts, ambiguous acknowledgements, independent final-state oracles, snapshot and restore checks, and honest `INCONCLUSIVE` verdicts.

**Pre-registered measurements:** duplicate external effects; lost authorized effects; false-VERIFIED rate; final-state agreement; recovery and restore success; mean time to justified recovery; overhead; amount of irreconcilable in-doubt work.

**Minimum convincing experiment:** compare at least (a) agent retries without durable operation identity, (b) durable workflow/retry engine with ordinary logs, (c) evidence-and-effect-identity harness. Use paired tasks and seeded fault schedules at boundaries before dispatch, after external effect, before acknowledgement, during verification and after state snapshot. Where an endpoint cannot offer effect idempotency, do **not** assert exactly-once.

**Failure that would falsify the proposed advantage:** no significant improvement on effect correctness or false-success at an acceptable latency/resource cost, or recovery cannot distinguish missing work from completed-but-unacknowledged work.

**Relation to existing work:** database transaction semantics, durable workflow frameworks, distributed systems recovery, state-machine replication and recent LLM-agent duplicate-side-effect research. The likely contribution is the *benchmark and cross-layer evidence protocol*, not inventing durable execution.

**Potential reusable output:** deterministic benchmark harness, fault traces with synthetic identifiers, baseline adapters, public oracle specification and reproducible evaluation recipe.

## R3 · Verified Skill Commons

**Question.** Can an agent accept third-party or self-generated reusable skills, improve on held-out tasks and still respect the authority, privacy, provenance and safety constraints of the original system?

**Hypothesis H3.** Evidence-gated skill admission with independent holdouts, bounded authority, quarantine and rollback can improve retained task performance versus a static skill library while reducing unsafe or regressive updates versus unvalidated skill accumulation.

**Candidate scientific contribution:** a portable *skill admission and lifecycle evaluation* contract, including ownership/licence metadata, declared capabilities, benchmark evidence, dependency versioning, least-privilege execution scopes, regression checks and promotion/rollback records. Community reputation is not a substitute for verification.

**Pre-registered measurements:** held-out task improvement; negative transfer; malicious-skill admission rate; permission-escalation incidents; detection of poisoned benchmark submissions; cost/latency overhead; rollback restoration; diversity of contributors and environments.

**Minimum convincing experiment:** static baseline vs naïve skill accumulation vs verified-admission protocol across multiple skill sources and unseen tasks; adversarial skills that attempt authority expansion, data exfiltration, misleading evaluation or dependency substitution; an independent evaluator that is not the skill author or proposer.

**Failure that would falsify the proposed advantage:** accepted skills fail to generalize, can smuggle new authority, degrade held-out performance, or cause unacceptable overhead versus simpler skill-management policies.

**Relation to existing work:** skill libraries, skill evolution and verification, software supply-chain security, capability-based authorization and federated/community evaluation. Novelty must be evaluated particularly against SkillWeaver and newer verifiable skill libraries.

**Potential reusable output:** schema, synthetic skill fixtures, independent evaluator interface, benchmark protocol and a community-ready contribution format.

---

## Methodology that all three studies must share

1. **Ground truth before prose.** Define objective state predicates and an independent oracle before testing agents. A persuasive explanation is not a verified outcome.
2. **Competing baselines.** Compare with strong existing alternatives, not merely an intentionally weak agent. Include ablations and failure cases.
3. **Preregister hypotheses.** Freeze task samples, holdouts, metrics, stopping rules and falsification criteria; do not select only successful demonstrations.
4. **Repeat and attribute.** Multiple seeds, independently rerunnable fixtures, pinned dependency versions, exact environment manifests, confidence intervals, failure distributions and cost/latency accounting.
5. **Separate engineering qualification from science.** Private development receipts can motivate a hypothesis, but public empirical claims require shareable, independently verified evidence or appropriately blinded replication.
6. **Preserve intellectual property and rights.** Publish only implementation-neutral protocols and synthetic or permission-cleared artifacts. Never publish private execution traces, proprietary algorithms, secrets, user records, undisclosed partner data or deployment details.
7. **Report negative results.** A failed experiment or a no-advantage result is useful research. Neither a benchmark PASS nor a paper acceptance is a production launch gate.

## Proposed two-surface research experience

**Research in the personal workspace:** researchers can inspect references, plan studies, produce candidate manuscripts, run analysis and review source-bound evidence. Human researchers control authorship, disclosure and submission. Manuscript-generation engines, including PaperOrchestra-style tools, are optional adapters rather than publication authorities.

**Research in the Commons:** approved participants may submit sanitized datasets/fixtures, skills, evaluation methods and benchmark results. A separate evaluator admits or rejects contributions; admission does not silently expand privileges or change production systems.

The workflow is a **proposal**; neither surface is claimed to implement this full research pipeline today.

## Reproducibility and public release gates

For each track, the release packet must contain: `README`/problem statement; threat model; claims vs evidence table; public synthetic task generator; baseline definitions; exact command/config manifest; run-level outcomes; evaluator independence record; rights review; known limitations; and a machine-readable versioned result.

**Paper-ready only when:** a concrete novelty claim survives a prior-art review, a controlled study answers the pre-registered hypothesis, independent reproduction succeeds, and the public/private publication gate admits the exact proposed release.

**Production claim-ready only when:** the separately governed product safety/release process admits it. Academic evaluation cannot override production holds.

## Selected related work and benchmark anchors

These references help define the *overlap and limitations* of proposed novelty; they are not proof of a unique contribution:

- [EFAD public specification (this repository)](README.md) — existing contract and conformance starting point.
- [tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — state-based agent/task evaluation.
- [AgencyBench](https://arxiv.org/abs/2601.11044) — long-horizon agent evaluation.
- [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825) — evaluation methodology risks.
- [ClaimReceipt: Verifying Evidence Sufficiency and Coverage in Agent Evaluations](https://arxiv.org/abs/2609.01992) — directly relevant to R1, demanding novelty scrutiny.
- [SkillWeaver](https://arxiv.org/abs/2504.07079) and [Skill-V](https://arxiv.org/abs/2610.11781) — directly relevant to R3.
- [W3C PROV overview](https://www.w3.org/TR/prov-overview/) — provenance foundations.

## Status and contribution policy

This is a **research prospectus**, not a submitted paper. Estimated strength: **R1 = best immediate research foundation; R2 = strongest product-aligned experimental testbed; R3 = highest ecosystem potential but least evidence today.**

No public benchmarking numbers or novel-science claims are currently certified by this agenda. A future PR must pass `python tools/publication_gate.py`, EFAD conformance, semantic IP/reconstruction-risk and independent research review before merge or release.

For questions or responsible contributions, open a proposal on this public repository without sharing private Mary or PythiaGrid implementation details.
