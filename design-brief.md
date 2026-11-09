# Le Boat design brief

November 8, 2026 · Revision 0.3 · Concept stage

## Purpose

Design and build a small RC sailboat for Love Park in Toronto.
Use wind in cloth sails for all propulsion.
Use a battery for the receiver and sail/rudder actuators.
The DragonForce 65 provides an initial reference for the arrangement.
Select dimensions from the pond, equipment, stability and fabrication limits.

The project includes CAD, home fabrication, CFD, assembly and water tests.
People and AI tools develop the project together.
Record tool use, design choices, calculations and test results.
Contributions are welcome through repository issues and pull requests.

## Tools

- [git-cad](https://github.com/range-et/git-cad): manage CAD revisions and comparisons when the required workflow is available.
- [Monad System](https://github.com/range-et/monad_system): supply website tokens, type, layout and UI components.
- [Hawa](https://github.com/range-et/hawa-cfd): model flow around the hull, keel and rudder in Rhino and Grasshopper.

Use the [tool and optimization plan](project/tools-and-optimization.md) for version records and setup checks.
git-cad is in specification/prototype development.
Boat CAD management and CFD cases remain pending.
Le Boat work does not change Hawa's development scope.

## Use and sailing site

The operator should carry the boat and transmitter from home.
Provide a removable rig, protective cradle and accessible controls.
The operator must launch and recover the boat from dry land.
Set cost, transport size, setup time and session endurance targets after selecting equipment.

Love Park is at 96 Queens Quay West.
[Waterfront Toronto's fact sheet](https://www.waterfrontoronto.ca/sites/default/files/2023-06/Love%20Park%20Fact%20Sheet_0.pdf) lists pond depth as **200–600 mm**, approximately **8–24 inches**.
The earlier 18-foot estimate conflicts with this source.
Measure route depths, obstructions and fill conditions before selecting an operating area.
Check operating rules with the park operator.
See [site research](project/pond.md) for the survey plan.

## Proposed dimensions and targets

These values define the first study.
Calculations and tests must determine the final requirements.

| Parameter | Initial study | Required evidence |
| --- | --- | --- |
| Hull length | 350–450 mm | Equipment fit, displacement, transport and stability |
| Loaded draft | Investigate 150 mm or less, including ballast and rudder | Measured route with at least 50 mm clearance. Increase margin for uncertainty and operating conditions. |
| Beam, hull depth and freeboard | Open | Hydrostatics, heel, water entry and equipment access |
| Displacement and ballast | Open | Component masses, finished structure, rig and contingency |
| Rig and sail area | Removable rig. Consider a smaller sail option. | Righting capacity, sheet travel and gust response |
| Wind range and endurance | Open | Measured wind, gusts and battery use |
| Cost and setup time | Open | BOM and timed assembly trial |

At 200 mm water depth, a 150 mm draft leaves a nominal 50 mm margin.
Actual clearance depends on fill level, obstructions, heel and trim.
A shorter fin reduces the ballast lever arm.
Recalculate stability and rig size after any fin or ballast change.

## Systems and interfaces

| System | Design requirements |
| --- | --- |
| Hull and deck | Displacement, trim, freeboard, sealed joints, hatch coaming, gasket, drainage and reserve flotation |
| Keel and ballast | Lateral resistance, righting moment, ballast retention, grounding loads, secure attachment and watertight trunk |
| Rudder | Draft, section, area, stock support, sealed penetration, actuator torque, travel and stops |
| Rig and sails | Mast support, boom, sail patterns, rigging, tension adjustment, sail balance and sheet routing |
| Controls | Compatible receiver, battery and actuators. Check current draw, switch access, antenna position and failure response. |
| Recovery and transport | Visible hull, retained flotation, reachable recovery point, shore equipment, cradle and rig storage |
| Fabrication and maintenance | Printable sections, tolerances, alignment, bonding, sealing, reinforcement, replaceable parts and repair access |

The boat has no propulsion motor.
Establish a recovery method for calm conditions and control failure.
Keep temporary test tethers clear of people, wildlife and pond equipment.
Check recovery before free sailing.

## Manufacturing limits

Use a **Bambu A1 mini** for printed parts.
The [manufacturer's guide](https://cdn1.bambulab.com/documentation/quick-start-f507128172bdf/Quick%20start%20guide%20-%20A1%20mini-EN.pdf) gives a nominal **180 × 180 × 180 mm** build volume.
Check each part, joint, support and adhesion margin in the slicer.
Select shell thickness after choosing filament, nozzle, settings and reinforcement.

If the hull requires several prints, design alignment, bonding, sealing and assembly access into the joints.
Include resin, laminate, coatings, adhesive, fittings and fasteners in the finished mass.
Compare a printed structural shell with printed tooling before selecting the construction method.

## Component choices

| Component | Initial option | Open choices |
| --- | --- | --- |
| Hull | Small RC yacht arrangement | Form, dimensions, waterline, segmentation and deck |
| Shell | Printed structure with possible composite reinforcement | Material, walls, orientation, joints and tooling role |
| Keel | Fin with a symmetric airfoil section | Span, chord, thickness, section, mount and load path |
| Ballast | Weight below the hull | Material, mass, shape, depth and secure retention |
| Rudder | Stern rudder | Section, area, stock, bearings, linkage and actuator |
| Mast | Possible carbon rod | Length, diameter, stiffness and support |
| Sails | Cloth sails | Material, area, pattern, rig and adjustment |
| Controls | Radio, battery and sail/rudder actuators | Components, voltage, travel, current, seals and access |

Select ballast and rudder sections separately from the keel section.
Check their effects on drag, stability, loads and grounding.

## Composite trials

The initial proposal uses glass fabric and resin over a printed structure, with vacuum-bag consolidation.
The original material note says **“75oz fiberglass.”**
Check the intended fabric weight and units before buying material or estimating laminate mass.
This specification remains unresolved.

Select reinforced areas, resin, layer count, fibre directions and cure conditions through sample tests.
Support prints during bagging and check their resistance to vacuum pressure.
Record finished sample mass, deformation, bonding and water resistance.
Select the construction method after these trials.

## Engineering and optimization

Create a complete component mass budget before selecting ballast.
Calculate displacement, trim, centres of mass and buoyancy, freeboard and stability.
Check mast, keel, rudder and joint loads.
Check water entry during heel and recovery after knockdown.

Use Hawa to compare flow around the hull and appendages.
Start with an explicitly submerged case and simple appendage studies.
Compare candidates at fixed physical conditions.
Check grid sensitivity, domain sensitivity and convergence.
Record pressure, velocity, drag and lateral force where supported.

Optimize drag and lateral resistance within limits for draft, stability, mass and fabrication.
Compare print material, print time, joint count, tacking and steering response.
Record trade-offs and uncertainty.
Use physical tests to check selected designs.

A submerged single-fluid case omits free-surface waves and sail-driven motion.
These effects need suitable models or experiments.
Use separate structural, hydrostatic and fabrication checks.
See the [optimization procedure](project/tools-and-optimization.md).

## First outputs

1. A dimensioned Rhino concept and assembly layout.
2. A component mass budget and hydrostatic assessment.
3. A print layout with joints, supports and build-volume checks.
4. Shell, joint and composite sample results.
5. Parametric hull, keel, ballast and rudder source with revision records.
6. Baseline CFD cases and controlled design comparisons.
7. A recovery plan and configuration-specific water tests.

## Test requirements

Follow the [build and test plan](project/build-plan.md).
Set acceptance criteria before each test.
Record the configuration, conditions, measurements and failures.

The first sailing prototype must meet the selected flotation, trim, stability and leak criteria.
It must respond to rudder and sail controls.
It must sail in both directions, tack and permit recovery from dry land.
Boat tests remain pending.
Wind and endurance limits remain open.

## Documentation and collaboration

Keep editable CAD, scripts, exports, drawings, BOM, print settings, sail patterns and assembly instructions.
Use git-cad revision records when the required workflow is available.
Link each simulation and test to its geometry and settings.
Publish design changes and build results in the GitHub Pages journal.
Label planned work, renders, simulations and physical results.

Use short, direct English with ASD-STE100 sentence structure.
Keep [AI use](project/ai-co-creation.md) visible in the project record.
Record tools, significant contributions, completed checks and uncertainty.
Invite contributions in CAD, CFD, fabrication, sails, electronics and testing.
See [CONTRIBUTING.md](CONTRIBUTING.md).

Original CAD and documentation use CC BY-NC-SA 4.0.
Original code uses PolyForm Noncommercial 1.0.0.
Commercial use outside those grants requires separate permission.
Keep third-party licenses and attribution.
See [LICENSE.md](LICENSE.md) and [DISCLAIMER.md](DISCLAIMER.md) for scope and limitations.

Update the [decision register](project/decisions.md) when choices change.
The next tasks are site checks, equipment masses and the baseline hull/ballast/rig arrangement.
