name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build with Buildozer
        uses: Android-for-Python/android-buildozer-action@v1.2.2
        with:
          buildozer_version: stable
          
