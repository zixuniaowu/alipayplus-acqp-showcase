# Repository Guidelines

## Project Structure & Module Organization
This checkout is currently minimal: no source tree, build manifest, or test suite is committed yet. Keep the repository root reserved for shared config and documentation. As code is added, use a predictable layout:

- `src/` for application code
- `tests/` for automated tests
- `assets/` for static files such as images or fixtures
- `docs/` for design notes or integration guides
- `scripts/` for local automation

Prefer feature-oriented folders inside `src/`, for example `src/payments/` or `src/showcase/`.

## Build, Test, and Development Commands
No canonical build or test commands exist in the current workspace. When introducing a toolchain, expose the main workflows through a single entry point such as `package.json`, `Makefile`, or documented scripts.

Examples to add once tooling exists:

- `npm run dev` for local development
- `npm test` for the automated test suite
- `npm run lint` for static checks

Document new commands in the same pull request that adds them.

## Coding Style & Naming Conventions
Use 4 spaces for indentation unless the chosen language has a stricter formatter. Prefer small modules, explicit names, and one responsibility per file. Use:

- `PascalCase` for types and classes
- `camelCase` for variables and functions
- `kebab-case` for file and directory names unless the framework requires otherwise

Adopt an automatic formatter and linter with the first language runtime added to the repo, and run both before opening a PR.

## Testing Guidelines
Place tests under `tests/` or next to the code as `*.test.*` or `*.spec.*`. Cover new logic and bug fixes with automated tests. If a change cannot be tested automatically, explain the manual verification steps in the PR.

## Commit & Pull Request Guidelines
No Git history is available in this checkout, so follow Conventional Commits by default, for example `feat: add showcase landing page` or `fix: handle missing acquirer config`.

Pull requests should include:

- a short problem and solution summary
- linked issue or task ID when available
- screenshots for UI changes
- notes on testing performed and any follow-up work

## Security & Configuration Tips
Do not commit secrets, private keys, or production credentials. Keep local configuration in ignored env files such as `.env.local`, and provide a sanitized example file when new settings are required.
