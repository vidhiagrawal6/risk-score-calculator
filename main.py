import json


def calculate_risk_score(events):
    """
    Calculate risk score based on monitoring events.
    """

    phone_events = events.get("phone_events", 0)
    multiple_person_events = events.get("multiple_person_events", 0)
    face_missing_events = events.get("face_missing_events", 0)

    # Risk score calculation
    risk_score = (
        phone_events * 12 +
        multiple_person_events * 24 +
        face_missing_events * 8
    )

    # Cap score at 100
    risk_score = min(risk_score, 100)

    # Determine risk level
    if risk_score <= 30:
        risk_level = "Low"
    elif risk_score <= 80:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level
    }


if __name__ == "__main__":

    print("=== Risk Score Calculator ===\n")

    phone_events = int(input("Enter phone events: "))
    multiple_person_events = int(input("Enter multiple person events: "))
    face_missing_events = int(input("Enter face missing events: "))

    events = {
        "phone_events": phone_events,
        "multiple_person_events": multiple_person_events,
        "face_missing_events": face_missing_events
    }

    result = calculate_risk_score(events)

    print("\nResult:")
    print(json.dumps(result, indent=4))