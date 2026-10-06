---
name: Autonomous Fintech Precision
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#424655'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#737687'
  outline-variant: '#c2c6d8'
  surface-tint: '#0054d7'
  primary: '#0053d4'
  on-primary: '#ffffff'
  primary-container: '#1e6bff'
  on-primary-container: '#fffeff'
  inverse-primary: '#b3c5ff'
  secondary: '#525f75'
  on-secondary: '#ffffff'
  secondary-container: '#d6e3fe'
  on-secondary-container: '#58657b'
  tertiary: '#006589'
  on-tertiary: '#ffffff'
  tertiary-container: '#007fac'
  on-tertiary-container: '#ffffff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#001849'
  on-primary-fixed-variant: '#003fa5'
  secondary-fixed: '#d6e3fe'
  secondary-fixed-dim: '#bac7e1'
  on-secondary-fixed: '#0e1c2f'
  on-secondary-fixed-variant: '#3a475c'
  tertiary-fixed: '#c4e7ff'
  tertiary-fixed-dim: '#7bd0ff'
  on-tertiary-fixed: '#001e2c'
  on-tertiary-fixed-variant: '#004c69'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Geist
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.025em
  headline-xl-mobile:
    fontFamily: Geist
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.015em
  title-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  body-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.005em
  label-md:
    fontFamily: Geist
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Geist
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  numeric-data:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  margin: 2rem
  margin-sm: 1rem
  margin-lg: 3rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system embodies high-velocity decision-making, institutional security, and intelligent financial navigation. Designed for modern enterprise CFOs, risk officers, and underwriting engineers, the visual language balances the structural gravitas of traditional corporate finance with the dynamic precision of cutting-edge autonomous AI infrastructure.

The aesthetic fuses **Corporate / Modern SaaS** rigor with subtle **Technical Minimalism**. Every view delivers immediate telemetry, high legibility, and effortless data ingestion. Key visual drivers include:
- **Directional Clarity:** Crisp, forward-leaning vector cues inspired by aeronautic telemetry and precision flight instruments.
- **Systematic Trust:** Solid deep navy anchors paired with electric navigational beacons, avoiding chaotic neon while signaling real-time computation.
- **Architectural Calm:** Generous structured breathing room, strict alignment grids, and modular card compositions that reduce cognitive load during complex risk assessment.

## Colors

The palette establishes an immediate hierarchy between algorithmic activity and structural framework:
- **Primary (`#1E6BFF` - Electric Royal Blue):** The primary focal driver. Used for active navigation paths, primary CTAs, live transaction states, and verified algorithmic outcomes.
- **Secondary (`#0B192C` - Deep Enterprise Navy):** Grounding foundation. Serves as high-contrast display typography, inverted sidebar navigation, header anchors, and critical infrastructure states.
- **Tertiary (`#38BDF8` - Cyan Pilot Beam):** Data telemetry accents, active graph paths, trend indicators, and secondary vector highlights.
- **Neutral Core (`#0F172A` Slate Dark / `#64748B` Muted Slate):** Strict readability for body, metadata, and data tables.
- **Surface Foundations:** Crisp white (`#FFFFFF`) layered over cool ambient slate (`#F8FAFC` canvas and `#F1F5F9` nested containers), bordered by razor-thin slate dividers (`#E2E8F0`).

## Typography

Geist provides an ultra-clean, engineered grotesque aesthetic, balancing high micro-legibility in financial figures with sharp structural precision in hero metrics.
- **Tabular Figures:** Always apply `font-feature-settings: "tnum" 1` across all numerical columns, balance tallies, and KPI counters to prevent layout jitter during live calculations.
- **Hierarchy Rules:** High-tier headlines use negative letter tracking to preserve density and authority, while micro-labels and technical status indicators leverage expanded tracking and uppercase transforms.

## Layout & Spacing

The layout is structured around an adaptive 12-column grid anchored by a dedicated 260px collapsible command sidebar for platform navigation:
- **Desktop (1280px+):** 12-column fluid grid, 24px (`1.5rem`) gutters, and 32px to 48px (`2rem` - `3rem`) outer boundary margins. Modules group data into 3, 4, 6, or 12 column spans.
- **Tablet (768px - 1279px):** 8-column layout with 16px gutters and 24px margins. Navigation condenses to an icon-rail dock.
- **Mobile (Below 768px):** 4-column responsive stream with 12px gutters and 16px safe margins. Multi-metric tables transform into modular vertical credit cards.
- **Cadence:** Spacing between related metric values adheres strictly to the 4px/8px incremental scale (`space-xs` to `space-md`), keeping data proximity tight and informative.

