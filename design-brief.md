# Le Boat design brief

November 8, 2026 · Revision 0.2 · Concept stage

Design and build a small RC sailboat inspired by a smaller version of the
DragonForce 65. The boat should be practical to manufacture and assemble at home,
using a Bambu A1 mini for printed parts and potentially fiberglass reinforcement.
The exact size, construction method and performance targets remain to be chosen.
The intended setting is neighbourhood sailing on the Love Park pond in Toronto.
This is an unmanned model yacht: wind in sails provides all propulsion. Battery
power is allowed for the receiver, rudder servo and sail-trim actuator only; no
propeller, auxiliary propulsion or powered recovery drive is included.

## Design intent

Develop the boat as a complete assembly: hull, rudder, keel, ballast, mast and
rigging, with provision for radio control and internal equipment. Use Rhino to
explore the geometry alongside manufacturing limits, shell thickness, component
weights, strength requirements and assembly details.

This should also become a practical Hawa use case: investigate flow around a
hull with its keel and rudder, while relating geometry choices to a boat that can
actually be made. The boat design is its own project; it does not expand Hawa's
current 0.5 development scope.

## People, place and use

Design for someone who can carry the boat and transmitter from home, rig it at
the pond edge, sail for a short session, recover it from dry land, and take it home
without needing a car or waterside workshop. Carry protection, a removable rig,
accessible controls and repairable parts belong in the design brief. Carry size,
ready-to-sail time, session endurance and total cost need explicit targets after
an equipment shortlist; none is yet a demonstrated capability.

