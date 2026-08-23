# Vercel Web Analytics Setup

This document describes the Vercel Web Analytics integration for The Nexus Protocol Token DAO project.

## Overview

Vercel Web Analytics has been successfully installed and configured for this project. The integration uses the `@vercel/analytics` package (v1.6.1) and follows the vanilla JavaScript approach suitable for this HTML/JS-based project.

## Installation

The analytics package has been installed via npm:

```bash
npm install @vercel/analytics
```

## Implementation

### Core Integration File

**File**: `main/widthdraws.js`

This file contains the analytics initialization code that:
1. Initializes the Vercel Analytics queue (`window.va`)
2. Detects the environment (development vs production)
3. Injects the Vercel Analytics script in production mode
4. Provides a global `NexusAnalytics` object for custom event tracking

### Integrated Pages

The analytics script has been added to the following key pages:

- ✅ `index.html` - Main contract withdrawal manager
- ✅ `withdraw.html` - Withdrawal operations page
- ✅ `governance.html` - DAO governance interface
- ✅ `web3-interface.html` - Web3 integration dashboard

### How It Works

#### 1. Automatic Page View Tracking

Once deployed to Vercel, all page views are automatically tracked. The script:
- Only runs in production (not on localhost)
- Loads the analytics script from `/_vercel/insights/script.js`
- Respects user privacy and Vercel's analytics policies

#### 2. Environment Detection

The script automatically detects the environment:
- **Development** (localhost, 127.0.0.1): Analytics disabled, no data sent
- **Production** (Vercel deployment): Analytics active, tracking enabled

#### 3. Custom Event Tracking

You can track custom events using the global `NexusAnalytics` object:

```javascript
// Track a custom event
NexusAnalytics.track('event_name', {
  property1: 'value1',
  property2: 'value2'
});
```

Example:
```javascript
// Track a withdrawal action
NexusAnalytics.track('withdrawal_initiated', {
  contract: contractAddress,
  amount: ethAmount,
  method: withdrawMethod
});
```

## Deployment Steps

To activate analytics on Vercel:

1. **Enable Web Analytics in Vercel Dashboard**
   - Go to your project in the Vercel dashboard
   - Navigate to the Analytics tab
   - Click "Enable Web Analytics"

2. **Deploy Your Project**
   ```bash
   vercel deploy
   ```

3. **Verify Tracking**
   - Visit your deployed site
   - Check the Network tab in browser DevTools
   - Look for requests to `/_vercel/insights/script.js` and `/_vercel/insights/view`
   - View analytics data in the Vercel dashboard

## Testing

A test page has been created to verify the integration:

**File**: `test-analytics.html`

Open this file in a browser to:
- Check if analytics initialized correctly
- View the current mode (development/production)
- Test custom event tracking

## File Structure

```
.
├── package.json                 # Added @vercel/analytics dependency
├── package-lock.json            # NPM lockfile
├── main/
│   └── widthdraws.js           # Analytics initialization script
├── index.html                   # Updated with analytics script
├── withdraw.html                # Updated with analytics script
├── governance.html              # Updated with analytics script
├── web3-interface.html          # Updated with analytics script
├── test-analytics.html          # Test/verification page
└── ANALYTICS_SETUP.md          # This documentation
```

## Important Notes

### Privacy-Friendly

Vercel Web Analytics is:
- GDPR-compliant
- Privacy-friendly
- Does not use cookies
- Does not track personal information
- Aggregates data without individual user tracking

### Development Mode

When running locally (localhost), the analytics script:
- Initializes the queue
- Does NOT send any data to Vercel
- Logs status to console for debugging

### Production Mode

When deployed to Vercel:
- Automatically detects production environment
- Sends anonymous analytics data
- Tracks page views and custom events
- Data visible in Vercel dashboard

## Troubleshooting

### Analytics Not Showing Data

1. Ensure Web Analytics is enabled in your Vercel project dashboard
2. Verify the project is deployed to Vercel (not just localhost)
3. Check browser DevTools Network tab for `/_vercel/insights/` requests
4. Wait a few minutes for data to appear in the dashboard

### Script Errors

Check the browser console for error messages:
- `[Nexus Analytics] Vercel Web Analytics initialized` = Success
- `[Nexus Analytics] Running in development mode` = Expected on localhost
- Script load errors may indicate network issues

## Resources

- [Vercel Web Analytics Documentation](https://vercel.com/docs/analytics)
- [Vercel Analytics Quickstart](https://vercel.com/docs/analytics/quickstart)
- [@vercel/analytics Package](https://www.npmjs.com/package/@vercel/analytics)

## Support

For issues or questions:
1. Check the Vercel Analytics documentation
2. Review the browser console for error messages
3. Verify the integration in `main/widthdraws.js`
4. Test using `test-analytics.html`
