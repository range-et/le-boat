# Tool notes

Updated November 8, 2026.

## CAD

I’m using Rhino, Grasshopper and Blender for geometry, with [git-cad](https://github.com/range-et/git-cad) for CAD management.
The git-cad project is in specification/prototype development.
Its setup for this boat remains pending.
Reference revision: [97b8143](https://github.com/range-et/git-cad/tree/97b81437a5142bcb9dba4cdee71a97eb93bab12c).

## Print preparation

I’m using Orca Slicer to prepare prints for the Bambu A1 mini.
Print settings and orientations will be recorded with the build notes.

## CFD

[Hawa](https://github.com/range-et/hawa-cfd) will help explore flow around the hull, keel and rudder.
I want to compare shapes as the design develops, including their effects on drag and lateral force.
Weight, stability, shallow draft and printability will also affect the choices.
Boat geometry and CFD cases are still ahead.

The journal will include geometry revisions, case settings and results when these experiments start.
A submerged flow study has limits, including the absence of free-surface waves and sail-driven motion.
Physical tests will provide more information about the completed boat.
Reference revision: [c04d7db](https://github.com/range-et/hawa-cfd/tree/c04d7db6529330687cc658838b0bb0b5d00b69ad).

## Website

The site uses [Monad System](https://github.com/range-et/monad_system) for its UI.
The CSS, JavaScript and MIT license are stored in `docs/assets/monad/`.
Vendored revision: [358d055](https://github.com/range-et/monad_system/tree/358d0559da407897957a5817b24f9ebd8774b791).
Project CSS adds the page layout and responsive behaviour.

For updates, copy both build files and the license from one upstream revision.
Keep generated Monad files unchanged and update this version record.
