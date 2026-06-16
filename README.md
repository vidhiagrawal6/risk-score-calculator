# Risk Score Calculator

## Overview

The Risk Score Calculator is a Python-based application that calculates a risk score from monitoring events. It helps classify the overall risk level based on detected violations such as phone usage, multiple person presence, and face missing events.

---

## Objective

To calculate a risk score and assign a risk level (Low, Medium, or High) based on monitoring event data.

---

## Features

- Calculates risk score from monitoring events
- Assigns a risk level based on score
- Handles missing logs using default values
- Handles no-violation scenarios
- Limits maximum risk score to 100
- Interactive user input through the terminal

---

## Risk Scoring Logic

| Event Type | Weight |
|------------|----------|
| Phone Events | 12 |
| Multiple Person Events | 24 |
| Face Missing Events | 8 |

### Formula

Risk Score =

(phone_events × 12) +
(multiple_person_events × 24) +
(face_missing_events × 8)

Maximum Risk Score = 100

---

## Risk Levels

| Score Range | Risk Level |
|-------------|------------|
| 0 - 30 | Low |
| 31 - 70 | Medium |
| 71 - 100 | High |

---

## Example Input

```text
Enter phone events: 2
Enter multiple person events: 1
Enter face missing events: 3
```

## Example Output

```json
{
    "risk_score": 72,
    "risk_level": "Medium"
}
```

---

## Edge Cases Handled

### Missing Logs

If an event field is missing, its value is treated as 0.

Example:

```python
{
    "phone_events": 2
}
```

### No Violations

```python
{
    "phone_events": 0,
    "multiple_person_events": 0,
    "face_missing_events": 0
}
```

Output:

```json
{
    "risk_score": 0,
    "risk_level": "Low"
}
```

---

## Technologies Used

- Python 3
- JSON Module (Built-in)
