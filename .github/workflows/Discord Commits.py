name: Discord
on:
  - push


jobs:
  discord:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Send Discord Notification
        uses: Sniddl/discord-commits@v1.6
        with:
          webhook: ${{ secrets.DISCORD_WEBHOOK }}
          template: "avatar-with-link"
          include-extras: true
