# File Categorization Patterns

Default patterns for categorizing modified files in the technical summary. These patterns
match the standard CakePHP 5 project structure.

Override these by setting `file_categories` in the settings file.

## Default Categories

| Category | Pattern |
|---|---|
| Controllers | `*/src/Controller/**/*.php` |
| Models/Tables | `*/src/Model/**/*.php` |
| Templates | `*/templates/**/*.php` |
| Migrations | `config/Migrations/**/*.php` |
| Seeds | `config/Seeds/**/*.php`, `config/DevSeeds/**/*.php` |
| Tests | `*/tests/**/*.php` |
| Frontend JS | `resources/js/**/*.js` |
| Frontend CSS | `resources/css/**/*.scss` |
| Config | `config/**/*.php` (non-migration) |

## Custom Categories Example (Laravel)

```yaml
file_categories:
  Controllers: "app/Http/Controllers/**/*.php"
  Models: "app/Models/**/*.php"
  Views: "resources/views/**/*.blade.php"
  Migrations: "database/migrations/**/*.php"
  Tests: "tests/**/*.php"
  Frontend JS: "resources/js/**/*.js"
  Frontend CSS: "resources/css/**/*.css"
  Config: "config/**/*.php"
```

## Usage

Files not matching any category pattern are grouped under "Other".
Each category in the technical summary includes file count and line change totals.
