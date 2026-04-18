import React, { useRef } from 'react';
import PhaserGame from './components/PhaserGame';

/**
 * App.tsx — Shell mínimo.
 *
 * React gerencia o container. Phaser gerencia o canvas.
 * Comunicacao entre eles via EventBus (src/game/EventBus.ts).
 *
 * Regras:
 * - App.tsx nao conhece nada de Phaser diretamente
 * - HUD, menus e overlays React sao filhos de PhaserGame (montados sobre o canvas)
 * - Estado de gameplay nao vive no React state — fica no EventBus / Phaser scene data
 */
const App: React.FC = () => {
  const phaserRef = useRef<Phaser.Game | null>(null);

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background: '#0a0a0a',
      }}
    >
      <PhaserGame ref={phaserRef} />
    </div>
  );
};

export default App;
