# Build and test plan

Boat tests are pending.
Complete each stage before starting dependent work.

## 1. Site and equipment

Check sailing access with the park operator.
Measure the proposed route and select recovery positions.
Weigh the receiver, servos, battery, switch, wiring and seals.
Check voltage, servo travel, current demand and radio-loss behaviour on the bench.
Set a budget before ordering the complete boat.

## 2. Mass and concept selection

Use the [mass-budget template](../templates/mass-budget.csv).
Include structure, coatings, joints, deck, hatch, fittings, rig, ballast and electronics.
Keep estimates and measurements in separate columns.
Keep a separate mass contingency.
Select ballast after estimating the other component masses.

Compare a shallow fin and bulb, a wider shallow ballast arrangement, and a removable or adjustable appendage.
Check lateral resistance, stability, grounding loads and assembly joints.
An adjustable fin needs a positive lock.
Moving ballast changes stability.
Use hydrostatic calculations and physical tests to select the arrangement.

## 3. CAD and calculations

Use Rhino and Grasshopper for geometry.
Use git-cad for change management after checking its available workflow.
Follow the [tool plan](tools-and-optimization.md).
Keep editable source, parameter values, units and revision IDs.
Record the waterline datum and axis directions.
Export STEP files where suitable and meshes for fabrication.
Record mesh units and export settings.

Calculate displacement at the intended waterline.
Record the assumed water density.
In freshwater, approximately one litre of displacement supports one kilogram.
Calculate trim, freeboard, total draft and the centres of mass and buoyancy.
Check stability across the required heel range.
Check where water can enter the hull during heel.
Assess recovery after a knockdown separately from initial stability.

Define mast, keel and rudder load paths.
Check actuator travel, sheet routing, seals, maintenance access and component clearances.
Geometry scripts use the software license.
Generated models use the CAD license to the extent project rights subsist.
A file-specific notice can specify different terms.

## 4. CFD and optimization

Use Hawa for hull, keel and rudder cases.
Start with a baseline and simple appendage studies.
Record geometry, speed, fluid properties, boundaries, grid and solver settings.
Check convergence and sensitivity to grid and domain size.
Compare drag and lateral force only where the available solver outputs support those measures.

Use the objectives and constraints in the [optimization plan](tools-and-optimization.md).
Check mass, draft, stability and fabrication limits for each candidate.
Keep physical conditions consistent during comparisons.
Record uncertainty and adverse effects with each proposed improvement.
Check selected candidates with physical tests.

## 5. Fabrication samples

Print joint and shell samples first.
Record filament, drying, nozzle, layer height, walls, orientation and slicer version.
Check sealing, bonding, water exposure, creep and fit.
Check the intended weight and units of the original “75oz fiberglass” note before buying cloth.

For composite trials, record cloth weight, resin, fibre/resin mass, cure schedule and material compatibility.
Support thin prints during vacuum bagging.
Test the vacuum level on a spare sample.
Weigh the cured sample and check deformation, adhesion and leaks.
Select the construction method after these checks.

## 6. Assembly and controlled water tests

Weigh the completed assembly against the budget.
Check ballast retention, rig attachment, sheet travel, rudder stops, hatch seals and retained flotation.
Start with a 30-minute leak test in controlled water.
Use dummy equipment or protect the electronics.
Record water ingress and trim.
Find and correct leaks before sailing.

Test flotation after flooding and capsize with immediate recovery available.
Set a heel and recovery criterion before the test.
Record the rig and ballast configuration.
Check transmitter loss and low battery with the boat restrained.
A possible failsafe releases sheet tension.
Check that the equipment supports this response.
The response does not guarantee recovery to shore.

## 7. Sailing trials

Start in light wind within recovery reach.
Check operating arrangements before release.
Record configuration, wind, gusts, tacks, steering, grounding, ingress and battery use.
Demonstrate controlled sailing in both directions and a repeatable tack.
Demonstrate recovery from dry land.
Set wind and endurance limits from measured trials.

After a revision, repeat checks for affected functions and unresolved issues.
Record successful and failed trials in dated journal entries.
Check assembly instructions through a documented repeat build.

## Release files

Include editable CAD, scripts, neutral exports, dimensioned drawings, BOM, print settings, sail patterns and rig settings.
Add assembly instructions, sealing details, test reports, limitations and licenses.
Link each test to its design revision.
Use git-cad records to track CAD changes.
Assess storage needs before adding large binary histories.
