#!/usr/bin/env bash

# Usage:
#   ./get-project-columns.sh <org_or_user> <project_number>
#
# Example:
#   ./get-project-columns.sh FuzzysTodd 1

OWNER=$1
PROJECT_NUMBER=$2

if [ -z "$OWNER" ] || [ -z "$PROJECT_NUMBER" ]; then
  echo "Usage: ./get-project-columns.sh <org_or_user> <project_number>"
  exit 1
fi

echo "Fetching Project ID..."
PROJECT_ID=$(gh api graphql -f query="
  query {
    user(login: \"$OWNER\") {
      projectV2(number: $PROJECT_NUMBER) {
        id
      }
    }
  }
" --jq '.data.user.projectV2.id')

if [ -z "$PROJECT_ID" ]; then
  echo "Trying as organization..."
  PROJECT_ID=$(gh api graphql -f query="
    query {
      organization(login: \"$OWNER\") {
        projectV2(number: $PROJECT_NUMBER) {
          id
        }
      }
    }
  " --jq '.data.organization.projectV2.id')
fi

if [ -z "$PROJECT_ID" ]; then
  echo "❌ Could not find project. Check owner and project number."
  exit 1
fi

echo "✅ Project ID: $PROJECT_ID"
echo
echo "Fetching fields (columns)..."
echo

FIELDS=$(gh api graphql -f query="
  query {
    node(id: \"$PROJECT_ID\") {
      ... on ProjectV2 {
        fields(first: 50) {
          nodes {
            id
            name
            dataType
            ... on ProjectV2SingleSelectField {
              options {
                id
                name
              }
            }
          }
        }
      }
    }
  }
")

echo "$FIELDS" | jq -r '
  .data.node.fields.nodes[] |
  "Field: \(.name)\n  Field ID: \(.id)\n  Type: \(.dataType)\n" +
  (if .options then
     (.options[] | "    Option: \(.name)\n      Option ID: \(.id)\n")
   else "" end)
'
