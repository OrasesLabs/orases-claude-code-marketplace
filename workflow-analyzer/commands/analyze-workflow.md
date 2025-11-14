---
name: analyze-workflow
description: Analyzes a recent Claude Code development session from logs to identify improvements, inefficiencies, and optimization opportunities
tools: Read, Glob, Grep, Bash, Task
argument-hint: "[date] [additional-instructions] - Optional date (YYYYMMDD) and/or custom analysis instructions"
color: cyan
---

# Workflow Session Analyzer

Analyze Claude Code development sessions from `.claude/logs/` to identify workflow improvements, inefficiencies, and optimization opportunities.

## Task

Parse session transcripts from a specific date directory, analyze multi-agent workflows, evaluate development patterns, and generate a comprehensive report with actionable recommendations.

## Execution Flow

**Arguments Provided:** `$ARGUMENTS`

### Step 1: Determine Target Session

**Parse Arguments:**

First, parse `$ARGUMENTS` to handle 4 scenarios:

1. **No arguments (`$ARGUMENTS` is empty):**
   - Proceed to list available sessions (see below)

2. **First token matches YYYYMMDD pattern (8 digits):**
   - Extract date as first token
   - Everything after first token (if present) = additional instructions
   - Store additional instructions for use in Step 3
   - Proceed with date validation (see below)

3. **First token does NOT match YYYYMMDD pattern:**
   - Entire `$ARGUMENTS` = additional instructions
   - Store instructions for user reference
   - Proceed to list available sessions
   - When showing session list, add note before example:
     ```
     You provided instructions: "{instructions}"
     Please re-run with date to apply them.
     Example: /analyze-workflow 20251007 {your-instructions}
     ```

4. **Parsing errors:**
   - Handle edge cases gracefully with clear error messages

**If date argument is provided (YYYYMMDD format):**
1. Validate the date format matches YYYYMMDD pattern
2. Construct the log directory path: `.claude/logs/{YYYYMMDD}/`
3. Verify the directory exists using Bash (`ls` or `test -d`)
4. If directory doesn't exist:
   - Inform user clearly: "No logs found for date {YYYYMMDD}"
   - Suggest running the command without arguments to see available dates
   - Exit gracefully
5. If directory exists: Proceed to Step 2 with this directory

**If NO date argument is provided (but additional instructions may be present):**
1. Use Bash to scan `.claude/logs/` directory and list all subdirectories
2. Filter for directories matching YYYYMMDD format (8 digits)
3. Sort directories chronologically (most recent first)
4. If no log directories found:
   - Inform user: "No Claude Code session logs found in `.claude/logs/`"
   - Suggest they may need to enable logging or check the correct project directory
   - Exit gracefully
5. If log directories found:
   - If additional instructions were provided, show them first:
     ```
     You provided instructions: "{instructions}"
     ```
   - Present available sessions as a numbered list with dates formatted for readability (e.g., "2025-10-07" instead of "20251007")
   - Example output (with instructions):
     ```
     You provided instructions: "focus on why we found so many errors"

     Available Claude Code session logs:

     1. October 11, 2025 (20251011)
     2. October 7, 2025 (20251007)

     Please select a session to analyze by providing the date in YYYYMMDD format.
     Example: /analyze-workflow 20251011 focus on why we found so many errors
     ```
   - Example output (without instructions):
     ```
     Available Claude Code session logs:

     1. October 11, 2025 (20251011)
     2. October 7, 2025 (20251007)

     Please select a session to analyze by providing the date in YYYYMMDD format.
     Example: /analyze-workflow 20251011
     ```
   - Wait for user to re-invoke the command with their chosen date
   - Exit gracefully

### Step 2: Prepare for Analysis

1. Confirm the target log directory path
2. Use Glob or Bash to preview the contents:
   - Count total log files
   - Identify file types (e.g., `*.log`, `*.md`, session transcripts)
   - Look for patterns suggesting multiple sessions within the same date
3. **Gather file size information** using `ls -lh` or `du -h`:
   - Get sizes of main session transcript(s)
   - Count and size subagent transcripts
   - This information helps workflow-analyzer decide optimization strategies
