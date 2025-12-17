# bevy-releasability

CI jobs to help check the release readiness of the Bevy project:

- check ownership of crates
- check crate build with default feature, all features, no default features
- check crate build for wasm32-unknown-unknown and aarch64-apple-ios
- check each top level feature individually
- build doc with example scrapping for each example individually
- release Bevy to a private repo to test the release process
