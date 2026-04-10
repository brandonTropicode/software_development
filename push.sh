#!/bin/bash

# Check if commit message is provided
if [ -z "$1" ]; then
  echo "❌ Please provide a commit message."
  echo "Usage: ./push.sh \"your commit message\""
  exit 1
fi

# Store commit message
MESSAGE=$1

echo "Adding changes..."
git add .

echo "Committing with message: $MESSAGE"
git commit -m "$MESSAGE"

echo "Pushing to main..."
git push origin main

echo "✅ Done!"