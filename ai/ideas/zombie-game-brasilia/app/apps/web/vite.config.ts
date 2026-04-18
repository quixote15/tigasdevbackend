import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import compression from 'vite-plugin-compression';
import { resolve } from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  base: '/',

  plugins: [
    react(),
    // Gzip pre-comprimido — Cloudflare Pages serve automaticamente
    compression({ algorithm: 'gzip', ext: '.gz' }),
    compression({ algorithm: 'brotliCompress', ext: '.br' }),
  ],

  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
      '@game': resolve(__dirname, 'src/game'),
    },
  },

  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false,
    // Target: Chrome 90+ / Safari 15+ — Android e iOS modernos
    target: ['es2020', 'chrome90', 'safari15'],
    rollupOptions: {
      output: {
        // Phaser em chunk separado: fica em cache entre deploys
        // O codigo do jogo (~50-200 KB) e o unico que muda a cada push
        manualChunks: {
          phaser: ['phaser'],
          react: ['react', 'react-dom'],
        },
      },
    },
  },

  server: {
    port: 5173,
    // Headers COOP/COEP necessarios para SharedArrayBuffer (Web Audio API)
    headers: {
      'Cross-Origin-Embedder-Policy': 'require-corp',
      'Cross-Origin-Opener-Policy': 'same-origin',
    },
  },
});
