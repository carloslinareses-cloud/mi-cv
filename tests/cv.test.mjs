import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const [web, printable, sitemap] = await Promise.all([
  readFile(new URL("../index.html", import.meta.url), "utf8"),
  readFile(new URL("../print.html", import.meta.url), "utf8"),
  readFile(new URL("../sitemap.xml", import.meta.url), "utf8"),
]);

const publicUrls = [
  "https://panavoy.com",
  "https://play.google.com/store/apps/details?id=com.panavoy.app",
  "https://admin.panavoy.com",
  "https://socios.panavoy.com",
  "https://alcaldiadecharallave.com",
  "https://asistencia.alcaldiadecharallave.com",
  "https://salasituacional.alcaldiadecharallave.com",
  "https://resuelia.pages.dev",
  "https://elearningcharallave.github.io/elearning/",
  "https://aerosocio.es",
  "https://eterniaot.com",
  "https://classic.eterniaot.com",
  "https://sumatevzla.org",
];

test("the web and printable CVs expose every verified public product", () => {
  for (const url of publicUrls) {
    assert.ok(web.includes(url), `Missing from index.html: ${url}`);
    assert.ok(printable.includes(url), `Missing from print.html: ${url}`);
  }
});

test("the bilingual web copy stays paired", () => {
  const spanishFields = web.match(/data-es=/g) ?? [];
  const englishFields = web.match(/data-en=/g) ?? [];

  assert.ok(spanishFields.length >= 90, "Expected the complete bilingual CV");
  assert.equal(spanishFields.length, englishFields.length);
});

test("the web document has unique element ids", () => {
  const ids = [...web.matchAll(/\sid=["']([^"']+)["']/g)].map((match) => match[1]);
  const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);

  assert.deepEqual([...new Set(duplicates)], []);
});

test("external web links use a safe new tab", () => {
  const links = [...web.matchAll(/<a\b[^>]*href=["']https?:\/\/[^"']+["'][^>]*>/g)].map(
    (match) => match[0],
  );

  assert.ok(links.length >= publicUrls.length);
  for (const link of links) {
    assert.match(link, /target=["']_blank["']/);
    assert.match(link, /rel=["']noopener noreferrer["']/);
  }
});

test("technology coverage and current municipal release are documented", () => {
  const combined = `${web}\n${printable}`;
  const technologies = [
    "Kotlin",
    "Jetpack Compose",
    "TypeScript",
    "React",
    "Python",
    "Firebase",
    "Supabase",
    "PostgreSQL",
    "Cloudflare",
    "Docker",
    "Playwright",
    "OpenAI API",
    "SumUp",
    "Wompi",
  ];

  for (const technology of technologies) {
    assert.ok(combined.includes(technology), `Missing technology: ${technology}`);
  }
  assert.ok(combined.includes("v1.0.17"));
  assert.ok(!combined.includes("v1.0.8"));
  assert.ok(!combined.includes("En revisión final Play Store"));
});

test("the sitemap records this CV revision", () => {
  assert.match(sitemap, /<lastmod>2026-07-14<\/lastmod>/);
});
