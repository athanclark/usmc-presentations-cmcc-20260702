# CMCC Duties and Responsibilities for SIPR Assets

Marp-based training deck for CMCC custody, couriering, imaging, inventory, upclassing, and return procedures for SIPR assets.

## Published presentation

- **GitHub Pages:** <https://athanclark.com/usmc-presentations-cmcc-20260702/>
- **PDF on Pages:** <https://athanclark.com/usmc-presentations-cmcc-20260702/cmcc-20260702.pdf>
- **Repository:** <https://github.com/athanclark/usmc-presentations-cmcc-20260702>
- **Releases:** <https://github.com/athanclark/usmc-presentations-cmcc-20260702/releases>

## Source files

| Path | Purpose |
|---|---|
| `presentation.md` | Main Marp slide deck source |
| `presentation.html` | Locally generated HTML output |
| `presentation.pdf` | Locally generated PDF output |
| `engine.js` | Custom Marp engine configuration |
| `.github/workflows/build-presentation.yml` | CI workflow for HTML/PDF artifacts, releases, and GitHub Pages deployment |
| `*.png` | Local image assets used by the deck and published beside `index.html` on Pages |
| `ai/` | Barebones AI-related workspace notes and examples |

## Build locally

From the repository root:

```bash
marp --html --allow-local-files --engine ./engine.js presentation.md -o presentation.html
marp --pdf --allow-local-files --engine ./engine.js presentation.md -o presentation.pdf
```

## GitHub Actions

The workflow builds `dist/cmcc-20260702.html` and `dist/cmcc-20260702.pdf` on pushes, pull requests, tags, and manual dispatches.

On pushes to `master`, it also publishes GitHub Pages by copying:

- `dist/cmcc-20260702.html` to `site/index.html`
- `dist/cmcc-20260702.pdf` to `site/cmcc-20260702.pdf`
- local PNG assets to `site/`

On version tags like `v0.1.2`, the workflow creates or updates the matching GitHub release and uploads the generated HTML/PDF assets.

## Validation standard

Before reporting the deck as complete, validate that:

- Marp generates both HTML and PDF successfully.
- Inline reference anchors match reference definitions.
- The rendered Marp HTML has no overflowing slide elements.
- PDF text extraction matches the Markdown source with high per-slide coverage.

## Notes

This deck is a policy-level SOP model. Local command security direction, COMSEC Manager/KMI Operating Account guidance, SCI/SAP-specific rules, and local vault/open-storage approval documentation remain controlling when stricter.
