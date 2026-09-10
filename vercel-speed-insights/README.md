# Vercel Speed Insights Distribution Files

This directory contains the distribution files from the `@vercel/speed-insights` npm package (v2.0.0).

## Purpose

These files are required for Speed Insights to function in the browser. Since this is a vanilla HTML/JavaScript project without a build process, the distribution files are included directly in the repository.

## Source

These files are copied from `node_modules/@vercel/speed-insights/dist/` after installing the package via npm.

## Contents

- `index.mjs` - Main ES module entry point (used by the project)
- Framework-specific adapters (next, react, vue, remix, sveltekit, nuxt, astro)
- TypeScript declaration files (`.d.ts`, `.d.mts`)
- Source maps for debugging (`.js.map`, `.mjs.map`)

## Updates

To update Speed Insights:
1. Update the package version in `playwright-tool/package.json`
2. Run `npm install` in the `playwright-tool/` directory
3. Copy the updated dist files: `cp -r playwright-tool/node_modules/@vercel/speed-insights/dist/* vercel-speed-insights/`

## Usage

The project uses the main module via ES6 import in `speed-insights-init.js`:
```javascript
import { injectSpeedInsights } from './vercel-speed-insights/index.mjs';
injectSpeedInsights();
```
