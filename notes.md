Experimental validation toolkit for FidelityFX SDK 1.1.4 (FSR 3.1.4) under Gamescope on ARM64 glibc Linux.

This is NOT a new RADV driver and does NOT add FSR3 to Gamescope. Gamescope -F fsr is FSR1. The official FSR3 Windows Vulkan sample is launched via a separately prepared Wine/Box64 runtime.

Includes source, an ARM64 native Vulkan probe and optional Box64 0.4.4 binary. The setup script downloads checksum-pinned Wine packages into a private runtime. The AMD SDK and sample media are downloaded separately from their official sources.

Validation completed: 13 toolkit tests; six actual SDK FP32/FP16 shader permutations passed SPIR-V validation and vkCreateComputePipelines on software Vulkan; ARM64 probe/Box64 cross-builds; official MediaDelivery --help under x64 Wine; packaged checksum checks. No GPU dispatch, Xclipse performance, Gamescope integration or FSR3 frame-generation pass is claimed.

Known blocker: current RADV Xclipse exposes one graphics queue; the official SDK Vulkan sample requires additional FG present/acquire queues and a dedicated copy queue. Preflight reports this rather than pretending FG works. The shader pipeline tests can still be used independently.

The ARM64 probe requires glibc 2.38 or newer. The optional prebuilt Box64 requires glibc 2.39; the installer builds from pinned source on 2.38. See docs/fidelityfx-gamescope.md inside the archive for commands, manual UI verification and limitations.
