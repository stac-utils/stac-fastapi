# Releasing

This is a checklist for releasing a new version of **stac-fastapi**.

1. Determine the next version. We currently do not have published versioning guidelines, but there is some text on the subject here: <https://github.com/radiantearth/stac-spec/discussions/1184>.
2. Create a release branch named `release/vX.Y.Z`, where `X.Y.Z` is the new version.
3. Search and replace all instances of the current version number with the new version. As of this writing, there's five different `version.py` files, and one `VERSION` file, in the repo.
4. Update [CHANGES.md](./CHANGES.md) for the new version. Add the appropriate header, and update the links at the bottom of the file.
5. Audit CHANGES.md for completeness and accuracy. Also, ensure that the changes in this version are appropriate for the version number change (i.e. if you're making breaking changes, you should be increasing the `MAJOR` version number).
6. (optional) If you have permissions, run `scripts/publish --test` to test your PyPI publish. If successful, the published packages will be available on <http://test.pypy.org>.
7. Push your release branch, create a PR, and get approval.
8. Once the PR is merged, create a new (annotated, signed) tag on the appropriate commit. Name the tag `X.Y.Z`, and include `vX.Y.Z` as its annotation message.
9. Push your tag to Github, which will kick off the [publishing workflow](.github/workflows/publish.yml).
10. Create a [new release](https://github.com/stac-utils/stac-fastapi/releases/new) targeting the new tag, and use the "Generate release notes" feature to populate the description. Publish the release and mark it as the latest.
11. Publicize the release via the appropriate social channels, including [Gitter](https://matrix.to/#/#SpatioTemporal-Asset-Catalog_python:gitter.im).
