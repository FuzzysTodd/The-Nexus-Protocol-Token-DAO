#!/usr/bin/env bash

# Usage:
#   ./bootstrap-nexus-project.sh <org_or_user> <project_name>
#
# Example:
#   ./bootstrap-nexus-project.sh FuzzysTodd "Nexus DAO Roadmap"

OWNER=$1
PROJECT_NAME=$2

if [ -z "$OWNER" ] || [ -z "$PROJECT_NAME" ]; then
  echo "Usage: ./bootstrap-nexus-project.sh <org_or_user> <project_name>"
  exit 1
fi

echo "🚀 Creating GitHub Project: $PROJECT_NAME"

# Create the project
PROJECT_ID=$(gh api graphql -f query="
  mutation {
    createProjectV2(input: {ownerId: \"$(gh api users/$OWNER --jq '.id')\", title: \"$PROJECT_NAME\"}) {
      projectV2 { id }
    }
  }
" --jq '.data.createProjectV2.projectV2.id')

echo "✅ Project created"
echo "Project ID: $PROJECT_ID"
echo

echo "🛠 Creating core fields..."

# Create Status field
STATUS_FIELD_ID=$(gh api graphql -f query="
  mutation {
    createProjectV2Field(input: {
      projectId: \"$PROJECT_ID\",
      dataType: SINGLE_SELECT,
      name: \"Status\"
    }) {
      projectV2Field { id }
    }
  }
" --jq '.data.createProjectV2Field.projectV2Field.id')

echo "Status Field ID: $STATUS_FIELD_ID"
echo

# Helper function to create status options
create_option () {
  local NAME=$1
  gh api graphql -f query="
    mutation {
      createProjectV2SingleSelectFieldOption(input: {
        fieldId: \"$STATUS_FIELD_ID\",
        name: \"$NAME\"
      }) {
        projectV2SingleSelectFieldOption { id }
      }
    }
  " --jq '.data.createProjectV2SingleSelectFieldOption.projectV2SingleSelectFieldOption.id'
}

echo "🧩 Creating Status options..."

BACKLOG_ID=$(create_option "Backlog")
INPROGRESS_ID=$(create_option "In Progress")
REVIEW_ID=$(create_option "Review")
READY_ID=$(create_option "Ready to Merge")
DONE_ID=$(create_option "Done")

echo "Backlog: $BACKLOG_ID"
echo "In Progress: $INPROGRESS_ID"
echo "Review: $REVIEW_ID"
echo "Ready to Merge: $READY_ID"
echo "Done: $DONE_ID"
echo

echo "🛠 Creating additional fields..."

# Priority field
PRIORITY_FIELD_ID=$(gh api graphql -f query="
  mutation {
    createProjectV2Field(input: {
      projectId: \"$PROJECT_ID\",
      dataType: SINGLE_SELECT,
      name: \"Priority\"
    }) {
      projectV2Field { id }
    }
  }
" --jq '.data.createProjectV2Field.projectV2Field.id')

echo "Priority Field ID: $PRIORITY_FIELD_ID"

# Priority options
LOW_ID=$(gh api graphql -f query="
  mutation {
    createProjectV2SingleSelectFieldOption(input: {
      fieldId: \"$PRIORITY_FIELD_ID\",
      name: \"Low\"
    }) {
      projectV2SingleSelectFieldOption { id }
    }
  }
" --jq '.data.createProjectV2SingleSelectFieldOption.projectV2SingleSelectFieldOption.id')

MEDIUM_ID=$(gh api graphql -f query="
  mutation {
    createProjectV2SingleSelectFieldOption(input: {
      fieldId: \"$PRIORITY_FIELD_ID\",
      name: \"Medium\"
    }) {
      projectV2SingleSelectFieldOption { id }
    }
  }
" --jq '.data.createProjectV2SingleSelectFieldOption.projectV2SingleSelectFieldOption.id')

HIGH_ID=$(gh api graphql -f query="
  mutation {
    createProjectV2SingleSelectFieldOption(input: {
      fieldId: \"$PRIORITY_FIELD_ID\",
      name: \"High\"
    }) {
      projectV2SingleSelectFieldOption { id }
    }
  }
" --jq '.data.createProjectV2SingleSelectFieldOption.projectV2SingleSelectFieldOption.id')

echo "Priority Options:"
echo "Low: $LOW_ID"
echo "Medium: $MEDIUM_ID"
echo "High: $HIGH_ID"
echo

# Subsystem field
SUBSYSTEM_FIELD_ID=$(gh api graphql -f query="
  mutation {
    createProjectV2Field(input: {
      projectId: \"$PROJECT_ID\",
      dataType: SINGLE_SELECT,
      name: \"Subsystem\"
    }) {
      projectV2Field { id }
    }
  }
" --jq '.data.createProjectV2Field.projectV2Field.id')

echo "Subsystem Field ID: $SUBSYSTEM_FIELD_ID"

# Subsystem options
for subsystem in "Contracts" "Dashboards" "Governance" "Signal Bus" "AI/MCP" "Infrastructure"; do
  OPTION_ID=$(gh api graphql -f query="
    mutation {
      createProjectV2SingleSelectFieldOption(input: {
        fieldId: \"$SUBSYSTEM_FIELD_ID\",
        name: \"$subsystem\"
      }) {
        projectV2SingleSelectFieldOption { id }
      }
    }
  " --jq '.data.createProjectV2SingleSelectFieldOption.projectV2SingleSelectFieldOption.id')

  echo "$subsystem: $OPTION_ID"
done

echo
echo "🎉 Nexus DAO Project Bootstrap Complete!"
echo "Copy these IDs into your automation workflows:"
echo
echo "PROJECT_ID: $PROJECT_ID"
echo "STATUS_FIELD_ID: $STATUS_FIELD_ID"
echo "BACKLOG_ID: $BACKLOG_ID"
echo "INPROGRESS_ID: $INPROGRESS_ID"
echo "REVIEW_ID: $REVIEW_ID"
echo "READY_ID: $READY_ID"
echo "DONE_ID: $DONE_ID"
echo
echo "PRIORITY_FIELD_ID: $PRIORITY_FIELD_ID"
echo "LOW_ID: $LOW_ID"
echo "MEDIUM_ID: $MEDIUM_ID"
echo "HIGH_ID: $HIGH_ID"
echo
echo "SUBSYSTEM_FIELD_ID: $SUBSYSTEM_FIELD_ID"
echo "Subsystem options created above"
