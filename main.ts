// News-image entry (Node 22, standard library only): copies the entry image
// (entry.png beside this file) to the grader's output directory as
// /output/entry.png. The gate takes a whole PNG or JPEG of at most 1 MiB
// and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const MAX_BYTES = 1024 * 1024;
const MAX_DIMENSION = 1024;

const source = new URL('./entry.png', import.meta.url);
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outDir, 'entry.png');

if (!existsSync(source)) {
  throw new Error(`entry image not found: ${source.pathname}`);
}

const bytes = statSync(source).size;
if (bytes > MAX_BYTES) {
  throw new Error(`entry image is ${bytes} bytes, over the ${MAX_BYTES} byte limit`);
}

// Read the PNG header (IHDR) to report the pixel dimensions; the copy
// itself does not depend on this, so a parse failure only hides the log.
let dimensions = 'unknown';
try {
  const header = readFileSync(source).subarray(0, 29);
  const width = header.readUInt32BE(16);
  const height = header.readUInt32BE(20);
  dimensions = `${width}x${height}`;
  if (width > MAX_DIMENSION || height > MAX_DIMENSION) {
    throw new Error(`entry image is ${dimensions}, over the ${MAX_DIMENSION}x${MAX_DIMENSION} limit`);
  }
} catch (error) {
  if (error instanceof Error && error.message.includes('over the')) throw error;
  dimensions = 'unknown';
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log(`copied entry.png (${bytes} bytes, ${dimensions}) to ${target}`);
