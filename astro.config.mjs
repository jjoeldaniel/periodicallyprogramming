import { defineConfig } from "astro/config";
import vercel from '@astrojs/vercel/serverless';

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
    output: 'hybrid',
    adapter: vercel(),
    integrations: [tailwind()],
    redirects:
    {
        "/github": "https://github.com/jjoeldaniel",
        "/gh": "https://github.com/jjoeldaniel",
        "/resume": "https://github.com/jjoeldaniel/resume/blob/main/resume.pdf",
        "/linkedin": "https://www.linkedin.com/in/joeldanielrico",
        "/mastadon": "https://mastodon.social/@jjoel",
    }
});
