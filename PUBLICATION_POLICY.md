# Public-Private IP Firewall

This repository is the public, MIT-licensed interoperability surface for PythiaGrid Research. It is intentionally **not** the product implementation of Mary/PythiaGrid.

## Public surface

Only material that is implementation-neutral and independently useful as a standard, conformance asset, synthetic fixture, reference tool, security/provenance document, or project documentation belongs here.

Permitted public classes:

- `PUBLIC_STANDARD` — implementation-neutral contracts and specifications.
- `SYNTHETIC_FIXTURE` — synthetic examples and negative/positive conformance cases.
- `REFERENCE_TOOLING` — minimal tooling required to validate the public standard.
- `PUBLIC_DOC` — documentation, licence, provenance, security and governance material.
- `CI_CONTROL` — automation that verifies only the public surface.

## Private moat

The following are outside the public surface and must remain in private, separately governed repositories or systems:

- Mary/PythiaGrid production runtime and orchestration;
- system/developer prompts and prompt libraries;
- proprietary planning/compiler logic;
- memory implementation and private knowledge structures;
- model-selection, routing, scoring, evaluation and recovery heuristics;
- production adapters, credentials, deployment topology and operational configuration;
- proprietary datasets, user data, private traces and internal receipts;
- unreleased product algorithms or implementation details whose disclosure would materially reduce reconstruction cost.

The MIT licence in this repository applies only to material actually published here. It does not grant rights to private code, private data, trademarks, model weights, hosted services, confidential information, or separately licensed assets.

## Default-deny publication rule

Every tracked file must be declared in `publication_manifest.json`. An unclassified tracked file is a publication failure.

A declared file must:

1. use one permitted public class;
2. declare `contains_private_implementation: false`;
3. declare `reconstruction_risk: LOW`;
4. avoid prohibited private/runtime paths;
5. pass secret/private-identifier leakage checks;
6. be synthetic or implementation-neutral where examples are used.

The automated gate is a minimum control, not a substitute for human IP review. Semantic disclosure can be risky even when no secret string is present.

## Reconstruction-risk test

Before publication, the reviewer must answer **NO** to this question:

> Could a capable competitor use this artifact to materially reproduce a differentiating Mary/PythiaGrid capability, production decision rule, implementation path, or operational advantage that is not necessary to implement the public EFAD interoperability contract?

If the answer is YES or uncertain, the artifact stays private until it is reduced to a genuinely implementation-neutral public contract.

## Release rule

A public release is admissible only when:

- `tools/publication_gate.py` returns `PASS`;
- the EFAD conformance gate returns `PASS`;
- the publication manifest covers the complete tracked surface;
- there is no unresolved reconstruction-risk concern;
- required provenance/licence review is complete.

Fail closed. Publication convenience never overrides the private-moat boundary.
