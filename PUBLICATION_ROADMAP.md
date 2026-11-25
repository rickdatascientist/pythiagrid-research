# Publication roadmap — PythiaGrid Research

**Research lead and proposed scholarly author:** Rick Sarkar  
**Current release:** Open MIT-licensed specification and research agenda, **not** a peer-reviewed article.  
**Publication disclaimer:** No manuscript here has been accepted by a journal, conference or arXiv.

## What is publishable now

The project's public EFAD JSON schema, rights-cleared synthetic conformance cases, reference validator, MIT licence, research hypotheses and documented limitations can be published **as an open-source research project on GitHub**. The repository is a public research asset, not an independent scientific certification.

The first evidence-carrying synthesis manuscript remains an internal **technical research report**, with early visible synthetic engineering checks and a deliberately candid comparison: an independently coded evidence-aware baseline matched the candidate on the test cases. These are not independent, hidden, multi-domain evaluations; broad superiority, novelty and product-safety claims must not be published as established results.

## Where a qualified future paper might be submitted

| Route | Why it might fit | Minimum additional work |
| --- | --- | --- |
| **[TMLR](https://jmlr.org/tmlr/)** | Rolling, double-blind machine-learning research review emphasizing sound technical claims and supported evidence | Strong prior-art positioning; preregistered fair comparative studies; independent replication; TMLR style and author requirements |
| **[NeurIPS](https://neurips.cc/)** / **[ICLR](https://iclr.cc/)** | Highly selective AI research venues for important technical/evaluation contributions | Significant novelty or a valuable new evaluation protocol; rigorous multi-domain benchmarks; calibrated uncertainty and reproducibility; venue-specific disclosure and submission rules |
| **[JOSS](https://joss.theoj.org/)** | Peer-reviewed substantial, reusable *research software* | Public installable software with meaningful research use, documentation, tests, maintenance and evidence of scholarly effort; a repository or a short note alone is insufficient |
| **[arXiv](https://arxiv.org/)** | Preprint dissemination of original substantive academic research; **not** peer review | Full, responsible manuscript with substantive contribution, accountable authorship, rights clearance, category/endorsement if required, moderation eligibility |
| **GitHub (this project)** | Open-source project, technical documentation and reproducibility materials | MIT licence, public/private separation, source and rights review, complete publication manifest and automated gates |

These are **candidate destinations, not acceptance predictions**. See primary policies: [TMLR acceptance criteria](https://jmlr.org/tmlr/acceptance-criteria.html), [TMLR authors](https://jmlr.org/tmlr/author-guide.html), [NeurIPS 2026 reviewing guidelines](https://neurips.cc/Conferences/2026/ReviewerGuidelines), [JOSS submission guide](https://joss.readthedocs.io/en/latest/submitting.html), [arXiv moderation](https://info.arxiv.org/help/moderation/index.html).

**ABDC clarification:** ABDC lists/ranks journals in business disciplines and does not certify individual research manuscripts. The venue must fit the research claim; AI/ML papers often appear in selective peer-reviewed conferences as well as journals.

## Evidence gates before submission

1. **Novelty:** a current, source-verified landscape review confronts ClaimReceipt, tau-bench, AgentRewind, UndoBench, provenance standards and related comparator methods.
2. **Method:** precise claims, failure-mode model, frozen datasets/splits, independently precommitted ground truth and explicit falsification criteria.
3. **Fair competitors:** stronger available verification methods receive equivalent evidence visibility, optimization budget and reproducible implementations.
4. **Results:** multiple independent tasks; held-out adversarial scenarios; exact denominators; paired statistical uncertainty; latency and resource cost; error analysis and *negative results*.
5. **Reproduction:** outside team/environment repeats source-pinned experiments. Publish the exact public-safe executable protocol, raw outcomes and manifest when rights-cleared.
6. **Research and rights review:** qualified non-author critique, citation and originality audit, human authorship responsibility, third-party licences, conflicts and AI-assistance disclosure.
7. **Public release:** only permission-cleared public material; private Mary production mechanisms, data, secrets and governance evidence remain outside this repo.

**Go/no-go law:** if the best fair evidence-aware comparator matches or outperforms the treatment on representative held-out tasks, narrow the claim or publish a negative benchmark methodology instead of implying a breakthrough.

## Authorship and licensing

The public project is credited to **Rick Sarkar**, with the [MIT licence](LICENSE). A researcher may be named as a scholarly author only if they approve and accept responsibility for their contribution, manuscript and disclosures. Do not list an AI system as a human author.

MIT licenses the **public repository materials** that are actually distributed. It does not grant rights to unreleased Mary source, private logs, product trade secrets or third-party assets. A journal may require a **different manuscript publication licence** (for example, TMLR submissions use CC BY 4.0). Its policy governs that manuscript; this does not change the MIT licence for the separate software project.

## Public site vs GitHub repository

The repository's README is publicly readable on GitHub after merge. A designed static site is staged at [docs/index.html](docs/index.html), but it is not a live GitHub Pages website until repository Pages is enabled, its source set to **Deploy from a branch**, branch **main**, folder **/docs**, and a successful Pages deployment is confirmed. Do not invent a public Pages URL before that verification.

---

*Last research editorial review: 25 November 2026. Recheck venue policy near actual submission.*
