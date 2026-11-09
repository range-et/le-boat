# Le Boat

A little wind-powered yacht for a little patch of Toronto.

Le Boat is an experimental, human–AI co-created RC sailboat for neighbourhood sailing at Love Park. Wind in cloth sails supplies all propulsion. A battery may power the receiver and servos for steering and sail trim; there is no propeller, auxiliary motor or powered recovery drive.

The project is primarily CAD and physical making: Rhino geometry, parametric scripts, home fabrication, assembly, and honest records of what happens on the water. A smaller DragonForce 65 is a starting inspiration, not a class rule or a design to copy.

**Status: brief and research. No hull has been designed, built or validated here yet.** The current repository contains project documentation and the project website, not ready-to-print boat files.

## Start here

- [Design brief](design-brief.md): requirements, candidate dimensions, systems and acceptance gates.
- [Site research](project/pond.md): location, published depth, access questions and survey plan.
- [Build and test plan](project/build-plan.md): work packages from mass budget to first sail.
- [Decision register](project/decisions.md): what is settled and what needs evidence.
- [AI co-creation](project/ai-co-creation.md): tools, human responsibility and evidence standards.
- [Build journal](journal/2026-11-08-project-foundation.md): first entry; future entries should include failures too.
- [Licensing](LICENSE.md) and [experimental-use notice](DISCLAIMER.md).
- [Project website](https://range-et.github.io/le-boat/).

## The pond shapes the boat

Google Maps identifies Love Park at 96 Queens Quay West. Waterfront Toronto publishes a pond depth of **20–60 cm**, approximately **8–24 in**, not 18 ft. Map imagery does not establish bottom clearance. We need to measure a usable route, account for obstructions and water levels, and confirm local operating rules before sailing. See the linked sources and unresolved questions in [site research](project/pond.md).

## Made with AI, openly

This project deliberately tests how a person and AI tools can design, document and build something physical together. Codex helped develop this repository's brief, research, documentation and website. AI suggestions are proposals until checked; models, calculations, simulations and physical tests must be distinguished. People choose what gets built and remain responsible for those choices.

## Reuse and commercial use

Original CAD, model exports, drawings, documentation, journal text and original imagery: **CC BY-NC-SA 4.0**. Original software, including geometry-generation scripts and website code: **PolyForm Noncommercial 1.0.0**. See [LICENSE.md](LICENSE.md) for scope, attribution, third-party exclusions and the limits of protection for functional objects.

Commercial use outside the published grants requires separate written permission from the relevant rights holders. Credit alone does not grant commercial permission. Start with a [repository issue](https://github.com/range-et/le-boat/issues) describing the proposed use; an unanswered request grants no permission. These noncommercial terms mean the project is source-available, rather than OSI open source or unrestricted open hardware.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Share editable source, units, assumptions, evidence, provenance and your AI involvement. Do not present renders or simulation images as successful physical trials.

## Website

The dependency-free static site is in `docs/`, served by GitHub Pages. Install the pinned build dependency once with `python3 -m venv .venv` and `.venv/bin/python -m pip install -r requirements-site.txt`. Run `.venv/bin/python scripts/build_site.py` after editing project documents; it generates browsable reference pages from the Markdown sources. Preview with `python3 -m http.server 8000 --directory docs` and open `http://localhost:8000`. The Pages workflow rebuilds and deploys on pushes to `main`; it can also be run manually.
