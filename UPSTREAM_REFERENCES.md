# Upstream references

PythiaGrid Research v0.1 is developed as clean-room specification work. The project does not vendor source code from the repositories below. References are recorded to make the research lineage auditable and to identify optional interoperability targets.

| Role | Repository | Pinned source | Code licence | Intended relationship |
|---|---|---|---|---|
| Evaluation | `EleutherAI/lm-evaluation-harness` | `a966806e4d297615a3d1d58be55de3c0e2dc915d` | MIT | Reference / optional adapter |
| AI security evaluation | `NVIDIA/garak` | `8ed1543b985a5722adb659584182faf6f7907d4e` | Apache-2.0 | Reference / optional adapter |
| Durable execution | `dbos-inc/dbos-transact-py` | `5bca975a729f6dcb921138f03e58628bbe00fa88` | MIT | Reference / optional adapter |
| Provenance | `philips-labs/slsa-provenance-action` | `9e9cb65933e01d622c0f092d9ec292f17bfe2c18` | MIT | Reference / optional adapter |

Additional evaluated references include `microsoft/PyRIT`, `temporalio/sdk-python`, `ossf/scorecard`, `hatchet-dev/hatchet`, and `modelscope/evalscope`. Their inclusion in research evidence does not make them runtime dependencies of EFAD.

## Rights boundary

A repository's code licence does not automatically grant rights to benchmark datasets, prompts, corpora, model weights, hosted services, trademarks, logos, or third-party assets included or referenced by that repository. EFAD v0.1 therefore keeps those asset classes outside the release bundle unless separately reviewed.

## Attribution posture

Where an optional adapter is later implemented against an upstream API, the adapter must preserve any attribution and notice obligations applicable to material actually redistributed. The baseline v0.1 export contains original clean-room specification material and no copied upstream source.
