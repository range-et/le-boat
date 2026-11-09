# About the boat

November 8, 2026 · Early design

I’m building a small, wind-powered RC sailboat for Love Park in Toronto.
This site records my build journey, from the first CAD model to printing, assembly and sailing.
The project is collaborative. Suggestions, shared experiments and contributions are welcome.

## The boat

The DragonForce 65 is an initial reference for the layout.
The hull, keel, ballast, rudder, mast and cloth sails will form a complete model yacht.
A battery will power the radio receiver and servos for steering and sail trim.
Wind will provide all propulsion.
The final dimensions and equipment are still open.

## Constraints I’m designing around

I’m using a **Bambu A1 mini**.
Its nominal build volume is **180 × 180 × 180 mm**.
Part sizes, print orientation and any hull sections will fit that printer.
Joints, sealing and finished weight will affect the construction.

The boat is intended for the shallow pond at Love Park.
[Waterfront Toronto](https://www.waterfrontoronto.ca/sites/default/files/2023-06/Love%20Park%20Fact%20Sheet_0.pdf) lists a depth of **20–60 cm**, approximately **8–24 inches**.
That limits the keel and rudder depth and affects the ballast arrangement.
Actual clearance will depend on the water level and the part of the pond being sailed.

I’m considering fiberglass and resin reinforcement over printed parts, possibly with vacuum bagging.
The fabric weight, resin, shell thickness and construction method are still open.
The original “75oz fiberglass” material note needs clarification.

## Tools

- Rhino and Grasshopper for geometry.
- [git-cad](https://github.com/range-et/git-cad) for CAD management.
- [Hawa](https://github.com/range-et/hawa-cfd) for flow studies around the hull, keel and rudder.
- [Monad System](https://github.com/range-et/monad_system) for the website UI.

CFD will help explore design changes as the geometry develops.
Prints and sailing tests will show how those choices work in practice.
[Tool notes](project/tools-and-optimization.md) record versions and current setup.

## Where things stand

The project is at the brief and research stage.
The website and initial notes are in place.
Boat geometry, prints, simulations and water tests are still ahead.
Next I’ll explore the hull layout, equipment weight and a shallow keel/ballast arrangement.

## Collaboration and AI

I’m developing this project with AI tools and documenting their contribution.
Codex helped with the research, documentation and website.
The [build journal](journal/2026-11-08-project-foundation.md) will record design choices, progress and problems as they occur.
Ideas and contributions are welcome through [GitHub](https://github.com/range-et/le-boat/issues).

Original CAD and documentation use CC BY-NC-SA 4.0.
Original code uses PolyForm Noncommercial 1.0.0.
Commercial use outside those grants needs separate permission.
See [licensing](LICENSE.md) and the [experimental-use notice](DISCLAIMER.md).
