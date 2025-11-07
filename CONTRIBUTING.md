# Contributing to HAGI Constants

Thank you for your interest in contributing to the HAGI Constants project! We welcome contributions that improve the algorithmic foundations, enhance performance, expand test coverage, or clarify documentation. This guide will help you get started smoothly.

## Quick Start

1. **Fork the repository**
2. **Create a feature branch** – e.g., `git checkout -b feature/improve-coherence`
3. **Implement your changes**
4. **Run verification**: `make check`
5. **Submit a pull request**

Before making major changes, please open an issue to discuss your proposal with the maintainers to ensure alignment with the project goals.

## What We're Looking For

- Algorithmic improvements for the six constants
- Performance optimizations while preserving accuracy
- Comprehensive tests with edge case coverage
- Clear and thorough documentation updates
- Bug fixes and usability enhancements

## Code Standards

- Adhere to the Python PEP 8 style guide
- Include type hints in all function signatures
- Write tests for any new or modified functionality
- Update documentation to reflect behavior changes
- Ensure `make check` passes without errors

## Testing and Verification

Our project places testing as a foundational pillar. Before submitting:

- Run all tests with `make check` or `pytest test_constants.py -v`
- Verify your changes do not degrade coverage or performance
- Follow existing test style and add tests for new code

Tests ensure reproducibility and validate our mathematical claims. All contributions should uphold these standards.

## How to Report Issues

Please use the GitHub issue tracker for bug reports, feature requests, or other discussion topics. Provide as much detail as possible including reproduction steps and relevant environment info.

## Development Environment Setup

- Python 3.9 is required
- Install dependencies with: `make install`
- Use the provided `environment.yml` for an isolated conda environment (optional)

## Recognition

All contributors are credited in the project repository. Your contributions help advance foundational AGI research—thank you!

---

Together, we aim to build a reproducible, rigorous, and transparent framework that advances AI research responsibly. We appreciate your interest and support in this mission!
