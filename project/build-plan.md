# Build and verification plan

No tests listed here have passed yet. These are the gates for progressing the prototype.

## 1. Site and equipment

Confirm sailing access and survey the proposed route. Weigh candidate receiver, sail servo/winch, rudder servo, battery, switch, wiring and seals. Check voltage compatibility, servo travel, current demand and receiver failsafe behaviour on the bench. Set a budget and identify locally obtainable materials before ordering the complete boat.

## 2. Mass and concept selection

Use the [mass-budget template](../templates/mass-budget.csv). Include shell, joints, laminate, coatings, deck/hatch, rig/sails, fasteners, keel/ballast, rudder and all electronics. Distinguish estimates from measurements and keep a separate contingency. Do not allocate ballast until non-ballast mass is credible.

Compare a shallow fixed fin/bulb, a wider shallow ballast arrangement, and a removable/depth-adjustable appendage. Document lateral resistance, righting moment, grounding, joints and sailing practicality. An adjustable fin must positively lock; lifting ballast changes stability. Choose with hydrostatics and a physical righting test, not resemblance to a larger yacht.

## 3. CAD and calculations

Model a watertight closed hull and compute displacement at the intended waterline. In freshwater, approximately one litre of displacement supports one kilogram; use a recorded water-density assumption. Show trim, freeboard, total draft, centre of buoyancy and an assembly-based centre of mass. Check heel conditions, downflooding openings and a righting-arm curve over the relevant heel range; positive initial stability alone does not demonstrate recovery from knockdown.

Define mast, keel and rudder load paths, servos and sheet travel, deck access, seals and maintenance clearances. Maintain millimetres, named axes, an explicit waterline datum and revisioned parameter sets. Keep editable Rhino/Grasshopper or script source, and export STEP where suitable plus fabrication meshes with units and tessellation settings. A script that defines boat geometry follows the software license; its generated model follows the CAD license to the extent project rights subsist, unless a file-specific notice states otherwise.

## 4. Fabrication coupons

Print joint and shell samples first. Record filament, drying, nozzle, layer height, wall strategy, orientation and slicer version. Assess sealing, bonding, wet behaviour, creep and dimensional fit. Clarify the original “75oz fiberglass” specification before buying cloth or calculating laminate mass; no replacement weight has been assumed.

If testing glass/resin, record exact cloth units, resin, fibre/resin mass, cure schedule and compatibility. Support thin prints during vacuum bagging and test vacuum level on a sacrificial coupon. Weigh the finished coupon and examine deformation, adhesion and leaks before selecting the construction method.

## 5. Dry assembly and controlled water tests

Weigh the finished assembly and compare with the budget. Check keel/ballast retention, rig attachment, sheet travel, rudder stops, hatch seals and flotation retention. Perform an initial 30-minute static leak test in controlled water with dummy equipment or protected electronics. Record water ingress and trim; any ingress needs diagnosis before sailing.

Test flotation after simulated flooding and capsize in controlled conditions with immediate recovery available. Define and record a heel/recovery criterion before the test, including rig and ballast configuration. Check transmitter loss and low battery with the boat restrained. A candidate failsafe eases sheets; verify that the actual equipment supports it and do not assume it brings the boat ashore.

## 6. First sailing trials

Start within recovery reach in light air, after operating arrangements are confirmed. Establish measured wind and gust limits from trials rather than publishing an unsupported rating. Record configuration, weather, tacks, steering response, grounding, ingress and battery use. Demonstrate controlled sailing in both directions, a repeatable tack, and retrieval from dry land. A calm patch can strand a wind-only boat: prove the recovery plan before releasing it.

Repeat after revisions only for affected behaviour and unresolved issues. Build instructions become a tested recipe only after another assembly or a sufficiently documented reproduction. Store measured evidence, including failed trials, in dated journal entries.

## Release package

Editable CAD and scripts; neutral exports; drawings with tolerances; BOM with measured masses and costs; print profiles and orientation; sail patterns and rig settings; assembly/sealing instructions; configuration-specific test reports; limitations; attribution and licenses. Add a revision manifest so geometry, settings and results remain traceable. Keep large binary CAD revisions manageable; consider Git LFS before adding substantial model history.
