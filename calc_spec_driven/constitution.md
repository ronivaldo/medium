# Project Constitution – Calculator

This document defines the immutable principles that govern the design, implementation and evolution of our calculator project. These principles are inspired by Spec‑Driven Development (SDD) practices and serve as the architectural DNA of the system. They ensure that any generated code or new features respect modularity, testability, and simplicity, and they align with the articles described in the SDD constitution【121547767717787†L709-L734】.

## Article I – Library‑first principle

All functionality must start as a standalone library. No feature is implemented directly in application code without first being abstracted into a reusable module【121547767717787†L709-L721】. For the calculator, the arithmetic operations (addition, subtraction, multiplication and division) are implemented as pure functions within a library package (`calc/operations.py`) so that other programs can reuse them independently of the CLI.

## Article II – CLI interface mandate

Every library must expose its functionality through a command‑line interface. The CLI must accept text input and emit text or JSON output【121547767717787†L723-L734】. Our calculator provides a CLI script (`calc_cli.py`) that accepts two numbers and an operator via command‑line arguments and prints the result.

## Article III – Test‑first imperative

No implementation code is written before the tests. All unit and integration tests must be authored, validated and confirmed to fail (red phase) before writing implementation code【121547767717787†L736-L749】. The calculator includes tests in `tests/` covering each arithmetic operation and the CLI behaviour. Tests are created first and serve as the acceptance criteria.

## Article VII & VIII – Simplicity and Anti‑abstraction

The initial implementation should be as simple as possible and avoid unnecessary abstraction【121547767717787†L751-L764】. The project will contain a maximum of two modules (the library and the CLI); additional layers or wrappers must be justified. Framework features are used directly rather than wrapped in extra abstractions.

## Article IX – Integration‑first testing

Tests must exercise the real code paths. Integration tests use the actual CLI and real arithmetic functions rather than mocks【121547767717787†L766-L774】. Each operation is tested via both the library API and the CLI interface to ensure end‑to‑end correctness.

## Amendment process

Modifying this constitution requires a documented rationale, review and approval by maintainers. Amendments must maintain backwards compatibility wherever possible【121547767717787†L800-L825】.
