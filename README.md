# Specjal Map

This is just a simple, static project based on Leaflet to showcase photos me
and my pals are taking around the world, drinking [Specjal
beer](https://www.specjal.pl). See it in action at
[https://dulek.github.io/specjal-map/](https://dulek.github.io/specjal-map/).

## How it works

The code is in index.html, markers data goes into markers.js, in a pretty
self-explanatory format.

### Marker Fields

Each marker in `markers.js` can contain the following fields:

- **latitude** (required): Decimal latitude coordinate (e.g., `52.516360`)
- **longitude** (required): Decimal longitude coordinate (e.g., `13.378772`)
- **photo** (required): Path to the photo file (e.g., `"photos/berlin.jpg"`)
- **author** (required): Name of the person who took the photo (e.g., `"Dulek"`)
- **title** (required): English title/location description (e.g., `"Brandenburger Tor - Berlin - Germany"`)
- **titlePL** (optional): Polish title/location description (e.g., `"Brama Brandenburska - Berlin - Niemcy"`)
- **type** (required): Type of Specjal - either `"can"` or `"bottle"`
- **comment** (optional): English comment/description about the location or photo
- **commentPL** (optional): Polish comment/description about the location or photo
- **datetime** (optional): ISO 8601 timestamp when the photo was taken (e.g., `"2023-01-13T14:15:00.511Z"`)

## Marker Preparation Tool

We've created a tool that allows you to easily prepare JSON files for creating markers on the map. To use the tool, follow the steps provided in the [Map Marker Preparation Tool README](./json-tool/README.md). This tool works best when your photos contain EXIF data with GPS information.

- [Tool for Preparing Map Markers](https://dulek.github.io/specjal-map/json-tool)
