# Technical Summary Template

Markdown structure for the technical summary section. This targets developers and maintainers.
Adapt section content based on actual changes - omit sections that do not apply.

```markdown
### Technical Summary

#### Architecture & Implementation
- Pattern changes or new abstractions introduced
- Integration with existing systems
- Database schema changes (if migrations present)

#### Modified Files

**Controllers** ({count} files, +{additions} -{deletions}):
- {plugin}/src/Controller/{ControllerName}.php

**Models** ({count} files, +{additions} -{deletions}):
- {plugin}/src/Model/Table/{TableName}.php
- {plugin}/src/Model/Entity/{EntityName}.php

**Templates** ({count} files, +{additions} -{deletions}):
- {plugin}/templates/{controller}/{action}.php

**Migrations** ({count} files):
- config/Migrations/{timestamp}_{MigrationName}.php

**Tests** ({count} files, +{additions} -{deletions}):
- {plugin}/tests/TestCase/Controller/{ControllerName}Test.php

**Frontend** ({count} files, +{additions} -{deletions}):
- resources/js/{path}
- resources/css/{path}

#### Commits
- {short_hash}: {Commit message}
- {short_hash}: {Commit message}

#### Testing Coverage
- Unit test additions or modifications
- Integration test scenarios covered
- Edge cases addressed

#### Code Quality
- PSR-12 compliance verified
- Security: h() escaping and __() localization applied
- CakePHP 5 patterns validated
- No deprecated API usage

#### Performance Considerations
- {Only include if query, caching, or load changes apply}
```
