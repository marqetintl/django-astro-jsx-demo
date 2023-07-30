import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";

import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: "http://example.com",
  integrations: [mdx(), sitemap()],
  output: "static",
  outDir: "../django/templates/astro/",
  publicDir: "../django/media/",
  trailingSlash: "always",
  compressHTML: process.env.NODE_ENV === "production",
  build: {
    copyPublicDir: false,
    format: "file",
    inlineStylesheets: "auto",
    assets: "static",
  },
});