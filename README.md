# godot-slim-templates

Smaller Godot release export templates for pure-2D games: 3D, XR, physics,
navigation and every module a 2D Control game doesn't use are compiled out.
The renderer, AccessKit and the advanced text server are left as stock.

- [`slim.py`](slim.py): the SCons profile. Each switch is commented.
- [`.github/workflows/build.yml`](.github/workflows/build.yml): builds Linux
  x86_64, Windows x86_64, macOS universal and Android arm64 (AAR) from an
  exact Godot tag, then publishes them as a GitHub Release with
  `SHA256SUMS`.

## Building

Run the workflow from the Actions tab, or:

```sh
gh workflow run build.yml -f godot_tag=4.7.2-stable -f release_tag=4.7.2-stable-slim.1
```

The Godot tag must match the editor that exports the game exactly. When the
editor is upgraded, build a new release at the new tag first.

## Release assets

| Asset | Use |
| --- | --- |
| `linux_release.x86_64` | Linux preset → `custom_template/release` |
| `windows_release_x86_64.exe` | Windows preset → `custom_template/release` |
| `macos.zip` | macOS preset → `custom_template/release` |
| `godot-lib.template_release.aar` | Gradle build → `android/build/libs/release/` |

Only release templates are built. Debug exports use the stock templates.

**A class that is compiled out fails only at runtime**, when the scene or
script using it loads. Play the game through on every platform before
shipping a new build.

## Licence

Godot Engine is MIT-licensed (© the Godot Engine contributors). The scripts
in this repo are MIT too.
