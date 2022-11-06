import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'



module.exports = {  publicPath: process.env.NODE_ENV === "production" ? "/swe_class_project/" : "/",};