from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import os


def generate_pdf_report(
    patient_name,
    heart_risk,
    diabetes_risk,
    cancer_risk,
    recommendations
):

    os.makedirs("reports", exist_ok=True)

    pdf_path = f"reports/{patient_name}_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Multi Disease Prediction Report",
        styles["Title"]
    )

    content.append(title)
    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"<b>Patient Name:</b> {patient_name}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            f"<b>Heart Disease Risk:</b> {heart_risk}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Diabetes Risk:</b> {diabetes_risk}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Breast Cancer Risk:</b> {cancer_risk}%",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    for recommendation in recommendations:

        content.append(
            Paragraph(
                f"• {recommendation}",
                styles["Normal"]
            )
        )

    doc.build(content)

    return pdf_path