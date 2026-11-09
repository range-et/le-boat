# Tools and optimization

Updated November 8, 2026.

## CAD management: git-cad

Use [git-cad](https://github.com/range-et/git-cad) to manage CAD changes.
The upstream project is in specification/prototype development.
Its specification describes native snapshots, OpenUSD exchange, visual comparisons and conflict resolution.
Rhino and Blender are the initial adapter targets.
Le Boat does not yet contain an installed git-cad workflow.

Before the first CAD baseline, check the available implementation against the specification.
Test a save, change, comparison and restore cycle with disposable geometry.
Record units, axes, waterline datum, object IDs and the git-cad revision.
Keep editable native files, parameter values and neutral exports together.
Link each design revision to its drawings, mass budget, simulation cases and test records.
Record any unavailable function and its temporary manual procedure.

Reference revision: [97b8143](https://github.com/range-et/git-cad/tree/97b81437a5142bcb9dba4cdee71a97eb93bab12c).
This reference does not establish that the proposed functions are implemented.

## Website UI: Monad System

Use [Monad System](https://github.com/range-et/monad_system) for tokens, type, layout and components.
The site loads its generated CSS and JavaScript locally.
It uses Monad header and button components, Strata color tokens and the theme control.
Project CSS defines page layout and responsive behaviour.
Keep colors in upstream tokens and use Helvetica system fonts.

Vendored revision: [358d055](https://github.com/range-et/monad_system/tree/358d0559da407897957a5817b24f9ebd8774b791).
Files: `docs/assets/monad/monad.css`, `monad.js` and `LICENSE`.
Keep generated files unchanged.
For updates, copy both build files and the license from one upstream revision.
Update this record and check the site in both themes and at narrow widths.

## CFD: Hawa

Use [Hawa](https://github.com/range-et/hawa-cfd) for hull, keel and rudder flow studies in Rhino and Grasshopper.
The upstream solver uses the lattice Boltzmann method.
Start with a simple appendage case and check the available force outputs.
Define each case before comparing designs.

Record these inputs and outputs:

- Geometry revision and dimensions.
- Fluid properties, speed and Reynolds number.
- Domain size, boundaries, grid spacing and time step.
- Solver settings, device, run duration and convergence checks.
- Force axes, drag, lateral force and averaging interval, where supported.
- Grid and domain sensitivity, uncertainty and known limitations.

Reference revision: [c04d7db](https://github.com/range-et/hawa-cfd/tree/c04d7db6529330687cc658838b0bb0b5d00b69ad).
Record the installed revision when creating a case.
No Le Boat CFD case or optimization result exists yet.

A submerged single-fluid model can compare underwater flow within its assumptions.
Free-surface waves, flotation and sail-driven motion need suitable models or physical tests.
Check solver capabilities before selecting an objective.
Le Boat work does not change Hawa's development scope.

## Optimization procedure

1. Define a baseline hull, appendages, ballast and rig.
2. Check mass, displacement, draft, freeboard and stability.
3. Select parameters and limits before running a search.
4. Compare candidates under the same physical conditions.
5. Check promising candidates with finer grids and larger domains.
6. Build and test selected candidates.
7. Record the selected design and reasons for the choice.

Candidate parameters include hull beam, waterline shape, fin chord, fin section and rudder area.
Keep displacement and intended operating conditions consistent during each comparison.
Use several cases when performance changes with speed, heel or leeway.
Leeway is the angle between the boat's heading and its direction through the water.

## Objectives and constraints

| Measure | Direction | Required check |
| --- | --- | --- |
| Hull and appendage drag | Reduce at defined speed and attitude | Compare converged results and uncertainty |
| Keel lateral force | Meet the required side force with acceptable drag | Compare at defined leeway and heel |
| Stability | Maintain the selected righting and recovery criteria | Calculate hydrostatics and test the assembly |
| Draft | Investigate 150 mm or less | Check loaded geometry against a measured route |
| Mass | Meet displacement and ballast budgets | Weigh the completed parts |
| Fabrication | Reduce material, print time and difficult joints | Compare print layouts and sample parts |
| Handling | Improve tacking and steering | Run repeatable sailing trials |

Evaluate these measures together.
A drag reduction can increase weight, reduce stability or make a part difficult to build.
Report those effects with the result.
Choose numerical targets after the first mass budget and baseline cases.

## Collaboration

Propose a task through a repository issue.
Submit editable geometry, case settings, data and a short explanation with each contribution.
Use the same baseline for shared comparisons.
Keep failed cases and rejected candidates when they explain a design choice.
Third-party tools retain their own licenses.
