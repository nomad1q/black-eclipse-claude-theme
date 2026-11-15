import type { Register, ThemeSetArgs } from 'claude-code'

import { makeColors } from './make-colors.js'
import { SCENE } from './scene'

// Black Eclipse: a dark-fantasy look. Iron and ash by night, old parchment by day,
// blood-crimson accents. Original art only.
const PALETTE: Parameters<typeof makeColors>[0] = {
  label: 'Black Eclipse',
  roles: { accent: '#9e1b22', danger: '#d0452f', success: '#5d7b3c', warning: '#b07a1e', pro: '#7a3b62' },
  light: {
    roles: { accent: '#9e1b22', danger: '#b8341f', success: '#4a6a2c', warning: '#8a5a0e', pro: '#6e3157' },
    git: {
      added: '#356023', removed: '#962018', modified: '#7a4c08', merged: '#5e2a4c',
      closed: '#86241c', conflicting: '#7a3d08', draft: '#54463e',
    },
    gray: {
      anchors: {
        'surface-0': '#e3d8c1',
        'surface-1': '#eae0cb',
        'surface-2': '#f2eadb',
        'surface-3': '#f2eadb',
        'text-primary': '#1d1513',
        'text-secondary': '#463832',
        'text-muted': '#5f5048',
      },
    },
  },
  dark: {
    gray: {
      anchors: {
        'surface-0': '#0d0a0a',
        'surface-1': '#151011',
        'surface-2': '#1c1516',
        'surface-3': '#221a1b',
        'text-primary': '#ece2cf',
        'text-secondary': '#c6b9a3',
        'text-muted': '#9d907c',
      },
    },
  },
}

const { theme, problems } = makeColors(PALETTE)

const LOOK: ThemeSetArgs = {
  colors: theme,
  backdrop: { scene: 'black-eclipse', glass: { blur: 3, opacity: 0.42 } },
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const unpainted = problems.find(line => line.startsWith("Desktop won't paint"))

    if (unpainted !== undefined) {
      $.ui.toast(unpainted)
    }
    const set = await $.theme.set(LOOK)

    if (!set.isDrawn) {
      $.ui.status(set.reason)
    }

    return next(e)
  })

  on('ui.render', { component: 'Backdrop' }, ($, e, next) => {
    if ((e.surface !== 'desktop' && e.surface !== 'mobile') || e.props.scene !== 'black-eclipse') {
      return next(e)
    }
    const { Svg } = $.ui.resolve(e)

    return <Svg source={SCENE} alt="A blood-red eclipse over a jagged ridge, a pixel-art swordsman on a crag, crows and drifting embers" isInteractive />
  })
}
