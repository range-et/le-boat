# Le Boat

Le Boat is an experimental RC sailboat for Love Park in Toronto.
Wind provides all propulsion. A battery powers the radio receiver and servos for steering and sail trim.

The project covers CAD, home fabrication, assembly, CFD and water tests.
The DragonForce 65 provides an initial design reference.
We will select dimensions from equipment mass, stability, pond depth and printer limits.

**Status: design brief and research.** The repository contains documentation and the website.
Boat geometry, fabrication and water tests are pending.

## Tools

| Work | Selected tool | Current use |
| --- | --- | --- |
| CAD management | [git-cad](https://github.com/range-et/git-cad) | Selected. Setup awaits an available workflow. The upstream project is in specification/prototype development. |
| Website UI | [Monad System](https://github.com/range-et/monad_system) | The site uses pinned Monad CSS, components and theme controls. |
| CFD | [Hawa](https://github.com/range-et/hawa-cfd) | Selected for hull, keel and rudder flow studies. Boat cases are pending. |

Use Rhino and Grasshopper to create geometry and define simulation cases.
Read the [tool and optimization plan](project/tools-and-optimization.md) for versions, interfaces and limits.

## Project documents

- [Design brief](design-brief.md): requirements and proposed dimensions.
- [Site research](project/pond.md): published depth, access questions and survey plan.
- [Build and test plan](project/build-plan.md): design, fabrication and test steps.
- [Decision register](project/decisions.md): selected tools and open design choices.
- [AI use](project/ai-co-creation.md): tool use, review and evidence records.
- [Build journal](journal/2026-11-08-project-foundation.md): project records.
- [Licensing](LICENSE.md) and [experimental-use notice](DISCLAIMER.md).
- [Project website](https://range-et.github.io/le-boat/).

## Sailing site

Love Park is at 96 Queens Quay West.
Waterfront Toronto lists a pond depth of **20–60 cm**, approximately **8–24 inches**.
We must measure route clearances and check operating rules before sailing.
See [site research](project/pond.md) for sources and open questions.

## Optimization

Compare hull and appendage designs against a recorded baseline.
Measure drag, lateral force, stability, mass, draft, print cost and sailing control.
Keep test conditions fixed when comparing designs.
Select improvements within the safety and fabrication constraints.
Record simulation uncertainty and check selected designs with physical tests.

## Collaboration

Contributions are welcome in CAD, CFD, fabrication, sail design, testing and documentation.
Start a [repository issue](https://github.com/range-et/le-boat/issues) with a proposed task.
Use a pull request to submit changes.
Read [CONTRIBUTING.md](CONTRIBUTING.md) for source files, evidence and license requirements.

## AI use

People and AI tools develop this project together.
Codex helped with research, documentation and website code.
Record significant AI contributions and the checks applied to them.
People decide what to build and test.

## Licensing

Original CAD and documentation use **CC BY-NC-SA 4.0**.
Original code uses **PolyForm Noncommercial 1.0.0**.
Retain attribution under the applicable license.
Commercial use outside the published grants requires separate written permission.
Third-party files retain their own licenses.
See [LICENSE.md](LICENSE.md) for scope and limitations.

## Website development

GitHub Pages serves the static files in `docs/`.
Monad supplies the website UI styles and theme controls.
The pinned files and MIT license are in `docs/assets/monad/`.

1. Create the build environment: `python3 -m venv .venv`.
2. Install the build dependency: `.venv/bin/python -m pip install -r requirements-site.txt`.
3. Build reference pages: `.venv/bin/python scripts/build_site.py`.
4. Start a preview: `python3 -m http.server 8000 --directory docs`.
5. Open `http://localhost:8000`.

Pushes to `main` build and deploy the site through GitHub Actions.
