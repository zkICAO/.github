# zkICAO

Zero-knowledge circuits and tooling for electronic identity documents, built on Noir and UltraHonk, with a Groth16 mirror of the predicate layer for verifiers that live on chain.

The first target is ICAO Doc 9303 (Machine Readable Travel Documents): ePassports and national eID cards carrying a contactless chip, across issuing states. Doc 9303 makes the machine readable zone in DG1 mandatory on every compliant document, which is what allows one set of circuits to serve documents from different states; data groups an individual state defines for itself are handled as opt-in profiles on top.

## What works

A document proves its way through a chain of small circuits: the country signing key certified the Document Signer, that signer signed the Security Object, the Security Object commits to a data group, that data group parses into committed fields, and statements are made about single fields without revealing the rest. Proofs are linked by equalities between their public values, and one verifier enforces that checklist so integrations do not carry their own copy.

Twenty three circuits exist across three machine readable zone layouts and six signature variants, including recursive aggregation: a registration proof that carries the whole document chain, and a session proof that carries a pair of predicates. A chip presence circuit proves the document's Active Authentication key answered this session's challenge, which is the one statement a copy of the data cannot make. A reference registry contract verifies real proofs under test and on a development chain with measured gas, and verification fails when the session context, the application domain, an output or an inner proof is changed.

## Status

Early development. Names, layouts and binding formats can still change. No genuine issued document has been proved end to end yet, and no third party audit has taken place; the coverage gaps are listed honestly in each repository rather than left to be discovered.

| Repository | Contents |
|---|---|
| [circuits](https://github.com/zkICAO/circuits) | Noir circuits, shared libraries, and the fixture generator |
| [prover](https://github.com/zkICAO/prover) | off-chain verification of a bundle of proofs |
| [contracts](https://github.com/zkICAO/contracts) | reference on chain registry and generated Solidity verifiers |
| [docs](https://github.com/zkICAO/docs) | protocol specification and threat model |

## Approach

Small circuits that compose, rather than one monolithic prover, so each piece can be reviewed on its own. Values shared between circuits are defined in one place and implemented once. Numbers are measured before they are published, and limitations are written down as they are found, including the inconvenient ones.

## Trademarks and affiliation

zkICAO is an independent open source project, not affiliated with, endorsed by, or approved by the International Civil Aviation Organization (ICAO) or the United Nations. See [TRADEMARKS.md](https://github.com/zkICAO/circuits/blob/main/TRADEMARKS.md).
