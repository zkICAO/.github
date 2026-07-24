# zkICAO

Zero-knowledge circuits and tooling for electronic identity documents, built on Noir and UltraHonk.

The first target is ICAO Doc 9303 (Machine Readable Travel Documents): ePassports and national eID cards carrying a contactless chip, across issuing states. Doc 9303 makes the machine readable zone in DG1 mandatory on every compliant document, which is what allows one set of circuits to serve documents from different states; data groups an individual state defines for itself are handled as opt-in profiles on top.

## Status

Early development. The shared circuit libraries exist and are tested. No circuit implements the protocol yet, nothing has been proved end to end, and the proving library is a skeleton. Names, layouts and binding formats can still change.

Work in progress, in order: the specification, a fixture generator, then the Security Object and data group circuits.

| Repository | Contents |
|---|---|
| [circuits](https://github.com/zkICAO/circuits) | Noir libraries, and the circuits as they land |
| [prover](https://github.com/zkICAO/prover) | Rust proving and off-chain verification library |
| [docs](https://github.com/zkICAO/docs) | protocol specification and threat model |

## Approach

Small circuits that compose, rather than one monolithic prover, so each piece can be reviewed on its own. Values shared between circuits are specified in one place and implemented once. Limitations are written down as they are found, including the ones that are inconvenient.

## Trademarks and affiliation

zkICAO is an independent open source project, not affiliated with, endorsed by, or approved by the International Civil Aviation Organization (ICAO) or the United Nations. See [TRADEMARKS.md](https://github.com/zkICAO/circuits/blob/main/TRADEMARKS.md).