4. Inform the user:
   - If NO additional instructions provided:
     ```
     Analyzing session logs from: .claude/logs/{YYYYMMDD}/
     Found {count} log files to analyze.
     Main transcript: {size}
     Subagent transcripts: {count} files
     ```
   - If additional instructions provided:
     ```
     Analyzing session logs from: .claude/logs/{YYYYMMDD}/
     Found {count} log files to analyze.
     Main transcript: {size}
     Subagent transcripts: {count} files
     Custom focus: "{instructions}"
     ```

### Step 3: Delegate to Workflow Analyzer

Invoke the `workflow-analyzer` subagent using the Task tool with high-level instructions that allow the agent to use its expertise.

**Task Prompt Structure:**

```
Analyze Claude Code session from {date} ({YYYYMMDD})

**Session Information:**
- Date: {formatted date}
- Log Directory: .claude/logs/{YYYYMMDD}/
- Main Transcript(s): {filename(s)} ({size(s)})
- Subagent Transcripts: {count} files ({size range if applicable})
- Total Log Files: {count}

{If additional instructions provided:}
**User-Provided Focus Areas:**
{instructions}

**Your Task:**
Analyze this Claude Code development session following your standard workflow analysis process. Use your expertise to determine the most effective analysis approach based on transcript sizes and complexity. Provide a comprehensive report with actionable recommendations for workflow improvements.

**Important Context:**
- Multiple sessions may exist within the date directory - identify session boundaries
- Correlate subagent transcripts with main session using timestamps, session IDs, task context, and file naming patterns
- If correlation is ambiguous or sessions overlap, note this in your analysis
- Consider edge cases: corrupted files, permission issues, incomplete logs

**Deliverable:**
Present your analysis report directly in the conversation using your standard format with clear markdown, prioritized recommendations, and specific log references.
```

**Key Principles:**
- Provide file size information so the agent can decide whether to use the transcript condenser tool
- Trust the agent's built-in process (including Step 0: Assess Transcript Size)
- Give high-level guidance, not step-by-step prescriptive instructions
- Let the agent determine optimal analysis strategies based on data characteristics
- Preserve essential context about multiple sessions, correlation strategies, and edge cases

### Step 4: Follow-Up Options

After the workflow-analyzer completes its report, offer the user:

1. **Save Report:** "Would you like to save this analysis to a file? I can write it to `docs/workflow-analysis-{date}.md`"
2. **Deep Dive:** "Would you like me to investigate any specific finding in more detail?"
3. **Compare Sessions:** "Would you like to compare this session with another date?"
4. **Analyze with Different Focus:** "Would you like to re-analyze this session with different focus areas?"

**Example commands with instructions:**
- `/analyze-workflow 20251011 Are we committing our work appropriately`
- `/analyze-workflow 20251011 focus on subagent handoffs`
- `/analyze-workflow focus on why we found so many errors` (lists sessions, then re-run with date)

## Edge Cases

**Invalid date format provided:**
- Detect non-YYYYMMDD formats (e.g., "2025-10-07", "Oct 7", "yesterday")
- Inform user of correct format: "Please provide date in YYYYMMDD format (e.g., 20251007)"
- Optionally suggest running without arguments to see available dates

**Missing log directory:**
- Check if `.claude/logs/` directory itself exists
- If not: "The `.claude/logs/` directory does not exist. Logging may not be enabled for this project."
- If yes but empty: "No session logs found. Check if logging is enabled and sessions have been recorded."

**Ambiguous session boundaries:**
- If the workflow-analyzer cannot clearly distinguish between multiple sessions, note this
- Analyze as a single continuous session and flag the ambiguity in the report

**Corrupted or incomplete log files:**
- Handle gracefully with informative error messages
- Analyze what is readable and note gaps or issues in the report

**Permission issues:**
- If log files cannot be read due to permissions, inform the user clearly
- Suggest checking file permissions on the log directory

## Best Practices

- **Always use relative paths from project root:** `.claude/logs/...`
- **Be informative:** Clearly communicate what's happening at each step
- **Handle errors gracefully:** Provide actionable guidance when things go wrong
- **Respect user choice:** When listing available dates, wait for explicit selection
- **Be thorough:** Ensure the workflow-analyzer receives complete, clear instructions
- **Prioritize findings:** Focus on high-impact improvements in recommendations

---

**Ready to analyze!** I'll determine which session to analyze based on your input, then delegate to the workflow-analyzer for comprehensive analysis.
