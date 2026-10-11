#!/usr/bin/env python3
"""
Generate Profile README for emaf205
Extracts public repositories, categorizes them, and generates an authoritative,
visual full-width card timeline on https://github.com/emaf205.
"""

import os, json, urllib.request

USERNAME = "emaf205"
EXCLUDED = ["emaf205", "github"] # Exclude profile repo itself and archived engine

PROJECTS = [
    # 1. Interactive Web Apps & Offline PWAs
    {
        "name": "silvo-tv",
        "title": "SILVO TV // Retro CRT Video Simulator",
        "category": "Interactive Web App / PWA",
        "tags": ["PWA", "RETRO CRT", "WEB AUDIO", "VANILLA JS"],
        "desc": "Interactive vintage cathode-ray tube television simulator with tactile rotary channel knobs, scanline shaders, and continuous broadcast of historical archives.",
        "demo": "https://emaf205.com/ideas/silvo-tv/",
        "cover": "assets/covers/silvo-tv.jpg"
    },
    {
        "name": "EMAF205-Easy-ChatGPT-Importer",
        "title": "Easy ChatGPT Importer // Offline JSON Archive Reader",
        "category": "Private Web App / PWA",
        "tags": ["PWA", "OFFLINE-FIRST", "JSON PARSER", "MARKDOWN EXPORT"],
        "desc": "Zero-cloud, client-side conversation explorer and markdown exporter for official OpenAI data exports. Sub-second full-text search across gigabytes of history.",
        "demo": "https://emaf205.com/ideas/chatgpt-importer/",
        "cover": "assets/covers/EMAF205-Easy-ChatGPT-Importer.jpg"
    },
    {
        "name": "SIMPLE-PDF-SIGN",
        "title": "Simple PDF Sign // In-Browser Cryptographic Signing",
        "category": "Client-Side Utility / PWA",
        "tags": ["PWA", "CRYPTOGRAPHY", "CANVAS", "ZERO SERVER"],
        "desc": "Pure browser-based digital document signing and cryptographic stamping utility. Zero server uploads, zero cloud dependencies, 100% private.",
        "demo": "https://emaf205.com/ideas/simple-pdf-sign/",
        "cover": "assets/covers/SIMPLE-PDF-SIGN.jpg"
    },
    {
        "name": "ai-diary",
        "title": "AI Diary // Encrypted Local-First Journal",
        "category": "Local-First PWA",
        "tags": ["PWA", "INDEXEDDB", "LOCAL-FIRST", "ENCRYPTION"],
        "desc": "Private personal reflection diary and workflow chronicle with local IndexedDB storage, biometric lock simulation, and zero telemetry.",
        "demo": "https://emaf205.com/ideas/ai-diary/",
        "cover": "assets/covers/ai-diary.jpg"
    },
    {
        "name": "kurt-cobain-street-critic",
        "title": "Kurt Cobain Street Critic // Lo-Fi Grunge Zine",
        "category": "Tactile Web App / Net Art",
        "tags": ["PWA", "LO-FI", "GRUNGE ZINE", "WEB AUDIO", "SATIRE"],
        "desc": "Photocopier halftone zine simulator and satirical street art critique engine. Caustic commentary on modern consumer aesthetics built with Web Audio.",
        "demo": "https://emaf205.com/ideas/kurt-critic/",
        "cover": "assets/covers/kurt-cobain-street-critic.jpg"
    },
    {
        "name": "EASY-PERSONAL-LINKTREE",
        "title": "Easy Personal Linktree // High-Velocity Bio Link Hub",
        "category": "Minimalist Web Hub",
        "tags": ["MOBILE-FIRST", "ZERO BLOAT", "SUB-50MS", "VANILLA CSS"],
        "desc": "Uncompromising, zero-dependency bio link directory loading in under 50 milliseconds. Single-file architecture with tactile mobile touch ergonomcs.",
        "demo": "https://linktr.ee/emaf205",
        "cover": "assets/covers/EASY-PERSONAL-LINKTREE.jpg"
    },
    {
        "name": "EmaF205-LinksX",
        "title": "Links-X // High-Contrast Brutalist Directory",
        "category": "Modern Brutalist Hub",
        "tags": ["BRUTALISM", "HIGH-CONTRAST", "KEYBOARD NAV", "FAST WEB"],
        "desc": "High-contrast, hyper-fast personal link directory built with electric neon accents, obsidian black backgrounds, and zero framework bloat.",
        "demo": "https://emaf205.com/ideas/easy-links/",
        "cover": "assets/covers/EmaF205-LinksX.jpg"
    },

    # 2. Sensory, Audio & Visual Experiments
    {
        "name": "emaf205-tapetone",
        "title": "TapeTone // Analog Cassette Tape & Saturation Synth",
        "category": "Audio Experiment / Web Audio",
        "tags": ["WEB AUDIO", "ANALOG SATURATION", "CASSETTE TAPE", "SYNTH"],
        "desc": "Warm analog acoustic saturation synthesizer and tape reel audio simulator modeling physical magnetic tape imperfections directly in browser memory.",
        "demo": "https://emaf205.com/ideas/tapetone/",
        "cover": "assets/covers/emaf205-tapetone.jpg"
    },
    {
        "name": "gif-tv",
        "title": "GIF TV // Algorithmic Retro Visual Broadcaster",
        "category": "Generative Media / Video Synth",
        "tags": ["RETRO BROADCAST", "GENERATIVE", "CANVAS 2D", "NET ART"],
        "desc": "Algorithmic non-stop retro animated GIF broadcasting station, procedural visual channel switcher, and generative net art installation.",
        "demo": "https://emaf205.com/ideas/gif-tv/",
        "cover": "assets/covers/gif-tv.jpg"
    },
    {
        "name": "torno-subito",
        "title": "Torno Subito // Interactive Spring Physics Sign",
        "category": "Physical Web Art",
        "tags": ["PHYSICS ENGINE", "SPRING DYNAMICS", "VINTAGE ITALIAN", "INTERACTIVE"],
        "desc": "Vintage Italian storefront sign simulation featuring real-time critically damped harmonic spring physics, interactive dragging, and opening hours net art.",
        "demo": "https://emaf205.com/ideas/torno-subito/",
        "cover": "assets/covers/torno-subito.jpg"
    },
    {
        "name": "office-os",
        "title": "Office OS // 90s Corporate Desktop Environment",
        "category": "Retro Desktop Simulator",
        "tags": ["90S DESKTOP", "RETRO OS", "SOUNDBOARD", "AMBIENT"],
        "desc": "Nostalgic 1990s corporate desktop environment, retro operating system simulator, and office soundboard built with semantic DOM components.",
        "demo": "https://emaf205.com/ideas/office-os/",
        "cover": "assets/covers/office-os.jpg"
    },
    {
        "name": "FIXYOUREYES",
        "title": "FIXYOUREYES // Sensory Ocular Relief & Therapy",
        "category": "Sensory Wellness / Ergonomics",
        "tags": ["EYE CARE", "VISUAL THERAPY", "WELLNESS", "PWA"],
        "desc": "Sensory ocular relief utility and visual fatigue exercise tool designed for screen workers, programmers, and designers.",
        "demo": "https://fixyoureyes.netlify.app",
        "cover": "assets/covers/FIXYOUREYES.jpg"
    },

    # 3. Editorial Systems & Typographic Design
    {
        "name": "BRERA-STYLEBOOK",
        "title": "BRERA StyleBook // Swiss Editorial Design System",
        "category": "Design System / CSS Framework",
        "tags": ["SWISS DESIGN", "TYPOGRAPHY", "DESIGN SYSTEM", "CSS"],
        "desc": "Precision Swiss typographic design system and CSS framework curated in Milan. Modular scales, print-grade microtypography, and anti-AI design patterns.",
        "demo": "https://brera-stylebook.netlify.app/",
        "cover": "assets/covers/BRERA-STYLEBOOK.jpg"
    },
    {
        "name": "DEAD-TEXT-SOCIETY",
        "title": "Dead Text Society // Literary Typography Crypt",
        "category": "Editorial Zine / Literature",
        "tags": ["EDITORIAL", "TYPOGRAPHY", "LITERARY CRYPT", "ZINE"],
        "desc": "Interactive typographical cemetery and dark zine exhibition for preserving fragmented prose, forgotten thoughts, and discarded manuscripts.",
        "demo": "https://emaf205.com/ideas/dead-text-society/",
        "cover": "assets/covers/DEAD-TEXT-SOCIETY.jpg"
    },
    {
        "name": "transcript-to-magazine-ai",
        "title": "Transcript to Magazine AI // Monograph Publisher",
        "category": "Publishing Pipeline / CSS Paged Media",
        "tags": ["CSS PAGED MEDIA", "EDITORIAL PRINT", "AI SESSIONS", "PDF EXPORT"],
        "desc": "Architectural publishing pipeline transforming raw conversational AI dialogue logs into museum-grade, multi-column editorial magazines.",
        "demo": "https://emaf205.com",
        "cover": "assets/covers/transcript-to-magazine-ai.jpg"
    },
    {
        "name": "emaf205-landing",
        "title": "EMAF205 Landing // Architectural Portfolio Showcase",
        "category": "Portfolio Architecture",
        "tags": ["EDITORIAL", "SWISS TYPOGRAPHY", "PHP ROUTING", "LIGHTWEIGHT"],
        "desc": "Architectural, editorial portfolio landing page built with Swiss typographic discipline, modular layout grids, and lightweight vanilla code.",
        "demo": "https://emaf205.com",
        "cover": "assets/covers/emaf205-landing.jpg"
    },

    # 4. AI Tools, Governance & Reasoning Engines
    {
        "name": "prompt-search",
        "title": "Prompt Search // Sub-Millisecond AI Prompt Catalog",
        "category": "Client-Side Search Engine",
        "tags": ["PROMPT ENGINEERING", "SEARCH ENGINE", "CLIENT-SIDE", "AI TOOLS"],
        "desc": "Ultra-fast, zero-dependency browser search engine and visual catalog for production prompts, system personas, and agent directives.",
        "demo": "https://emaf205.com/ideas/prompt-search/",
        "cover": "assets/covers/prompt-search.jpg"
    },
    {
        "name": "ai-policy-builder",
        "title": "AI Policy Builder // Corporate Governance Generator",
        "category": "Compliance Tool / Web App",
        "tags": ["AI GOVERNANCE", "COMPLIANCE", "ENTERPRISE AI", "POLICY"],
        "desc": "Enterprise generative AI governance and ethical policy generator for studios and companies. Generates customized legal compliance frameworks.",
        "demo": "https://emaf205.com/ideas/ai-policy-builder/",
        "cover": "assets/covers/ai-policy-builder.jpg"
    },
    {
        "name": "Rex-for-ChatGPT",
        "title": "REX // Ruthless Executive Reasoning Persona",
        "category": "Reasoning Directive / System Prompt",
        "tags": ["SYSTEM PROMPT", "REASONING", "FORENSIC CODE REVIEW", "ANTI-SLOP"],
        "desc": "High-density executive system prompt and adversarial reasoning persona for forensic engineering, architecture review, and zero-bullshit problem solving.",
        "demo": "https://github.com/emaf205/Rex-for-ChatGPT",
        "cover": "assets/covers/Rex-for-ChatGPT.jpg"
    },

    # 5. Developer Utilities & Release Pipelines
    {
        "name": "static-folder-publisher",
        "title": "Static Folder Publisher // Zero-Noise Deploy CLI",
        "category": "CLI Tool / Python",
        "tags": ["CLI", "PYTHON", "FTP DEPLOY", "METADATA SANITIZER"],
        "desc": "Opinionated Python CLI tool for deploying and syncing local static folders to web servers with automated OS metadata sanitization (.DS_Store strip).",
        "demo": "https://github.com/emaf205/static-folder-publisher",
        "cover": "assets/covers/static-folder-publisher.jpg"
    },
    {
        "name": "emaf205-snap",
        "title": "SNAP // Viewport Framing & Screenshot Utility",
        "category": "Browser Tool / Mockup Engine",
        "tags": ["SCREENSHOT", "VIEWPORT FRAMING", "CANVAS", "DESIGN UTILITY"],
        "desc": "Lightweight viewport capture and mockup framing utility creating clean, distraction-free visual presentations for web apps.",
        "demo": "https://github.com/emaf205/emaf205-snap",
        "cover": "assets/covers/emaf205-snap.jpg"
    },
    {
        "name": "FTP-Minimal-Archive",
        "title": "FTP Minimal Archive // Static Directory Indexer",
        "category": "Static File Browser",
        "tags": ["PHP", "DIRECTORY BROWSER", "ZERO DATABASE", "DEPLOYMENT"],
        "desc": "Single-file static directory explorer and lightweight FTP release bundle browser for shared hosting and asset archiving.",
        "demo": "https://github.com/emaf205/FTP-Minimal-Archive",
        "cover": "assets/covers/FTP-Minimal-Archive.jpg"
    }
]