## Elevation & Depth

Visual hierarchy leverages dual-layered precision outlines paired with low-opacity cool navy shadows:
- **Baseline Tier (Flat):** Cards sit at zero elevation with a 1px solid border (`#E2E8F0`) over a pure `#FFFFFF` background.
- **Level 1 (Card Hover / Data Tiles):** Ambient shadow: `0 1px 3px 0 rgba(11, 25, 44, 0.04), 0 4px 12px 0 rgba(11, 25, 44, 0.03)`. Border shifts smoothly to `#CBD5E1`.
- **Level 2 (Dropdowns, Command Menus, Flyouts):** `0 10px 25px -5px rgba(11, 25, 44, 0.08), 0 8px 10px -6px rgba(11, 25, 44, 0.04)` combined with subtle 1px border `#E2E8F0`.
- **Level 3 (Modal Dialogs & Decision Overlays):** Deep ambient isolation: `0 25px 50px -12px rgba(11, 25, 44, 0.20)` with high-clarity background blur (`backdrop-filter: blur(8px)` on `#0B192C` 40% backdrop).
- **Directional Glow:** On primary active agents or real-time pilot signals, an ambient focus aura is applied: `0 0 0 3px rgba(30, 107, 255, 0.15)`.

## Shapes

The interface balances soft ergonomics with structural exactness:
- **Metric Cards & Modules:** Locked strictly at `16px` (`rounded-lg` / `1rem`) corner radius, creating a unified modern frame for dense fintech tables and charts.
- **Interactive Controls (Inputs, Buttons, Dropdowns):** Configured at `8px` (`0.5rem`), ensuring crisp affordance and tactile certainty.
- **Status Tags, Badges & Chips:** Finished with fully circular caps (`9999px` pill contours) to distinguish temporal states from structural containers.
- **Pilot Motif:** Subtle 45-degree navigational angular notches and connected linear pathways are reserved for workflow progression nodes and intelligence pipeline diagrams.

## Components

### Buttons
- **Primary:** Background `#1E6BFF`, color `#FFFFFF`, font-weight 600, height 40px, padding `0 16px`, border-radius 8px. Hover shifts to `#1753C7` with a subtle elevation aura. Focus-visible applies a 2px offset ring in `#1E6BFF`.
- **Secondary (Navy Outline):** Background `#FFFFFF`, border `1px solid #E2E8F0`, color `#0B192C`. Hover initiates background `#F8FAFC` and border `#CBD5E1`.
- **Destructive/Risk:** Background `#FFF1F2`, text `#E11D48`, border `1px solid #FECDD3`. Hover deepens to `#FFE4E6`.

### Cards & Dashboards
- **Structure:** Pure white `#FFFFFF` surface, 16px corner radius, 1px solid border `#E2E8F0`, padding 24px (`space-lg`).
- **Header:** Metric label in `label-sm` uppercase muted slate (`#64748B`), paired with an action icon or dynamic trend indicator in the top right.
- **AI Pilot State:** Sub-cards generated by automated risk analysis feature an inner linear accent border on the left edge (`3px solid #1E6BFF`).

### Input Fields & Controls
- **Inputs:** Height 40px, background `#FFFFFF`, border `1px solid #CBD5E1`, border-radius 8px, padding `0 12px`, typography `body-md`. Focus transitions border to `#1E6BFF` and adds `box-shadow: 0 0 0 3px rgba(30, 107, 255, 0.12)`.
- **Checkboxes & Radios:** 18px size, 4px radius for checkboxes, full circle for radios. Active state fills with `#1E6BFF` featuring an internal white pilot tick icon.

### Chips & Badges
- **Status Chips:** Height 24px, padding `2px 8px`, border-radius 9999px, typography `label-sm`.
  - *Active / Clear:* Background `#ECFDF5`, text `#059669`, border `1px solid #A7F3D0`.
  - *Under Review / Processing:* Background `#EFF6FF`, text `#1E6BFF`, border `1px solid #BFDBFE`.
  - *High Risk / Alert:* Background `#FFF1F2`, text `#E11D48`, border `1px solid #FECDD3`.

### Data Tables & Lists
- **Structure:** Zero-margin alternating clean rows. Header rows use `#F8FAFC` with uppercase `label-sm` in `#64748B`.
- **Cell Content:** 52px row height, vertically centered, bordered with horizontal 1px lines (`#F1F5F9`). Numerical values aligned right with tabular figures enabled. Hover highlights row in `#F8FAFC`.