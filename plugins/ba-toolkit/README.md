# Visual Workflow Diagram Generator

A Claude Code skill that transforms written workflow steps into interactive, browser-based visual process flow diagrams with clickable elements.

## Overview

This skill converts textual workflow descriptions, Standard Operating Procedures (SOPs), or business processes into professional, interactive flowchart diagrams. The generated diagrams are self-contained HTML files that can be opened in any modern web browser.

## Features

- **Interactive Diagrams**: Click any element to see detailed information in a flyout panel
- **Standard Flowchart Shapes**: Uses industry-standard shapes (rectangles for processes, diamonds for decisions, etc.)
- **Self-Contained Output**: Single HTML file with embedded CSS, JavaScript, and inline SVG
- **Responsive Design**: Works on desktop and mobile devices
- **Accessible**: WCAG AA compliant color contrast and keyboard navigation (Escape key to close panels)
- **Customizable**: Supports branding, orientation (vertical/horizontal), and step badges

## How It Works

The skill uses a hybrid implementation approach:
- **HTML**: Document structure, containers, and flyout panel
- **CSS**: Styling for layout, colors, hover effects, and responsive design
- **SVG**: Flowchart diagram with shapes, connectors, arrows, and text (embedded inline)
- **JavaScript**: Interactivity for clicking elements and showing/hiding detailed information

## Usage

Invoke this skill when you need to:
- Convert written SOPs into visual diagrams
- Document business processes for training or compliance
- Create interactive process maps from meeting notes
- Visualize decision trees and approval workflows
- Transform step-by-step instructions into flowcharts

### Trigger Phrases

The skill activates when you ask Claude to:
- "create a workflow diagram"
- "visualize a workflow"
- "generate a process flow"
- "make a flowchart"
- "diagram these steps"

### Example Request

```
Create a workflow diagram for the following order fulfillment process:
1. Customer submits order through website
2. System validates payment information
3. If payment is approved, proceed to fulfillment
4. If payment is declined, send error notification
5. Warehouse picks and packs items
6. Shipping carrier delivers order
7. Customer receives order confirmation
```

## User Preferences

The skill will ask you for the following preferences before generating the diagram:

1. **Branding**: Optional URL to brand the diagram
2. **Orientation**: Vertical or horizontal layout
3. **Badges**: Numeric or alphanumeric step identifiers
4. **Format**: HTML/CSS with inline SVG (default), Mermaid, or Pure HTML/CSS

## Output

The skill generates a complete HTML file that you can:
- Save to your local machine
- Open in any web browser
- Share with team members
- Embed in documentation
- Print or export to PDF

## Standards & Best Practices

### Flowchart Conventions
- **Process/Task**: Rectangle
- **Decision**: Diamond
- **Data/Input/Output**: Parallelogram
- **Start/End**: Rounded Rectangle
- **Flow Direction**: Arrows with clear direction

### Design Principles
- Concise labels (2-5 words) with detailed information in flyout panels
- High color contrast for accessibility
- Proper spacing to prevent overlapping
- Clean routing of connector lines
- Center-aligned text with equal padding

## Technical Details

- No external dependencies (except optional CDN for Mermaid format)
- All assets embedded in a single HTML file
- Touch-friendly click targets (minimum 44x44px)
- Keyboard accessible (Escape key dismissal)
- Fully responsive across viewport sizes

## Version

Current version: 0.1.0

## Support

For issues, questions, or feature requests, please refer to the main Claude Code documentation or skills repository.