def render_readme():
    lines = []
    lines.append('<p align="center">')
    lines.append('  <img src="assets/social-preview.jpg" alt="Emanuele BDC // Creative Technologist & AI Architect" width="100%">')
    lines.append('</p>\n')
    lines.append('<h1 align="center">Emanuele BDC (EmaF205)</h1>')
    lines.append('<p align="center">')
    lines.append('  <b>Creative Technologist & AI Systems Architect // Milan, Italy</b><br>')
    lines.append('  <i>Generative systems, client-first web tools, sensory interfaces & editorial architectures.</i>')
    lines.append('</p>\n')
    lines.append('<p align="center">')
    lines.append('  <a href="https://emaf205.com"><img src="https://img.shields.io/badge/Official_Website-emaf205.com-e63946?style=for-the-badge&logo=safari" alt="Website"></a>')
    lines.append('  <a href="https://github.com/emaf205"><img src="https://img.shields.io/badge/GitHub_Showcase-22_Active_Projects-181a20?style=for-the-badge&logo=github" alt="Projects"></a>')
    lines.append('  <a href="https://github.com/emaf205/emaf205/actions"><img src="https://img.shields.io/badge/Automated_Profile-100%25_Hands--Free-242733?style=for-the-badge&logo=github-actions" alt="Actions"></a>')
    lines.append('</p>\n')
    lines.append('---\n')
    lines.append('## 🏛️ Architectural Manifesto\n')
    lines.append('Digital craftsmanship operating at the convergence of **Swiss design discipline** and **frontier artificial intelligence**:\n')
    lines.append('- **Anti-AI Slop & Radical Simplicity**: Eliminating conversational filler, generic card soup, and neon clichés. Every element exists with structural and typographical intention.')
    lines.append('- **Client-Side Sovereignty**: Prioritizing zero-cloud, offline-first architectures (IndexedDB, Web Audio, Canvas, Service Workers). What can run privately in browser memory never touches remote servers.')
    lines.append('- **Zero Framework Bloat**: Pure vanilla web standards (modern ES6+, semantic HTML5, CSS custom properties). Sub-100ms render speeds and negligible dependency footprints.')
    lines.append('- **Forensic Execution**: Mathematical verification, strict quality gates, and surgical implementation.\n')
    lines.append('---\n')
    lines.append('## 🌟 Creative Projects Feed // Visual Timeline\n')
    lines.append('> *A continuous, full-width visual feed of production web apps, sensory prototypes, and open-source tools.*\n')

    for idx, p in enumerate(PROJECTS, 1):
        repo_url = f"https://github.com/{USERNAME}/{p['name']}"
        tags_str = " ".join([f"`{t}`" for t in p["tags"]])
        
        lines.append(f'<p align="center">')
        lines.append(f'  <a href="{repo_url}">')
        lines.append(f'    <img src="{p["cover"]}" alt="{p["title"]}" width="100%">')
        lines.append(f'  </a>')
        lines.append(f'</p>\n')
        lines.append(f'### {idx}. [{p["title"]}]({repo_url})')
        lines.append(f'{tags_str}\n')
        lines.append(f'> {p["desc"]}\n')
        
        btn_line = f'<a href="{repo_url}"><img src="https://img.shields.io/badge/GitHub-Repository-181a20?style=for-the-badge&logo=github" alt="Repository"></a> '
        if p.get("demo") and p["demo"] != repo_url:
            btn_line += f'<a href="{p["demo"]}"><img src="https://img.shields.io/badge/Live_Demo-Launch_App-e63946?style=for-the-badge&logo=google-chrome" alt="Live Demo"></a>'
        lines.append(f'<p>{btn_line}</p>\n')
        lines.append('---\n')

    lines.append('## 🛠️ Technology & Creative Craft\n')
    lines.append('```')
    lines.append('Frontend Engineering : Pure ES6+, Semantic HTML5, CSS Grid / Paged Media, Swiss Typographic Scales')
    lines.append('Sensory & Graphics   : Web Audio API Synthesizers, Canvas 2D Shaders, Harmonic Spring Physics')
    lines.append('Application Core     : Offline-First PWAs, Service Worker Caching, Local-First IndexedDB')
    lines.append('AI Systems           : Multi-Agent Architectures, Forensic Reasoning Prompts, Tool Gateways')
    lines.append('Backend & Pipelines  : Python 3.12, PHP 8.2, Automated GitHub Actions & Deployment Sync')
    lines.append('```\n')
    lines.append('---\n')
    lines.append('## 📬 Connect & Collaborate\n')
    lines.append('- **Official Portfolio & Home**: [emaf205.com](https://emaf205.com)')
    lines.append('- **Location**: Milan, Italy')
    lines.append('- **GitHub Profile**: [@emaf205](https://github.com/emaf205)\n')
    lines.append('<p align="center">')
    lines.append('  <sub>Automated with GitHub Actions. Crafted with architectural discipline by Emanuele BDC in Milan, Italy.</sub>')
    lines.append('</p>\n')

    return "\n".join(lines)

if __name__ == "__main__":
    content = render_readme()
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("README.md successfully generated with", len(PROJECTS), "cards!")
