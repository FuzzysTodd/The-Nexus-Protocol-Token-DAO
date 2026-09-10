/**
 * Vercel Speed Insights Initialization
 * 
 * This script initializes Vercel Speed Insights for the Nexus Protocol project.
 * It uses the injectSpeedInsights function to track Core Web Vitals and other
 * performance metrics.
 */

// Import the Speed Insights injection function
import { injectSpeedInsights } from './vercel-speed-insights/index.mjs';

// Initialize Speed Insights
injectSpeedInsights();
