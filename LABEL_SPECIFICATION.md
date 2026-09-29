# Label specification

## Source fields

Primary metadata fields used for task construction

- `scp_codes`
- `patient_id`
- `strat_fold`

The diagnostic superclass mapping is read from `scp_statements.csv`.

## Diagnostic classes

The five PTB-XL diagnostic superclasses are

- NORM
- MI
- STTC
- CD
- HYP

A record can carry more than one superclass.

## SCP likelihood

Each diagnostic SCP statement can carry a likelihood value.

The primary label rule uses a common threshold of 50%.

A superclass is considered present for the primary task if at least one mapped SCP statement in that superclass has likelihood >= 50.

## Primary HYP task

Positive

- HYP likelihood >= 50

Negative

- NORM likelihood >= 50
- HYP likelihood < 50

Excluded

- HYP likelihood < 50
- NORM likelihood < 50

If both HYP and NORM reach 50, the record is positive.

Version 1.0.3 metadata counts before waveform technical exclusions

- positive = 2,258
- negative = 9,434
- excluded = 10,107

## Primary MI task

Positive

- MI likelihood >= 50

Negative

- NORM likelihood >= 50
- MI likelihood < 50

Excluded

- MI likelihood < 50
- NORM likelihood < 50

If both MI and NORM reach 50, the record is positive.

Version 1.0.3 metadata counts before waveform technical exclusions

- positive = 4,134
- negative = 9,438
- excluded = 8,227

## Sensitivity label rule

The prespecified label-definition sensitivity uses superclass presence without a likelihood threshold.

Positive

- target superclass appears in the mapped diagnostic statements

Negative

- NORM appears
- target superclass does not appear

Excluded

- neither target nor NORM appears

Target-plus-NORM remains target-positive.

## Unit of analysis

Labels are assigned at the ECG-record level.

Patient identity is retained for patient-aware folds and patient-level uncertainty.

A patient can therefore contribute records with different labels at different examinations.

## Interpretation boundary

These are operational PTB-XL phenotype definitions.

They are not independent adjudications of overall patient health, active myocardial infarction or another clinical endpoint beyond the source ECG annotation structure.
