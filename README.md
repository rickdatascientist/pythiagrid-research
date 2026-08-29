# PythiaGrid Research — EFAD v0.1

**Evidence-First Autonomous Development (EFAD)** is an implementation-neutral specification for making autonomous software work inspectable, bounded, and fail-closed.

EFAD is not a model, agent framework, workflow engine, or benchmark suite. It defines a small interoperability layer that lets those systems prove four things consistently:

1. **Authority** — who or what authorized an action, with explicit scope and constraints.
2. **Evidence** — what was observed, which predicate was tested, and which source identities support the verdict.
3. **Work state** — what is active, blocked, failed, or complete under an explicit WIP limit and ANDON stop condition.
4. **Capability boundaries** — typed adapters that declare side-effect class and reject arbitrary-code or secret-bearing payloads by default.

## Why this exists

Autonomous development systems can generate large volumes of activity while leaving a weak answer to a simple question: **what exactly was authorized, what exactly happened, and what evidence proves the claim?**

EFAD treats that question as a protocol problem rather than a dashboard problem. The intended unit of progress is not a status update; it is a bounded claim backed by content-addressed evidence.

## v0.1 scope

The v0.1 candidate contains:

- implementation-neutral JSON contracts for authority, evidence receipts, work state, and capability adapters;
- positive and negative conformance fixtures;
- a deterministic conformance gate;
- a publication leakage/reconstruction-risk gate;
- provenance and upstream-reference metadata;
- synthetic examples only;
- no vendored third-party source code.

The release candidate intentionally does **not** prescribe an agent framework, LLM provider, durable-execution backend, evaluation framework, or provenance vendor.

## Core invariants

- Explicit authority beats inferred authority.
- Claims identify the predicate actually verified.
- Evidence carries immutable source identities and SHA-256 digests where applicable.
- Unsafe or unprovable states fail closed.
- Work in progress is bounded and machine-readable.
- ANDON is a first-class terminal/stop state, not a log message.
- Capability adapters declare side effects before execution.
- Arbitrary code execution and secret material are outside the baseline adapter contract.
- Public examples are synthetic and must not depend on private implementation history.

## Interoperability posture

EFAD is designed to sit above existing tools rather than replace them. The research process evaluates permissively licensed references across four roles:

- evaluation;
- AI security evaluation;
- durable execution;
- provenance/security-health.

Upstream tools remain optional references or adapters. Their source is not copied into this project, and their code licences do not imply rights to datasets, prompts, model weights, hosted services, trademarks, or other separately governed assets.

## Conformance model

A conforming implementation should be able to prove at least:

- positive authority/evidence/work-state/adapter fixtures validate;
- deliberately malformed or unsafe fixtures fail;
- evidence receipts are deterministic and content-addressable;
- export contents contain no configured private identifiers, local paths, secret-like strings, or direct private-source blob reuse;
- release provenance binds the published artifact to an exact source identity.

Passing EFAD conformance is a claim about these predicates only. It is not a claim that an autonomous system is generally safe, correct, or reliable.

## Project status

This directory is a **clean-room release candidate template**, not a published v0.1 release. Final publication remains gated on conformance, leakage/provenance checks, a fresh standalone repository, and finalization of the copyright holder in the MIT licence notice.

## Licence

The intended code/specification licence for v0.1 is the MIT License. The release bundle includes a licence template; it must not be treated as final until the copyright-holder field is resolved.
