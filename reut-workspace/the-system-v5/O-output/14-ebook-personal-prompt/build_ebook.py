#!/usr/bin/env python3
"""Build the Personal Prompt Template e-book PDF using reportlab."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus.flowables import Flowable
import os

# Colors
TEAL = HexColor("#0D9488")
DARK_TEAL = HexColor("#0F766E")
LIGHT_TEAL = HexColor("#CCFBF1")
VERY_LIGHT_TEAL = HexColor("#F0FDFA")
DARK_TEXT = HexColor("#1E293B")
MID_TEXT = HexColor("#475569")
LIGHT_TEXT = HexColor("#64748B")
BG_GRAY = HexColor("#F8FAFC")
LINE_COLOR = HexColor("#E2E8F0")
WHITE = white

OUTPUT_PATH = "/Users/reutamariyo/Documents/Obsidian Vault/reut-workspace/the-system-v5/O-output/14-ebook-personal-prompt/your-personal-prompt-template.pdf"


# Custom flowables
class RoundedBox(Flowable):
    """A rounded rectangle box with optional background color."""
    def __init__(self, width, height, color=VERY_LIGHT_TEAL, stroke_color=None, stroke_width=0):
        Flowable.__init__(self)
        self.box_width = width
        self.box_height = height
        self.color = color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width

    def draw(self):
        self.canv.setFillColor(self.color)
        if self.stroke_color:
            self.canv.setStrokeColor(self.stroke_color)
            self.canv.setLineWidth(self.stroke_width)
        else:
            self.canv.setStrokeColor(self.color)
        self.canv.roundRect(0, 0, self.box_width, self.box_height, 8, fill=1, stroke=1 if self.stroke_color else 0)


class AnswerLines(Flowable):
    """Draw blank lines for writing answers."""
    def __init__(self, width, num_lines=3, line_spacing=24):
        Flowable.__init__(self)
        self.line_width = width
        self.num_lines = num_lines
        self.line_spacing = line_spacing
        self.height = num_lines * line_spacing

    def wrap(self, availWidth, availHeight):
        return (self.line_width, self.height)

    def draw(self):
        self.canv.setStrokeColor(LINE_COLOR)
        self.canv.setLineWidth(0.5)
        for i in range(self.num_lines):
            y = self.height - (i + 1) * self.line_spacing + 4
            self.canv.line(0, y, self.line_width, y)


class AccentBar(Flowable):
    """A colored accent bar."""
    def __init__(self, width, height=4, color=TEAL):
        Flowable.__init__(self)
        self.bar_width = width
        self.bar_height = height
        self.color = color

    def wrap(self, availWidth, availHeight):
        return (self.bar_width, self.bar_height)

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.roundRect(0, 0, self.bar_width, self.bar_height, 2, fill=1, stroke=0)


class SectionNumber(Flowable):
    """A large section number with teal background circle."""
    def __init__(self, number):
        Flowable.__init__(self)
        self.number = str(number)

    def wrap(self, availWidth, availHeight):
        return (50, 50)

    def draw(self):
        self.canv.setFillColor(TEAL)
        self.canv.circle(25, 25, 22, fill=1, stroke=0)
        self.canv.setFillColor(WHITE)
        self.canv.setFont("Helvetica-Bold", 22)
        self.canv.drawCentredString(25, 17, self.number)


# Styles
def get_styles():
    return {
        'cover_title': ParagraphStyle(
            'CoverTitle', fontName='Helvetica-Bold', fontSize=38,
            leading=46, textColor=DARK_TEXT, alignment=TA_CENTER,
            spaceAfter=16
        ),
        'cover_subtitle': ParagraphStyle(
            'CoverSubtitle', fontName='Helvetica', fontSize=16,
            leading=24, textColor=MID_TEXT, alignment=TA_CENTER,
            spaceAfter=40
        ),
        'cover_tagline': ParagraphStyle(
            'CoverTagline', fontName='Helvetica-Bold', fontSize=13,
            leading=20, textColor=TEAL, alignment=TA_CENTER
        ),
        'page_title': ParagraphStyle(
            'PageTitle', fontName='Helvetica-Bold', fontSize=26,
            leading=34, textColor=DARK_TEXT, alignment=TA_LEFT,
            spaceAfter=8
        ),
        'section_header': ParagraphStyle(
            'SectionHeader', fontName='Helvetica-Bold', fontSize=22,
            leading=30, textColor=DARK_TEXT, alignment=TA_LEFT,
            spaceAfter=6
        ),
        'section_sub': ParagraphStyle(
            'SectionSub', fontName='Helvetica', fontSize=13,
            leading=20, textColor=LIGHT_TEXT, alignment=TA_LEFT,
            spaceAfter=20
        ),
        'body': ParagraphStyle(
            'Body', fontName='Helvetica', fontSize=12,
            leading=20, textColor=MID_TEXT, alignment=TA_LEFT,
            spaceAfter=10
        ),
        'body_bold': ParagraphStyle(
            'BodyBold', fontName='Helvetica-Bold', fontSize=12,
            leading=20, textColor=DARK_TEXT, alignment=TA_LEFT,
            spaceAfter=6
        ),
        'question': ParagraphStyle(
            'Question', fontName='Helvetica-Bold', fontSize=12,
            leading=18, textColor=DARK_TEXT, alignment=TA_LEFT,
            spaceAfter=4
        ),
        'hint': ParagraphStyle(
            'Hint', fontName='Helvetica-Oblique', fontSize=10,
            leading=16, textColor=LIGHT_TEXT, alignment=TA_LEFT,
            spaceAfter=6
        ),
        'step_title': ParagraphStyle(
            'StepTitle', fontName='Helvetica-Bold', fontSize=15,
            leading=22, textColor=DARK_TEXT, alignment=TA_LEFT,
            spaceAfter=4
        ),
        'step_body': ParagraphStyle(
            'StepBody', fontName='Helvetica', fontSize=12,
            leading=18, textColor=MID_TEXT, alignment=TA_LEFT,
            spaceAfter=14
        ),
        'code_block': ParagraphStyle(
            'CodeBlock', fontName='Courier', fontSize=11,
            leading=18, textColor=DARK_TEXT, alignment=TA_LEFT,
            spaceAfter=4, leftIndent=20
        ),
        'cta_text': ParagraphStyle(
            'CTAText', fontName='Helvetica-Bold', fontSize=14,
            leading=22, textColor=TEAL, alignment=TA_CENTER,
            spaceAfter=6
        ),
        'big_quote': ParagraphStyle(
            'BigQuote', fontName='Helvetica', fontSize=14,
            leading=24, textColor=MID_TEXT, alignment=TA_CENTER,
            spaceAfter=12
        ),
        'footer': ParagraphStyle(
            'Footer', fontName='Helvetica', fontSize=9,
            leading=14, textColor=LIGHT_TEXT, alignment=TA_CENTER
        ),
    }


def add_question(story, styles, number, question, hint, content_width, num_lines=3):
    """Add a formatted question with hint and answer lines."""
    story.append(Spacer(1, 4))
    story.append(Paragraph(f"<b>{number}.</b> {question}", styles['question']))
    story.append(Paragraph(f"Hint: {hint}", styles['hint']))
    story.append(AnswerLines(content_width - 20, num_lines=num_lines))
    story.append(Spacer(1, 6))


def build_pdf():
    """Build the complete e-book PDF."""
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch
    )

    styles = get_styles()
    story = []
    content_width = letter[0] - 1.7 * inch  # usable width

    # ==================== COVER PAGE ====================
    story.append(Spacer(1, 100))
    story.append(AccentBar(80, 5, TEAL))
    story.append(Spacer(1, 30))
    story.append(Paragraph("Your Personal Prompt", styles['cover_title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "The Template That Makes Every AI Tool<br/>Know Exactly Who You Are",
        styles['cover_subtitle']
    ))
    story.append(Spacer(1, 50))
    # Decorative line
    story.append(HRFlowable(width="40%", thickness=1, color=LINE_COLOR, spaceAfter=50))
    story.append(Paragraph(
        "Stop explaining yourself. Start getting results.",
        styles['cover_tagline']
    ))
    story.append(Spacer(1, 60))
    story.append(Paragraph("getagents.today", styles['footer']))

    story.append(PageBreak())

    # ==================== PAGE 2: WHY YOU NEED THIS ====================
    story.append(Spacer(1, 20))
    story.append(AccentBar(60, 4, TEAL))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Why You Need This", styles['page_title']))
    story.append(Spacer(1, 20))

    story.append(Paragraph(
        "There is nothing more frustrating than opening a new chat, "
        "having to explain yourself for the 100th time, and getting "
        "generic AI garbage.",
        styles['body']
    ))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "The fix? <b>One master prompt about yourself.</b>",
        styles['body']
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph("How you think.", styles['body']))
    story.append(Paragraph("How you write.", styles['body']))
    story.append(Paragraph("What you'll never say.", styles['body']))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "<b>One prompt that saves you hours of work.</b> Every AI tool you use "
        "will know exactly who you are.",
        styles['body']
    ))
    story.append(Spacer(1, 16))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=16))
    story.append(Paragraph(
        "This template will guide you through building yours in <b>3 simple steps.</b>",
        styles['body']
    ))

    story.append(PageBreak())

    # ==================== PAGE 3: THE 3 STEPS ====================
    story.append(Spacer(1, 20))
    story.append(AccentBar(60, 4, TEAL))
    story.append(Spacer(1, 16))
    story.append(Paragraph("The 3 Steps", styles['page_title']))
    story.append(Spacer(1, 30))

    steps = [
        ("Step 1: Gather", "Ask your AI to tell you everything it has learned about you. "
         "Copy the conversation history, writing samples, or past interactions. "
         "The more data, the better your prompt will be."),
        ("Step 2: Organize", "Categorize everything into 4 sections using the framework "
         "on the following pages: Origin Story, Mindset, Tone & Voice, and Non-Negotiables."),
        ("Step 3: Evolve", "Treat this as a living document. As you evolve, your prompt "
         "needs to evolve too. Revisit it every few months and update what has changed.")
    ]

    for i, (title, body) in enumerate(steps):
        story.append(SectionNumber(i + 1))
        story.append(Spacer(1, 8))
        story.append(Paragraph(title, styles['step_title']))
        story.append(Paragraph(body, styles['step_body']))
        if i < 2:
            story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=20))

    story.append(PageBreak())

    # ==================== PAGE 4: SECTION 1 - ORIGIN STORY ====================
    story.append(Spacer(1, 10))
    story.append(AccentBar(60, 4, TEAL))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Section 1: Your Origin Story", styles['section_header']))
    story.append(Paragraph(
        "This is who you are and why you do what you do.",
        styles['section_sub']
    ))

    add_question(story, styles, 1,
        "In one sentence, what do you do?",
        "What's your expertise? For whom? What's the outcome?",
        content_width, num_lines=2)

    add_question(story, styles, 2,
        "What problem do you solve?",
        "What keeps your audience/clients up at 2am? What are they tired of?",
        content_width, num_lines=3)

    add_question(story, styles, 3,
        "Why you, and not someone else?",
        "2-3 things that make you unique. Not 'I care' - that's not real.",
        content_width, num_lines=3)

    add_question(story, styles, 4,
        "What's your background in 2-3 sentences?",
        "The key milestones that shaped who you are today.",
        content_width, num_lines=3)

    story.append(PageBreak())

    # ==================== PAGE 5: SECTION 2 - MINDSET ====================
    story.append(Spacer(1, 10))
    story.append(AccentBar(60, 4, TEAL))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Section 2: Your Mindset", styles['section_header']))
    story.append(Paragraph(
        "This is how you think, what you believe, and how you approach the world.",
        styles['section_sub']
    ))

    add_question(story, styles, 5,
        "What are your core beliefs about your field?",
        "The 2-3 things you'd argue about at dinner.",
        content_width, num_lines=2)

    add_question(story, styles, 6,
        "How do you approach problems?",
        "Are you data-driven? Intuitive? Hands-on? Strategic?",
        content_width, num_lines=2)

    add_question(story, styles, 7,
        "Who is the person you serve/help?",
        "Role, age range, industry, what stage they're at.",
        content_width, num_lines=2)

    add_question(story, styles, 8,
        "What does success look like for them?",
        "Their main goal. What would make them feel they made it?",
        content_width, num_lines=2)

    add_question(story, styles, 9,
        "What's blocking them right now?",
        "Their main obstacle or frustration that you help solve.",
        content_width, num_lines=2)

    story.append(PageBreak())

    # ==================== PAGE 6: SECTION 3 - TONE & VOICE ====================
    story.append(Spacer(1, 10))
    story.append(AccentBar(60, 4, TEAL))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Section 3: Your Tone & Voice", styles['section_header']))
    story.append(Paragraph(
        "This is how you sound. The words you choose and the ones you don't.",
        styles['section_sub']
    ))

    add_question(story, styles, 10,
        "If you were a character, how would someone describe you?",
        "e.g., 'A smart friend who explains complex things simply'",
        content_width, num_lines=2)

    add_question(story, styles, 11,
        "Give an example of a sentence that sounds like you.",
        "A real sentence you've written, or one you could write.",
        content_width, num_lines=3)

    add_question(story, styles, 12,
        "Who are 2-3 creators or voices you admire?",
        "People whose style resonates with yours.",
        content_width, num_lines=2)

    add_question(story, styles, 13,
        "What words or phrases do you use often?",
        "Your signature expressions, recurring themes.",
        content_width, num_lines=3)

    story.append(PageBreak())

    # ==================== PAGE 7: SECTION 4 - NON-NEGOTIABLES ====================
    story.append(Spacer(1, 10))
    story.append(AccentBar(60, 4, TEAL))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Section 4: Your Non-Negotiables", styles['section_header']))
    story.append(Paragraph(
        "This is what you'll never say, never do, and never compromise on.",
        styles['section_sub']
    ))

    add_question(story, styles, 14,
        "What is your brand/voice NOT?",
        "2-3 things you'll never be. e.g., 'Not corporate', 'Not preachy'",
        content_width, num_lines=2)

    add_question(story, styles, 15,
        "What words or phrases will you never use?",
        "Buzzwords, cliches, or tones that don't fit you.",
        content_width, num_lines=3)

    add_question(story, styles, 16,
        "What topics or approaches are off limits?",
        "Things that go against your values or positioning.",
        content_width, num_lines=2)

    add_question(story, styles, 17,
        "What must always be true in anything you create?",
        "Your quality standard. The line you won't cross.",
        content_width, num_lines=3)

    story.append(PageBreak())

    # ==================== PAGE 8: PUTTING IT ALL TOGETHER ====================
    story.append(Spacer(1, 10))
    story.append(AccentBar(60, 4, TEAL))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Now, Assemble Your Prompt", styles['page_title']))
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        "Take your answers and combine them into one document. "
        "Structure it like this:",
        styles['body']
    ))
    story.append(Spacer(1, 16))

    # Code/template block
    template_lines = [
        "=== MY PERSONAL PROMPT ===",
        "",
        "[ABOUT ME]",
        "(Paste your Origin Story answers here as flowing text)",
        "",
        "[MY MINDSET]",
        "(Paste your Mindset answers here as flowing text)",
        "",
        "[MY VOICE]",
        "(Paste your Tone & Voice answers here as flowing text)",
        "",
        "[NEVER DO THIS]",
        "(Paste your Non-Negotiables here as a list)",
        "",
        "=== END ===",
    ]

    # Build a table-based code block
    code_data = []
    for line in template_lines:
        if line == "":
            code_data.append([Paragraph("<br/>", styles['code_block'])])
        else:
            code_data.append([Paragraph(line, styles['code_block'])])

    code_table = Table(code_data, colWidths=[content_width - 40])
    code_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor("#F1F5F9")),
        ('LEFTPADDING', (0, 0), (-1, -1), 16),
        ('RIGHTPADDING', (0, 0), (-1, -1), 16),
        ('TOPPADDING', (0, 0), (0, 0), 12),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -2), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -2), 0),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))
    story.append(code_table)
    story.append(Spacer(1, 24))

    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=16))

    story.append(Paragraph(
        "<b>Copy this into any AI tool as your first message.</b><br/>"
        "Update it every few months as you grow.",
        styles['body']
    ))

    story.append(PageBreak())

    # ==================== PAGE 9: FINAL PAGE ====================
    story.append(Spacer(1, 80))
    story.append(AccentBar(80, 5, TEAL))
    story.append(Spacer(1, 30))
    story.append(Paragraph(
        "One Prompt. Every Tool.<br/>Always You.",
        styles['cover_title']
    ))
    story.append(Spacer(1, 24))

    story.append(Paragraph(
        "You just built the most powerful AI tool you'll ever have -<br/>"
        "a prompt that makes every AI know exactly who you are.",
        styles['big_quote']
    ))
    story.append(Spacer(1, 20))

    closing_lines = [
        "No more repeating yourself.",
        "No more generic outputs.",
        "No more wasted time.",
    ]
    for line in closing_lines:
        story.append(Paragraph(line, ParagraphStyle(
            'ClosingLine', fontName='Helvetica-Bold', fontSize=14,
            leading=26, textColor=DARK_TEXT, alignment=TA_CENTER
        )))
    story.append(Spacer(1, 16))

    story.append(Paragraph(
        "Update it as you evolve. Share it with your team. Use it everywhere.",
        ParagraphStyle(
            'ClosingSub', fontName='Helvetica', fontSize=12,
            leading=20, textColor=MID_TEXT, alignment=TA_CENTER
        )
    ))

    story.append(Spacer(1, 50))
    story.append(HRFlowable(width="50%", thickness=1, color=TEAL, spaceAfter=20))

    # CTA Box
    cta_data = [[
        Paragraph(
            "Want help building your AI system?<br/>"
            "<b>getagents.today</b>",
            styles['cta_text']
        )
    ]]
    cta_table = Table(cta_data, colWidths=[content_width * 0.7])
    cta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), VERY_LIGHT_TEAL),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 24),
        ('RIGHTPADDING', (0, 0), (-1, -1), 24),
        ('TOPPADDING', (0, 0), (-1, -1), 20),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 20),
        ('ROUNDEDCORNERS', [10, 10, 10, 10]),
        ('BOX', (0, 0), (-1, -1), 1.5, TEAL),
    ]))
    # Center the CTA table
    outer = Table([[cta_table]], colWidths=[content_width])
    outer.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(outer)

    # Build with page number footer
    def add_page_number(canvas_obj, doc_obj):
        page_num = canvas_obj.getPageNumber()
        if page_num > 1:  # Skip cover page
            canvas_obj.saveState()
            canvas_obj.setFont('Helvetica', 8)
            canvas_obj.setFillColor(LIGHT_TEXT)
            canvas_obj.drawCentredString(
                letter[0] / 2, 0.4 * inch,
                f"Your Personal Prompt  |  Page {page_num}"
            )
            canvas_obj.restoreState()

    doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=add_page_number)
    print(f"PDF created successfully: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
