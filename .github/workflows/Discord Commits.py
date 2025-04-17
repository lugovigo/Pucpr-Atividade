name: Discord Commits

on:
  push:
    branches:
      - main

jobs:
  discord:
    runs-on: windows-latest
    steps:
      - name: Send Discord Notification
        uses: Sniddl/discord-commits@v1.6
        with:
          webhook: ${{ secrets.DISCORD_WEBHOOK }}
          template: "avatar-with-link"
          include-extras: true
