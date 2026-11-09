# Le Boat

I’m building a small, wind-powered RC sailboat for Love Park in Toronto.
This repository and website record my build journey.
The project is collaborative, and ideas and contributions are welcome.

## Where things stand

The project is at the brief and research stage.
The website and initial notes are in place.
Boat CAD, prints, simulations and water tests are still ahead.

## The build

I’m using a **Bambu A1 mini**, with a **180 × 180 × 180 mm** build volume.
The printed parts and any hull sections will fit that printer.
The shallow pond affects the keel, rudder and ballast arrangement.
Dimensions, equipment and the construction method are still open.

The DragonForce 65 is an initial reference.
Wind will provide propulsion, with battery-powered radio controls for steering and sail trim.
I’m considering fiberglass and resin reinforcement for the printed hull.

## Tools

- Rhino and Grasshopper for geometry.
- [git-cad](https://github.com/range-et/git-cad) for CAD management.
- [Hawa](https://github.com/range-et/hawa-cfd) for hull and appendage CFD.
- [Monad System](https://github.com/range-et/monad_system) for the website UI.

The [tool notes](project/tools-and-optimization.md) record versions and setup.
AI tools are part of the build process.
Codex helped with research, documentation and the website.
Amp Code also helped with earlier coding.

## Follow the build

- [Website and journal](https://range-et.github.io/le-boat/).
- [About the boat](design-brief.md).
- [Current project notes](project/decisions.md).
- [Next build steps](project/build-plan.md).
- [Love Park](project/pond.md).
- [AI use](project/ai-co-creation.md).

[Ideas and contributions](CONTRIBUTING.md) are welcome through issues and pull requests.
Original CAD and documentation use CC BY-NC-SA 4.0.
Original code uses PolyForm Noncommercial 1.0.0.
See [licensing](LICENSE.md) and the [experimental-use notice](DISCLAIMER.md).

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
