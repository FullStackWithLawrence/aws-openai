# Semantic Versioning Guide

See [Conventional Commits](https://www.conventionalcommits.org/)

The [release.yml](.github/workflows/release.yml), [checkPullRequest.yml](.github/workflows/checkPullRequest.yml) and [testRelease.yml](.github/workflows/testRelease.yml) Github Action Workflows in this repo are designed to act on the commit comment rules that follow.

As an open-source maintainer, squash feature branches onto master and write a standardized commit message while doing so. The commit message should be structured as follows:

> `<type>`: This represents the type of change made in the commit. Common types include feat (for a new feature), fix (for a bug fix), chore (for routine tasks like updating dependencies), docs (for documentation changes), style (for code style changes), refactor (for refactoring existing code), test (for adding or updating tests), and perf (for performance improvements).
>
> `[optional scope]`: This is an optional part that provides additional contextual information, like the part of the codebase the commit modifies.
>
> `<description>`: This is a brief description of the changes the commit makes.
>
> `[optional body]`: This is an optional part where you can provide a more detailed explanation of the changes.
>
> `[optional footer(s)]`: This is also optional and is often used to reference issue tracker IDs.

## Commit Message format

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries such as documentation generation

Example

```console
git commit -m "docs: add an example of a good commit message"
```
