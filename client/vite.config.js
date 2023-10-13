 import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // FIX NOTE: ADD THIS?
  // build: {
  //   sourcemap: true,
  // }
})
