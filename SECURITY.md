# Security policy

## Reporting a vulnerability

Please use GitHub's private security-advisory mechanism for vulnerabilities in the released EFAD specification, reference tooling, conformance gates, or release workflow. Do not include credentials, private keys, access tokens, or sensitive third-party data in a public issue.

## Security boundary

EFAD conformance is intentionally narrow. A passing conformance result means the tested authority, evidence, work-state, adapter, and publication predicates passed. It does not certify the safety of a model, agent, operating system, workflow backend, third-party adapter, or deployment environment.

## Baseline prohibited behavior

The baseline capability-adapter contract rejects arbitrary-code execution and secret-bearing payloads. Implementations that deliberately extend those capabilities are outside baseline conformance and must define their own explicit authority, isolation, audit, and recovery controls.

## Supply-chain expectations

Release candidates should use exact source identities, pinned CI actions where practical, content-addressed receipts, dependency review, and provenance/SBOM generation. Third-party code, data, models, and hosted services remain subject to their own licences and security policies.
