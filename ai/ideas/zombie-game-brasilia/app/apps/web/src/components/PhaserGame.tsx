import React, { forwardRef, useEffect, useLayoutEffect, useRef } from 'react';
import StartGame from '../game/PhaserGame';

/**
 * PhaserGame.tsx — Wrapper React para o canvas do Phaser.
 *
 * Responsabilidades:
 * 1. Criar o container DOM onde o Phaser vai montar o canvas
 * 2. Inicializar o Phaser.Game uma unica vez (via StartGame)
 * 3. Destruir o Phaser.Game quando o componente desmontar (evita memory leak em dev StrictMode)
 * 4. Expor o ref do Phaser.Game para o pai (App.tsx)
 *
 * NÃO fazer aqui:
 * - Nenhuma logica de jogo
 * - Nenhum acesso a scenes do Phaser
 * - Nenhum state do React que mude durante gameplay
 */
interface PhaserGameProps {
  // Adicionar props conforme necessario (ex: onSceneReady, initialScene)
}

const PhaserGame = forwardRef<Phaser.Game, PhaserGameProps>((_props, ref) => {
  const containerRef = useRef<HTMLDivElement>(null);

  useLayoutEffect(() => {
    if (containerRef.current === null) return;

    // Inicializa o Phaser passando o container div como parent
    const game = StartGame(containerRef.current);

    // Expoe o game para o componente pai via ref
    if (typeof ref === 'function') {
      ref(game);
    } else if (ref !== null) {
      ref.current = game;
    }

    return () => {
      // Destruicao limpa — essencial para React StrictMode (double-mount em dev)
      game.destroy(true);
    };
  }, [ref]);

  return (
    <div
      ref={containerRef}
      id="phaser-container"
      style={{
        width: '100%',
        height: '100%',
        position: 'relative',
      }}
    />
  );
});

PhaserGame.displayName = 'PhaserGame';

export default PhaserGame;