The intended water is Love Park at 96 Queens Quay West. Google Maps was checked
for the location; [Waterfront Toronto's fact sheet](https://www.waterfrontoronto.ca/sites/default/files/2023-06/Love%20Park%20Fact%20Sheet_0.pdf)
gives pond depth as **200–600 mm (about 8–24 inches)**. The initial 18-foot claim
conflicts with that source and is not used. Maps are not a depth survey. See
[site research](project/pond.md) for sources, operating-rule uncertainty and the
required visit. Permission/access, actual water levels, obstacles and wind
conditions remain unverified.

## Provisional design envelope

These are proposed study inputs, not settled dimensions or approved plans.

| Parameter | Starting study | How it becomes a requirement |
| --- | --- | --- |
| Hull length | Explore 350–450 mm | Equipment fit, displacement, transport and stability comparison |
| Overall loaded draft | Investigate at or below 150 mm, including ballast and rudder | Verify a route with at least 50 mm clearance under all appendages; increase margin for measured uncertainty/conditions |
| Beam, hull depth and freeboard | Open | Hydrostatics, downflooding, heel and access layout |
| Sailing displacement and ballast | Open | Measured equipment masses plus finished structure/rig and contingency |
| Rig and sail area | Open; investigate a simple removable rig and smaller wind option | Match righting capacity, sheeting and observed gust response |
| Wind range and endurance | Open | Controlled trials with recorded wind, gusts and battery use |
| Cost and setup time | Open | BOM and a timed dry setup trial |

A published shallow point of 200 mm minus a proposed 150 mm draft leaves only a
nominal 50 mm margin. That arithmetic is not evidence of route clearance. Measure
and revise; a shorter fin reduces the ballast lever arm and may make stability,
weight or rig targets incompatible. Do not solve draft by simply shortening a
DragonForce-style keel without reevaluating the complete boat.

## Whole-boat systems and interfaces

| System | Design work and interfaces |
| --- | --- |
| Hull/deck | Displacement, trim/freeboard, shell joints, hatch coaming/gasket, reserve flotation, drainage and handling |
| Keel/ballast | Lateral resistance, righting moment, secure ballast containment, grounding load path, replaceable/removable attachment and watertight trunk |
| Rudder | Total draft, section/area, stock support, sealed penetration, servo torque/travel and mechanical stops |
| Rig/sails | Mast support, boom, sail material/patterns, standing/running rigging, tension adjustment, sail balance, sheet routing and unobstructed release |
| Controls | Compatible receiver/battery/actuators, linkage and sheet travel, current draw, switch access, antenna routing, failsafe and low-battery behaviour |
| Recovery/transport | Visible hull, retained flotation, a reachable recovery point, shore retrieval equipment and protective cradle/rig stowage |
| Fabrication/maintenance | Printable segments, tolerances, alignment, bonding/sealing, reinforcement, replaceable wear parts and access for repairs |

No propulsion motor also means no motor to rescue a becalmed boat. Prove a
shore-based recovery method before free sailing. Keep any temporary tether under
control during near-shore tests; it must not create hazards or stand in for a
workable sailing/recovery plan.

## Manufacturing constraints

- Manufacture at home with a **Bambu A1 mini** as the available 3D printer.
- The [manufacturer's A1 mini guide](https://cdn1.bambulab.com/documentation/quick-start-f507128172bdf/Quick%20start%20guide%20-%20A1%20mini-EN.pdf) lists a nominal **180 × 180 × 180 mm** build volume.
  Fit parts, joints, supports and adhesion margins in the actual slicer profile;
  nominal machine limits are not the usable dimensions of every orientation.
- Treat printable shell thickness as a design constraint. Select actual values
  after choosing material, nozzle, print settings and reinforcement approach.
- If the hull needs multiple prints, design their joints, alignment, sealing and
  assembly access as part of the hull rather than as an afterthought.
- Account for the finished construction, including reinforcement, resin, joins
  and fittings, when estimating dimensions and weight.

## Initial component ideas

| Component | Starting idea | Decisions still open |
| --- | --- | --- |
| Hull | Smaller sailboat inspired by the DragonForce 65 | Overall dimensions, hull form, target displacement, printed sections and deck arrangement |
| Printed shell | Thin printed structure with possible composite reinforcement | Filament, thickness, print orientation, joints and whether the print remains in the finished hull or serves as tooling |
| Keel | Fin using a symmetric airfoil section | Section, span, chord, thickness, attachment and structural load path |
| Ballast | Weight at the lower end of the keel | Material, mass, shape, position and secure attachment |
| Rudder | Rudder integrated into the complete hull/appendage design | Profile, area, stock, bearings, linkage and servo arrangement |
| Mast | Possibly a carbon rod | Length, diameter, stiffness, support and attachment |
| Sails and rigging | Small RC sailboat rig | Sail area, layout, materials, adjustment and control arrangement |
| Internal equipment | Radio control, power and sail/rudder actuation | Components, access, waterproofing and their contribution to the mass budget |

The symmetric airfoil idea applies initially to the keel fin. Ballast shape and
rudder section should be selected explicitly rather than assuming all underwater
parts use the same profile.

## Fiberglass and forming concept

The initial idea is to cover the printed construction with fiberglass and resin,
then use a vacuum bag to consolidate/form the laminate.

The material was described in the initial brief as **“75oz fiberglass.”** Preserve
this as an unresolved specification: confirm the intended fabric weight and units
before selecting materials or estimating laminate thickness and mass. Do not
silently interpret it as another fabric weight.

Confirm which parts receive reinforcement, the resin system, layer count and
layup, and how the printed structure or tooling will be supported during bagging.
The vacuum-bagging construction method is a candidate to test, not a settled
manufacturing process.

## Geometry and engineering questions

- What size gives a useful small RC sailboat while remaining practical to print,
  assemble and equip?
- What is the complete mass budget, including printed parts, laminate, resin,
  keel, ballast, rig, battery and electronics?
- Where are the centres of mass and buoyancy for the intended draft, and what
  flotation and stability checks are needed?
- How should hull shell thickness, local reinforcement and joints support the
  keel, ballast, mast and rudder loads?
- How should the hull, keel and rudder geometry work together, including their
  attachment details and watertight penetrations?
- What can be checked geometrically or with hand calculations, and what needs
  structural analysis, flow simulation or a physical test?

## Flow analysis direction

Begin with clearly bounded studies of underwater appendages and, where useful,
an explicitly submerged hull/keel/rudder assembly. Compare geometry variants at
consistent physical conditions and inspect pressure, wake and vector-field slices.

A submerged single-fluid case does not represent the complete sailing boat at
the water surface. Surface waves, flotation, heel/trim response and sail-driven
motion need their own appropriate models or experiments. Likewise, CFD does not
establish shell strength or printability; keep the manufacturing, structural and
hydrostatic checks explicit.

## First design outputs

1. A dimensioned concept and assembly layout in Rhino, with the reference boat
   and intended size reduction recorded.
2. A preliminary component mass budget and flotation/stability assessment.
3. A print layout showing build-volume fit, hull segmentation and assembly joints.
4. A proposed shell/reinforcement construction, supported by small print and
   laminate trials before committing to a complete hull.
5. Parametric hull, keel, ballast and rudder geometry with clearly recorded inputs.
6. A bounded simulation and physical-test plan tied to specific design questions.

## Decisions to make next

Choose the overall size or target displacement; confirm printer build limits;
select an initial construction approach; clarify the fiberglass specification;
and estimate the equipment, rig and ballast masses. These decisions should guide
the first hull geometry rather than treating the project as a purely scaled mesh.

## Validation and evidence

Follow the [build and test plan](project/build-plan.md): site/access and recovery
check; equipment mass budget; hydrostatics and stability; print/bond/laminate
coupons; dry assembly and controls; controlled leak/flotation/heel tests; then
short sailing trials within recovery reach. Record configuration and acceptance
criteria before each test, including failures. Do not call the design validated
because a CAD assembly looks complete or a CFD image looks plausible.

The first physical success is a recoverable boat that floats to its predicted
trim, stays dry in a controlled leak test, responds reliably to steering and sail
trim, and sails and tacks under recorded conditions without grounding. Speed,
racing class compliance and optimization are secondary to an operable first boat.
No tests have yet passed and no wind rating is assigned.

## Documentation, licensing and co-creation

Maintain editable CAD and parametric source, neutral exports, drawings, BOM,
print/laminate settings, assembly instructions and a dated build journal tied to
revision IDs. The GitHub Pages site should explain the intent and document the
actual making, including failed prints and rejected designs. It must distinguish
planned work from completed work and renders from photographs.

Be explicit that the project is [co-created with AI](project/ai-co-creation.md).
Record tools, consequential suggestions, human checks and measured outcomes. AI
is part of the experiment, not a hidden author or a substitute for validation.

The owner requires commercial permission separately from the public grants.
Original CAD and documentation use CC BY-NC-SA 4.0; software uses PolyForm
Noncommercial 1.0.0. Preserve attribution and third-party provenance. See
[LICENSE.md](LICENSE.md) for exact scope and legal limitations, and
[DISCLAIMER.md](DISCLAIMER.md) for the experimental, as-is notice. Neither a
license nor a disclaimer guarantees zero liability or control over every
functional physical design.

Track resolutions in the [decision register](project/decisions.md). Before a
first detailed hull, prioritize the site survey and equipment masses, then choose
displacement, draft/ballast architecture and rig together.
