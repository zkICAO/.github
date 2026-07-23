# zkICAO

Zero-knowledge circuits and tooling for ICAO 9303 electronic identity documents: ePassports and national eID cards, universal across issuing states.

zkICAO provides small, auditable primitives on Noir + UltraHonk:

- Passive Authentication in circuit: document signer signature over the Security Object, data group integrity, optional trust chain up to the CSCA
- A universal attribute layer anchored on DG1 (MRZ), with country specific data groups as opt-in enrichment profiles
- Selective disclosure predicates: numeric comparison, set membership, single field reveal
- Scoped nullifiers with explicit, versioned uniqueness policies
- Off-chain verification by default; on-chain verification through recursive aggregation

| Repository | Contents |
|---|---|
| [circuits](https://github.com/zkICAO/circuits) | Noir circuits and shared libraries |
| [prover](https://github.com/zkICAO/prover) | Rust proving and off-chain verification library |
| [docs](https://github.com/zkICAO/docs) | protocol specification and threat model |

Status: early development. Specifications and limitations are documented honestly as they land; nothing is claimed that is not measured.
