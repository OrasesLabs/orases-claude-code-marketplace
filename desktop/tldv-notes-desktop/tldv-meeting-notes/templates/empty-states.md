# Empty State Messages

Fallback content when meeting data is unavailable.

## No Summary Available

```markdown
_No summary available — transcript may be processing_
```

## No Action Items

```markdown
- _No action items identified_
```

## No Transcript

```markdown
_Transcript not yet available for this meeting_
```

## No Meetings Found

```markdown
No meetings found for the specified period.
```

## No Highlights Available

When highlights are missing but a transcript exists, generate a summary directly from the transcript instead of showing an empty state.

## Note Generation Guidelines

### Summary Section
- Extract top 3-5 highlights as bullet points
- Focus on decisions, outcomes, and key discussions
- Keep each point concise (1-2 sentences)

### Discussion Notes
- Group by topic from TLDV's topic detection
- Include relevant quotes from transcript
- Preserve speaker attribution for important statements

### Action Items Extraction
Look for:
- Explicit mentions of "action item", "to do", "follow up"
- Assignments: "[Person] will [task]"
- Deadlines mentioned
- Commitments made
