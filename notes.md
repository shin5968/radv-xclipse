Experimental ARM64 glibc RADV build with optional AHardwareBuffer bridge support and an opt-in Termux-X11 AHB socket presentation path.

- Requires glibc 2.38 or newer and the X11/Wayland runtime dependencies documented in the package.
- A separate glibc-compatible AHB bridge implementing the documented layout callback is required to enable AHB support. No bridge implementation is included. Without it, the driver retains the existing presentation paths.
- Legacy servers retain required CPU render-completion waits; this is not a CPU-wait-free build.
- ARM64 cross-build, package integrity checks, native ICD loading, 5 mock bridge tests and 13 existing compiler tests passed. GPU execution and performance on a Samsung device are untested.

The release tag identifies the unchanged radv-glibc base commit. The ZIP additionally contains local source changes supplied in the attached patch; apply that patch to the tagged source to review/reproduce these changes. These changes have not been pushed to the branch. SHA256SUMS covers the ZIP and source patch. See AHB.md inside the ZIP for the bridge contract and activation instructions.
